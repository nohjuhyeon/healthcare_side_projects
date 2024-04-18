## dbmongo의 collection 연결
from pymongo import MongoClient
mongoClient = MongoClient("mongodb://192.168.10.240:27017/")
# database 연결
database = mongoClient["healthcare_sideproject"]
# collection 작업
collection = database['naver_FHP_data']
collection.delete_many({})
# insert 작업 진행
# 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

import time


# Chrome 드라이버 설치 디렉터리 설정
webdriver_manager_directory = ChromeDriverManager().install()

# Chrome 브라우저 옵션 설정
chrome_options = Options()
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")

# WebDriver 생성
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory), options=chrome_options)

# 크롤링할 웹 페이지 URL
url = "https://academic.naver.com/search.naver?query=%22forward+head+posture%22&field=0&sort=2&searchType=1&refineType=exist&docType=&thesisLv=&journalLv=&access=&year=&category=&journal=&source=&page=1"

# 웹 페이지 열기
html_source = browser.get(url)
time.sleep(2)
while True:
    page_list = browser.find_elements(by=By.CSS_SELECTOR, value='body > div.wrap > div.container > div > div > div.main_area > div > div.ui_paging_small > span.ui_paging_small_list > a')
    for j in range(len(page_list)):
        list_article = browser.find_elements(by=By.CSS_SELECTOR,value="body > div.wrap > div.container > div > div > div.main_area > div > div.ui_listing > div > ul > li")
        for i in range(len(list_article)):
            list_article = browser.find_elements(by=By.CSS_SELECTOR,value="body > div.wrap > div.container > div > div > div.main_area > div > div.ui_listing > div > ul > li")
            list_title_link = list_article[i].find_element(by=By.CSS_SELECTOR,value="div.ui_listing_info > h4 > a")
            date = list_article[i].find_element(by=By.CSS_SELECTOR,value='span.ui_listing_source').text

            list_title_link.click()
            time.sleep(1)
            try : 
                title = browser.find_element(by=By.CSS_SELECTOR,value='p.ui_listdetail_subtxt').text
            except : 
                try: 
                    title = browser.find_element(by=By.CSS_SELECTOR,value='#articleData').text
                except:
                    title = ""
            try:
                abstract = browser.find_element(by=By.CSS_SELECTOR,value="#div_abstract > p").text
            except:
                abstract = ""
            collection.insert_one({"title": title,"artical_date":date,"abstract_list":abstract})
            print(title)
            print(abstract)
            print(date)

            browser.back()
        page_list = browser.find_elements(by=By.CSS_SELECTOR, value='body > div.wrap > div.container > div > div > div.main_area > div > div.ui_paging_small > span.ui_paging_small_list > a')

        page_list[j].click()
    try:
        next_block = browser.find_element(by=By.CSS_SELECTOR,value='body > div.wrap > div.container > div > div > div.main_area > div > div.ui_paging_small > a.spimg.ui_paging_small_btn.move_next')
        next_block.click()
    except:
        break
pass