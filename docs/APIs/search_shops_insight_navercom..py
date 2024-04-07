# 데이터명 : 조달청_나라장터 공공데이터개방표준서비스
# from https://developers.naver.com/docs/serviceapi/datalab/shopping/shopping.md#%EC%87%BC%ED%95%91%EC%9D%B8%EC%82%AC%EC%9D%B4%ED%8A%B8-%EB%B6%84%EC%95%BC%EB%B3%84-%ED%8A%B8%EB%A0%8C%EB%93%9C-%EC%A1%B0%ED%9A%8C
import requests 

# url 주소 변수 지정
url = 'https://openapi.naver.com/v1/datalab/shopping/categories'

header = {'X-Naver-Client-Id':'cRMNURzoedZxUwUyW0Hh',
           'X-Naver-Client-Secret':'87bY0YnCTe'
           }
bodys = {
    "startDate": "2017-08-01",
    "endDate": "2017-09-30",
    "timeUnit": "month",
    "category": [
        {"name": "패션의류", "param": [ "50000000"]},
        {"name": "화장품/미용", "param": [ "50000002"]}
        ],
        "device": "pc",
        "gender": "f",
        "ages": [ "20",  "30"]
}

pass
# respose라는 변수로 받음
response = requests.post(url,json=bodys, headers=header) 
pass
# response의 내용을 출력
print(response.content) 

# json 파일을 dictionary 형태로 변환
import json
contents = json.loads(response.content)
pass



# # mongoDB 저장
# from pymongo import MongoClient
# # mongodb에 접속 -> 자원에 대한 class
# mongoClient = MongoClient("mongodb://localhost:27017")
# # database 연결
# database = mongoClient["data_go_kr"]
# # collection 작업
# collection = database['search_shop_info']
# # insert 작업 진행
# collection.delete_many({})
# result = collection.insert_one({'lastBulidDate': contents['lastBuildDate'],
#                                 'total':contents['total'],
#                                 'start':contents['start'],
#                                 'display':contents['display']})
# pass
# for i in range(len(contents['items'])):
#     contents['items'][i]['id_relative'] = result.inserted_id
# pass
# collection = database['serach_shop_list']
# collection.delete_many({})
# collection.insert_many(contents['items'])