import pip._vendor.requests 
import requests
import subprocess
import sqlite3



from bs4 import BeautifulSoup
import pandas as pd
searchterm=input('please enter your searchterm')
desired_price=int(input('please enter desired price'))




def get_data(searchterm):
    url=f'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw={searchterm}&_sacat=0'
    r=requests.get(url)
    soup=BeautifulSoup(r.text, 'html.parser')
    return soup





def parse(soup):
    productlist=[]
    results= soup.find_all('div',{'class': 's-item__info clearfix'})
    for item in results:
        product={
            'title':item.find('div',{'class':'s-item__title'}).text,
            'sellingprice': float(item.find('span',{'class':'s-item__price'}).text.replace('$','').replace(',','').strip()),
            
            'bids':item.find('span',{'class': 's-item__bids s-item__bidCount'}),
            'link':item.find('a',{'class': 's-item__link'})['href'],
            
        }
        
        #print(product)
        productlist.append(product)
        
    
    return productlist
def output(productlist):
    productsdf=pd.DataFrame(productlist)
    productsdf.to_csv('output2.csv',index=False)
    print('saved to csv')
    return
def send_mac_notification(title, message):
    script = f'display notification "{message}" with title "{title}"'
    subprocess.call(["osascript", "-e", script])

# Modify the table creation to set unique constraint on title and link
def setup_database():
    conn = sqlite3.connect('listings.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS listings (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        sellingprice REAL NOT NULL,
        link TEXT NOT NULL UNIQUE
    )
    ''')
    
    conn.commit()
    conn.close()

def insert_listing(title, sellingprice, link):
    conn = sqlite3.connect('listings.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
        INSERT INTO listings (title, sellingprice, link)
        VALUES (?, ?, ?)
        ''', (title, sellingprice, link))
        conn.commit()
        conn.close()
        return True  # Return True indicating new listing was added
    except sqlite3.IntegrityError:
        # This means the listing is already in the database (because the link is unique).
        conn.close()
        return False  # Return False indicating listing was not added
def fetch_listings():
    conn = sqlite3.connect('listings.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM listings')
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()



setup_database()
fetch_listings()

send_mac_notification("Ebay Price Tracker", "New listing available!")

setup_database()
new_listings_found = False  # Flag to check if any new listings were found

soup = get_data(searchterm)
productlist = parse(soup)



for product in productlist:
    if product['sellingprice'] < desired_price:
        is_new = insert_listing(product['title'], product['sellingprice'], product['link'])
        if is_new:
            new_listings_found = True  # Update the flag
            output = f"Title: {product['title']}\nPrice: ${product['sellingprice']}\nLink: {product['link']}\n{'-'*50}"
            print(output)  # Print the new listing details

# Send a notification if there are new listings
if new_listings_found:
    send_mac_notification("Ebay Price Tracker", "New listings available!")
else:
    print("No new listings found.")