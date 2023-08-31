# Ebay_Price_Tracker
This script allows users to track products on eBay based on a specific search term and a desired price point.
Functionality:

User Input: The user provides a search term (e.g., "iPhone 12") and a desired price (e.g., $500).

Data Retrieval:

The script fetches product listings from eBay using the search term provided.
Using the requests library, it sends a GET request to eBay's search URL.
The page's HTML is then parsed using BeautifulSoup to extract product information.
Data Parsing:

The script looks for product listings in the parsed HTML.
For each product found, it extracts the title, selling price, bid count (if any), and link to the product.
This data is aggregated into a list of product dictionaries.
Data Storage:

The script employs SQLite to maintain a database (listings.db).
A table named listings is created if it doesn't already exist. This table has columns for the product title, selling price, and a unique link to ensure no duplicates.
Products with selling prices below the desired price are inserted into this database.
Notifications and Outputs:

If a new listing (not previously stored in the database) matches the criteria (i.e., selling price below the desired price), details of the product are printed to the console.
Additionally, the product details are saved in a CSV file named output2.csv.
The user is notified via a macOS notification about any new listings found.
Database Interaction:

On initialization, the script sets up the database (if it doesn't exist) and fetches and prints any listings already stored in it.
It checks new listings against the database and only adds unique listings (based on the product link).
Automation Potential:

Though not inherent in the script, it can be set up to run periodically (e.g., daily) using tools like cron (for macOS/Linux) or Task Scheduler (for Windows) to provide updated listings and notifications.
Dependencies:

requests for fetching web pages.
BeautifulSoup from bs4 for parsing HTML.
sqlite3 for database operations.
pandas for CSV data operations.
subprocess to send macOS notifications.
Use Case:
This script is ideal for users who are looking to track product prices on eBay. By setting a desired price, they can be immediately notified of any listings that match their criteria, allowing them to take advantage of deals or price drops.

