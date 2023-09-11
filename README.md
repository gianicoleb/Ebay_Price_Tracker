# eBay Price Tracker

I originally made this project because of my decade long obsession with vintage sweaters. Specifically, it is Coogi brand sweaters that I have fawned over. They generally go for $250-$300, but if you're lucky you can catch a dad or grandpa doing some spring cleaning and snag one for $50. I searched ebay regulared for years with no luck, and found 2 I could affford within a week of using this program

The eBay Price Tracker is a Python-based project designed to streamline the process of tracking product prices on eBay. When a product is listed below a specified price threshold, the user is instantly notified, allowing them to grab deals as they appear.

## Overview:

This tool leverages web scraping techniques and a local SQLite database to monitor eBay listings and notify users when there's a match.

### Key Components:

- **Web Scraping with BeautifulSoup:** Scans eBay for the desired product listings.
- **SQLite Database:** Stores product listings to ensure users are notified only once per listing.
- **Mac Notifications:** Provides a user-friendly notification experience.
- **CSV Output:** Allows the user to maintain a permanent record of tracked products.

## Why This Approach?

1. **BeautifulSoup over API:** While eBay offers an API, web scraping provides more flexibility without the constraints of rate limits or potential API changes.
2. **SQLite for Local Storage:** SQLite offers a lightweight and serverless database solution, ideal for standalone applications. No setup or connection strings are required.
3. **Mac Notifications for User Interaction:** Direct OS notifications are user-friendly and immediate, ensuring users don't miss out on deals.
4. **CSV for Record-keeping:** A universal format for data storage and review. Users can easily import this into other tools or share with others.

## Setup:

### Requirements:

- Python 3.x
- BeautifulSoup4: For web scraping.
- Pandas: For data handling and CSV operations.
- SQLite: As a lightweight relational database.
- Requests: To make HTTP requests to eBay.

### Installation:

1. **Set Up Python:**
   Ensure you have Python 3.x installed. You can check with:
   ```bash
   python --version

