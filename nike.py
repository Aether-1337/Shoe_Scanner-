from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

def search_stockx():
    print("\n🔍 Searching StockX...")
    query = "Nike Air Max 1 Pinnacle Ocean Fog UK 7.5"
    driver = webdriver.Chrome(service=Service())
    driver.get(f"https://stockx.com/search?s={query}")
    time.sleep(5)

    results = []
    for item in driver.find_elements(By.CLASS_NAME, "css-1msuq50"):
        try:
            name = item.find_element(By.CLASS_NAME, "css-3lpefb").text
            price_text = item.find_element(By.CLASS_NAME, "css-1vvcwn9").text
            price = float(price_text.replace("£", "").replace(",", "").strip())
            link = item.find_element(By.TAG_NAME, "a").get_attribute("href")

            if price <= 160:
                results.append({"name": name, "price": price, "url": link, "source": "StockX"})
        except:
            continue

    driver.quit()
    return results

def search_ebay():
    print("\n🔍 Searching eBay UK...")
    query = "Nike Air Max 1 Pinnacle Ocean Fog UK 7.5"
    driver = webdriver.Chrome(service=Service())
    driver.get(f"https://www.ebay.co.uk/sch/i.html?_nkw={query}")
    time.sleep(5)

    results = []
    for item in driver.find_elements(By.CLASS_NAME, "s-item"):
        try:
            name = item.find_element(By.CLASS_NAME, "s-item__title").text
            price_text = item.find_element(By.CLASS_NAME, "s-item__price").text
            price = float(price_text.replace("£", "").split()[0].replace(",", ""))
            link = item.find_element(By.CLASS_NAME, "s-item__link").get_attribute("href")

            if price <= 160:
                results.append({"name": name, "price": price, "url": link, "source": "eBay"})
        except:
            continue

    driver.quit()
    return results

def main():
    stockx_results = search_stockx()
    ebay_results = search_ebay()

    all_results = stockx_results + ebay_results
    if all_results:
        print("\n🎯 Matching Results:")
        for r in all_results:
            print(f"- {r['name']} | £{r['price']} | {r['source']} | {r['url']}")
    else:
        print("\n❌ No matches found under £160.")

if __name__ == "__main__":
    main()