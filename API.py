import os
import requests
import json
from datetime import *
now=datetime.now()
todays_date=str(now.year)+"-"+str(now.month)+"-"+str(now.day)
parm = {"apiKey": "f585ca62acdb46e7b7decd0d245efe16"}
url="https://newsapi.org"
print("Type 'A' for top headlines")
print("Type 'B' if you want to search particular item")
typed=input("A or B? ::::  ")
global request_data_text
if typed=="A":
    sub_page="/v2/top-headlines?"
    parm["country"]="us"
else:
    what=input("Type what you want to search?:::: ")
    sub_page="/v2/everything?"
    parm["q"]=what
    parm["from"]=todays_date
request_data=requests.get(url+sub_page,params=parm)
request_data_text = request_data.text
final_data = json.loads(request_data_text)
print(final_data)
file_data=open("e:/NewsOutput.txt" , "w",encoding="utf-8")
file_data.write(request_data.text)
text_data=open("e:/text.txt").read()
article_textnews=text_data
articles=final_data["articles"]
for article in articles:
    
    if article["author"]:
        article_textnews.replace("Author1234",article["author"])
    if article['title']:
        article_textnews.replace("Title1234",article["title"])
    if article["content"]:
        article_textnews.replace("Content1234",article["content"])
    article_textnews+=text_data

open("e:/article_textnews.txt",'r')


