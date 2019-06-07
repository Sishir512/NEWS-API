""" When you run the API.py program you can se that you get unnecessary Author1234,Content1234 & Title1234 in the output.That problem is fixed by this code"""

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
open("e:/article_textnews.txt", "w").write(text_data)
article_textnews=open("e:/article_textnews.txt").read()
articles=final_data["articles"]
for article in articles:
    if article['title']:
        article_textnews=article_textnews.replace("Title1234",article["title"])
    if article["content"]:
        article_textnews=article_textnews.replace("Content1234",article["content"])
    if article["author"]:
        article_textnews=article_textnews.replace("Author1234","-"+article["author"])
    
    article_textnews+=text_data
article_textnews=article_textnews.replace("Title1234","")   
article_textnews=article_textnews.replace("Author1234","")  
article_textnews=article_textnews.replace("Content1234","")  
open("e:/FinalOutput.txt","w",encoding="utf-8").write(article_textnews)

