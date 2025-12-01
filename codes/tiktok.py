import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from typing import Literal
import os



CHROME_DRIVER_PATH = "/usr/bin/chromedriver"

OP = webdriver.ChromeOptions()
# OP.add_argument('--headless')  
OP.add_argument("--disable-blink-features=AutomationControlled")

OP.add_argument("--no-sandbox")
OP.add_argument("--disable-dev-shm-usage")
OP.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36")

service = Service(executable_path=CHROME_DRIVER_PATH)

driver = webdriver.Chrome(service=service, options=OP)


class TiktokBot:
    def __init__(self):
        pass

    def scrape(self, keyword: str, n):
        driver.get(f"http://tiktok.com/search?q={keyword}")
        time.sleep(5)


        try:
            cards = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[data-e2e='search_top-item']"))
            )

            i = 0
            while i <= n:

                cards[i].click()
                try:


                    likes = WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "strong[data-e2e='browse-like-count']"))
                    )

                    comments = WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "strong[data-e2e='browse-comment-count']"))
                    )

                    captions = WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-e2e='browse-video-desc']"))
                    )


                    # account_names = WebDriverWait(driver, 20).until(
                    #     EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-e2e='browse-username']"))
                    # )


                    video_links = WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "p[data-e2e='browse-video-link']"))
                    )
                    

                    print(likes.text, comments.text, captions.text, video_links.text)
                except Exception as e:
                    print(e)

                i += 1

                if i == n:
                    break

                time.sleep(5)
                driver.back()
                time.sleep(5)


        except Exception as e:

            print(f"Eror brow: \n{e}")
    


    