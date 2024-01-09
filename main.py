import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# service = Service("C:/Program Files/Google/Chrome/Application/chrome.exe")
# driver = webdriver.Chrome(service=service)
driver = webdriver.Chrome()
error_url = "https://docs.oracle.com/en/error-help/db/ora-00001/"


def crawl(http_url):
    print("here-0")
    try:
        driver.get(http_url)
        current_url = driver.current_url
        print("here-1")
        if current_url != http_url:
            print("Redirected to:", current_url)
            crawl(current_url)
        print("here-2")

        # Wait for the contentContainer div to be present
        element = WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.TAG_NAME, "main")))
        print("here-3")

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        print("here-4")
        div_wrap = soup.find("main")
        print(f"div_wrap: {div_wrap}")
        print(f"div_wrap: {div_wrap.get_text()}")
        time.sleep(2)  # Add a small delay to allow the page to fully load
    except Exception as e:
        print(e)
    finally:
        driver.quit()


crawl(error_url)
