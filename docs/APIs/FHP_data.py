# 데이터명 : 조달청_나라장터 공공데이터개방표준서비스
# from https://www.data.go.kr/iim/api/selectAPIAcountView.do
import requests 
import xmltodict
# url 주소 변수 지정
# sickCd = ['M542','S134']
# medTp = 1,2
import time
from pymongo import MongoClient
for i in range(2021,2023):
    j= 2
    url = 'https://apis.data.go.kr/B551182/diseaseInfoService/getDissByGenderAgeStats?'
    params1 = {"serviceKey":"Qa6CXT4r6qEr%2BkQt%2FJx6wJr5MPx45hKNJwNTScoYryT2uGz7GozIqpjBw%2FRMk1uE8l92NU7h89m20sa%2FXHKuaQ%3D%3D",
            "pageNo":"1",
            "numOfRows":"18",
            "year":i,
            "sickCd":'S134',
            "sickType":2,
            "medTp":j
            }
    response = requests.get(url,params=params1)
    data_dict = xmltodict.parse(response.text)
    while True:
        try:
            if data_dict['response']['body']['items'] == None:
                break
            data_list = data_dict['response']['body']['items']['item']
            for m in range(len(data_list)):
                data_list[m]['year'] = i
                data_list[m]['medTp']=j
                # mongoDB 저장
            # mongodb에 접속 -> 자원에 대한 class
            mongoClient = MongoClient("mongodb://localhost:27017")
            # database 연결
            database = mongoClient["healthcare_sideproject"]
            # collection 작업
            collection = database['FHP_data']
            # insert 작업 진행
            result = collection.insert_many(data_list)
            break
        except:
            time.sleep(3)
            print('repeat')

    pass




# mongoDB 저장
# from pymongo import MongoClient
# # mongodb에 접속 -> 자원에 대한 class
# mongoClient = MongoClient("mongodb://localhost:27017")
# # database 연결
# database = mongoClient["data_go_kr"]
# # collection 작업
# collection = database['getDataSetOpnStdBidPblancInfo']
# # insert 작업 진행
# result = collection.insert_many(contents['response']['body']['items'])
