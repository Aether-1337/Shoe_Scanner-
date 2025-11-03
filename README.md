
Trainer Price Scraper: StockX & eBay UK

A Python script that automates the search for a specific sneaker—**Nike Air Max 1 Pinnacle Ocean Fog UK 7.5**, you can edit the search by amednding code line 8 and price on code line 21 and 62 —across StockX and eBay UK. It scrapes listings, filters by price, and displays matching results under £160.

---

 Table of Contents
- [Features](#-features)
- [Requirements](#-requirements)
- [Setup](#-setup)
- [Usage](#-usage)
- [Output](#-output)
- [Notes](#-notes)
- [Future Enhancements](#-future-enhancements)

---

 Features
- Searches StockX and eBay UK for the target sneaker
- Filters results priced at or below £160
- Displays product name, price, source, and direct URL
- Fully automated using Selenium WebDriver

---

 Requirements
- Python 3.7+
- Google Chrome installed
- ChromeDriver (compatible with your Chrome version)
- Python packages:
  ```bash
  pip install selenium



 Setup
- Clone this repository:
git clone https://github.com/your-username/sneaker-price-scraper.git
cd sneaker-price-scraper
- Ensure ChromeDriver is installed and accessible in your system PATH.
- Run the script:
python sneaker_scraper.py


 Usage
The script will:
- Open StockX and eBay UK in Chrome
- Search for the sneaker
- Wait for results to load
- Print matches under £160

 
 Output
If matching results are found:
 Matching Results:
- Nike Air Max 1 Pinnacle Ocean Fog | £155.00 | StockX | https://...
- Nike Air Max 1 Pinnacle Ocean Fog | £149.99 | eBay | https://...


If no matches are found:
 No matches found under £160.



 Notes
- This script uses time.sleep(5) to allow pages to load—adjust if needed.
- Web scraping is sensitive to site layout changes. If the script breaks, inspect the site and update class names accordingly.
- Always respect site terms of service when scraping.

 Future Enhancements
- Add support for multiple sneaker queries
- Implement headless browsing for faster execution
- Export results to CSV or JSON
- Add GUI or Streamlit dashboard interface

 Author
 by Aether

 License
This project is licensed under the MIT License. See the LICENSE file for details.



