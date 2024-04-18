## dbmongo의 collection 연결
from pymongo import MongoClient
mongoClient = MongoClient("mongodb://127.0.0.1:27017")
# database 연결
database = mongoClient["healthcare_sideproject"]
# collection 작업
collection = database['PMC_FHP_data']
# collection.delete_many({})
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
url = "https://www.ncbi.nlm.nih.gov/pmc"

# 웹 페이지 열기
html_source = browser.get(url)

search = browser.find_element(by=By.CSS_SELECTOR,value="#pmc-search")
search.send_keys("forward head posture")
search_click = browser.find_element(by=By.CSS_SELECTOR,value="#main-content > section > div > div:nth-child(3) > form > div > button")
search_click.click()
time.sleep(3)
article_list = browser.find_elements(by=By.CSS_SELECTOR,value="#maincontent > div > div:nth-child(5) > div > div.rslt > div.title > a")
page_num = 0
while True:
    for i in range(len(article_list)):
        article_list = browser.find_elements(by=By.CSS_SELECTOR,value="#maincontent > div > div:nth-child(5) > div > div.rslt > div.title > a")
        article_list[i].click()
        time.sleep(2)
        try:
            article_date = browser.find_element(by=By.CSS_SELECTOR,value="span.fm-vol-iss-date").text
        except:
            article_date = ""
        try:
            article_title = browser.find_element(by=By.CSS_SELECTOR,value="h1.content-title").text
        except : 
            article_title = ""
        abstract =""
        article_abstract= browser.find_elements(by=By.CSS_SELECTOR,value="div#Abs1")
        if len(article_abstract) == 0:
            article_abstract=  browser.find_elements(by=By.CSS_SELECTOR,  value='div[id^="abs"]')
            pass
        for j in range(len(article_abstract)):
            abstract =abstract + article_abstract[j].text + " "
        abstarct = abstract.lower()
        if abstract.find("head forward posture") or abstract.find("forward head posture"):
            print(article_date)
            print(article_title)
            print(abstract)
            collection.insert_one({"title": article_title,"artical_date":article_date,"abstract_list":abstract})

        else:
            print("not forward head posture")
        print("--------------------------------------")
        
        browser.back()
        time.sleep(2)
        print(page_num)
    try:
        page_num = page_num + 1
        next_btn = browser.find_element(by=By.CSS_SELECTOR,value="a.next")
        next_btn.click()
        time.sleep(3)
    except:
        break
pass