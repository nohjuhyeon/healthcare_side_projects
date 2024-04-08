# 데이터명 : 조달청_나라장터 공공데이터개방표준서비스
# from https://www.data.go.kr/iim/api/selectAPIAcountView.do
import requests 
import xmltodict
# url 주소 변수 지정

# for i in range(2012,2023):
#     for j in range(1,3):
#         for k in ['M542','S134']:
#             url = 'https://apis.data.go.kr/B551182/diseaseInfoService/getDissByGenderAgeStats?'
#             params1 = {"serviceKey":"ow0djIIbtYKcXjahX81pjlVfuA8kUj6DBQkALWCEeCXNuir3R0%2BLMOTTuhmW9Ms7R%2FAVfqb7cGIAazhHFttnPw%3D%3D",
#                     "pageNo":"1",
#                     "numOfRows":"10",
#                     "year":i,
#                     "sickCd":k,
#                     "sickType":2,
#                     "medTp":j
#                     }
# url = 'https://apis.data.go.kr/B551182/diseaseInfoService/getDissByGenderAgeStats?'
# params1 = {"serviceKey":"ow0djIIbtYKcXjahX81pjlVfuA8kUj6DBQkALWCEeCXNuir3R0%2BLMOTTuhmW9Ms7R%2FAVfqb7cGIAazhHFttnPw%3D%3D",
#         "pageNo":"1",
#         "numOfRows":"1",
#         "year":'2021',
#         "sickCd":'M542',
#         "sickType":'2',
#         "medTp":'1'
#         }
url = 'https://apis.data.go.kr/B551182/diseaseInfoService/getDissByGenderAgeStats?serviceKey=Ix7Xj2a52fUYj6pPXF5TMooSl/dFBu/Y6/oyu8NyrmGGcfaMKwy99HEdnaPF5AAzDB0UBHEjkRjWrvJN7M5lPg==&numOfRows=10&pageNo=1&year=2022&sickCd=A00&sickType=1&medTp=1'
response = requests.get(url)
data_dict = xmltodict.parse(response.text)
print(data_dict) 




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
