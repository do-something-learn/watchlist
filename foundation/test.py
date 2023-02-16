import time
import requests
import logging
from fake_useragent import UserAgent
import hashlib
import time
import base64
import copy
#获取token
def get_token(args:list):
    
    timestamp=str(int(time.time()))
    newargs=copy.deepcopy(args)
    newargs.append(timestamp)
    value=hashlib.sha1(','.join(newargs).encode('utf-8')).hexdigest()
    # print(value)
    token=base64.b64encode((f'{value},{timestamp}').encode('utf-8')).decode('utf-8')
    # print(token)
    return token

def scrapy_method(url): 
    ua=UserAgent()
    response=requests.get(url=url,headers={'user-agent':ua.random})
    return response
 

LIMIT=10
OFFSET=0
id_list=[]
URL='https://spa6.scrape.center/api/movie/?limit={limit}&offset={offset}&token={token}'
args=['/api/movie']
#遍历页面获取id
for page in range(1,10):
   offset=LIMIT*(page-1)
   token=get_token(args)
   print(token)
   url=URL.format(limit=LIMIT,offset=offset,token=token)#获取列表页url
   response=scrapy_method(url)
 
   for item in response.json()['results']:
        
        id_list.append(item['id'])
    
   

# 遍历集合，获取id
for item in id_list:
    #根据id进行拼接字符串
    id_value='ef34#teuq0btua#(-57w1q5o5--j@98xygimlyfxs*-!i-0-mb'+str(item)
    #进行base64编码
    key=base64.b64encode(id_value.encode('utf-8')).decode('utf-8')
    #将编码后的值进行拼接，作为参数
    arg=[f'/api/movie/{key}']
    token=get_token(arg)
    URL_DETAIL='https://spa6.scrape.center/api/movie/{key}/?token={token}'
    url_detail=URL_DETAIL.format(key=key,token=token)
    response=scrapy_method(url_detail)
    print(response.json()['name'])
