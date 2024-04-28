## dbmongo의 collection 연결
from pymongo import MongoClient
mongoClient = MongoClient("mongodb://trainings.iptime.org:48003/")
# database 연결
database = mongoClient["healthcare_sideproject"]
# collection 작업
collection = database['PMC_FHP_data']
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
url = "https://www.ncbi.nlm.nih.gov/pmc/?term=forward+head+posture"
# 웹 페이지 열기
html_source = browser.get(url)
# collection.insert_one({"title": "UEG Week 2019 Poster Presentations","artical_date":"","abstract_list":""})


title_dict =  collection.find({}, { "_id": 0, "title": 1 })
title_list = []
for title_element in title_dict:
    title_list.append(title_element['title'])
filter = browser.find_element(by=By.CSS_SELECTOR,value='#EntrezSystem2\.PEntrez\.PMC\.Pmc_ResultsPanel\.Pmc_DisplayBar\.Display')
filter.click()
time.sleep(1)
items100 = browser.find_element(by=By.CSS_SELECTOR,value='#ps100')
items100.click()
page_number = browser.find_element(by=By.CSS_SELECTOR,value="#pageno")

##################
## 여기 수정해주기  ##
page_num = 195  ##
##################

page_number.send_keys(Keys.BACK_SPACE)
page_number.send_keys(page_num)
page_number.send_keys(Keys.ENTER)
time.sleep(3)
article_list = browser.find_elements(by=By.CSS_SELECTOR,value="#maincontent > div > div:nth-child(5) > div > div.rslt > div.title > a")

while True:
    for i in range(len(article_list)):
        article_list = browser.find_elements(by=By.CSS_SELECTOR,value="#maincontent > div > div:nth-child(5) > div > div.rslt > div.title > a")
        if article_list[i].text not in title_list:
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
            else:
                abstract = "not forward head posture"
                print("not forward head posture")
            print(page_num)
            if abstract == "" and article_date =="" and article_title == "":
                break
            else:
                collection.insert_one({"title": article_title,"artical_date":article_date,"abstract_list":abstract})
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