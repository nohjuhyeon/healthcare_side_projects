# 데이터명 : 네이버 쇼핑
# from https://developers.naver.com/docs/serviceapi/search/shopping/shopping.md#%EC%87%BC%ED%95%91
import requests 

# url 주소 변수 지정
url = 'https://openapi.naver.com/v1/search/shop'

param1 = {'query': '소고기'}
header1 = {'X-Naver-Client-Id':'cRMNURzoedZxUwUyW0Hh',
           'X-Naver-Client-Secret':'87bY0YnCTe'}

pass
# respose라는 변수로 받음
response = requests.get(url,params = param1, headers=header1) 
pass
# response의 내용을 출력
print(response.content) 

# json 파일을 dictionary 형태로 변환
import json
contents = json.loads(response.content)
pass

# mongoDB 저장
from pymongo import MongoClient
# mongodb에 접속 -> 자원에 대한 class
mongoClient = MongoClient("mongodb://localhost:27017")
# database 연결
database = mongoClient["data_go_kr"]
# collection 작업
collection = database['search_shop_info']
# insert 작업 진행
collection.delete_many({})
result = collection.insert_one({'lastBulidDate': contents['lastBuildDate'],
                                'total':contents['total'],
                                'start':contents['start'],
                                'display':contents['display']})
pass
for i in range(len(contents['items'])):
    contents['items'][i]['id_relative'] = result.inserted_id            # 내가 insert한 값을 변수로 지정해놓으면 내가 insert한 값의 id를 가져올 수 있음
pass
collection = database['serach_shop_list']
collection.delete_many({})
results =collection.insert_many(contents['items'])
pass