## dbmongo의 collection 연결
from pymongo import MongoClient
mongoClient = MongoClient("mongodb://192.168.10.240:27017")
# database 연결
database = mongoClient["healthcare_project"]
collection = database['FHP_article']
# collection.delete_many({})

# 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import requests

import time


# Chrome 드라이버 설치 디렉터리 설정
webdriver_manager_directory = ChromeDriverManager().install()

# Chrome 브라우저 옵션 설정
chrome_options = Options()
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")

# WebDriver 생성
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory), options=chrome_options)

# 크롤링할 웹 페이지 URL
url = "https://pubmed.ncbi.nlm.nih.gov/?term=forward+head+posture&sort=date"
html_source = browser.get(url)
first_content = browser.find_element(by=By.CSS_SELECTOR,value='#search-results > section.search-results-list > div.search-results-chunks > div > article:nth-child(2) > div.docsum-wrap > div.docsum-content > a')
first_content.click()

# 웹 페이지 열기
while True:
    time.sleep(2)
    article_title = browser.find_element(by=By.CSS_SELECTOR,value='h1.heading-title').text
    article_date =  browser.find_element(by=By.CSS_SELECTOR,value='span.cit').text
    article_date = article_date.split(";")[0]
    article_date = article_date.split(":")[0]
    try:
        abstract =  browser.find_element(by=By.CSS_SELECTOR,value='div.abstract > div').text
    except:
        abstract = ''
    print(article_title)
    print(article_date)
    print(abstract)
        # mongodb 삽입
    data = {
        'title' : article_title,
        'date': article_date,
        'abstract' : abstract,
    }

    # MongoDB 컬렉션에 데이터 삽입
    collection.insert_one(data)
    try:
        next_btn = browser.find_element(by=By.CSS_SELECTOR,value='#adjacent-navigation > div.next.side-link.visible > a')
        next_btn.click() 
    except : 
        break

# 브라우저 종료
browser.quit()