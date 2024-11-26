import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("user-agent = your user agent")

download_dir = "downloads"
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

prefs = {
    "download.default_directory": os.path.abspath(download_dir),
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safe browsing.enabled": True
}
chrome_options.add_experimental_option("prefs", prefs)

service = Service('your chrome driver path') 
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    
    driver.get("https://www.nseindia.com/all-reports")  
    time.sleep(10)

    report_div = driver.find_element(By.XPATH, "//div[@id='cr_equity_daily_Current']")

    report_divs = report_div.find_elements(By.XPATH,"//div[contains(@class, 'reportsDownload')]")

    for report in report_divs:
        data_link = report.get_attribute("data-link")
        print(f"Downloading from: {data_link}")

        driver.get(data_link)
        time.sleep(5)

finally:
    driver.quit()

