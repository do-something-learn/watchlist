import time
import requests
import logging

# times=int(time.time())#获取时间戳
# import hashlib
# value=hashlib.sha1("/api/movie,{times}".encode('utf-8')).hexdigest()
# print(value)
# import base64
# bsvalue=base64.b64encode((value+',{times}').encode('utf-8')).decode('utf-8')
# print(bsvalue)
# url=f'https://spa6.scrape.center/api/movie/?limit=10&offset=0&token={bsvalue}'
# print(url)
# response=requests.get(url=url)
# print(response.json(),response.text)

# times=int(time.time())#获取时间戳
import hashlib
value=hashlib.sha1("/api/movie,{times}".encode('utf-8')).hexdigest()
print(value)
import base64
bsvalue=base64.b64encode((value+',{times}').encode('utf-8')).decode('utf-8')
print(bsvalue)
