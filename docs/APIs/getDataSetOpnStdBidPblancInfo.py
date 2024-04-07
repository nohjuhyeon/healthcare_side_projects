# 데이터명 : 조달청_나라장터 공공데이터개방표준서비스
# from https://www.data.go.kr/iim/api/selectAPIAcountView.do
import requests 

# url 주소 변수 지정
url = 'http://apis.data.go.kr/1230000/PubDataOpnStdService/getDataSetOpnStdBidPblancInfo?serviceKey=ow0djIIbtYKcXjahX81pjlVfuA8kUj6DBQkALWCEeCXNuir3R0%2BLMOTTuhmW9Ms7R%2FAVfqb7cGIAazhHFttnPw==&pageNo=1&numOfRows=10&type=json&bidNtceBgnDt=201712010000&bidNtceEndDt=201712312359'

pass
# respose라는 변수로 받음
response = requests.get(url) 
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
collection = database['getDataSetOpnStdBidPblancInfo']
# insert 작업 진행
result = collection.insert_many(contents['response']['body']['items'])
