#To make this program run correctly add URL1234 in the text.txt file.
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
def type_function():
    global typed
    global sub_page
    print("A or B ?  ::::  ")
    typed=input()
    if typed.upper()=="A":
        sub_page="/v2/top-headlines?"
        parm["country"]="us"
        print_json()
    elif typed.upper()=="B":
        what=input("Type what you want to search?:::: ")
        sub_page="/v2/everything?"
        parm["q"]=what
        parm["from"]=todays_date
        print_json()
    else:
        print("You were asked to type A or B you idiot . Not other characters")
        type_function()
    
def print_json():#Prints json data
    global request_data_text
    global final_data
    request_data=requests.get(url+sub_page , params=parm)
    request_data_text = request_data.text
    final_data = json.loads(request_data_text)
    print(final_data)
def open_file(): #To create a text file(NewsOutput.txt) and write the json data in the file.
    global text_data
    file_data=open("e:/NewsOutput.txt" , "w",encoding="utf-8")
    file_data.write(request_data_text)
    text_data=open("e:/text.txt").read()
    open("e:/article_textnews.txt", "w").write(text_data) #To create a text file (article_textnews.txt).In this file we store the contents of text.txt file so that not to change the contents of text.txt file and by doing so we can run the program again and again.
def replacing():
    global article_textnews
    article_textnews=open("e:/article_textnews.txt").read()
    articles=final_data["articles"]
    for article in articles: #To replace the Title1234 , Content1234 , URL1234 & Author 1234 in the article_textnews.txt file by Title , Content , URL & Author respectively.
        if article["title"]:
            article_textnews=article_textnews.replace("Title1234","Title:::: "+article["title"])
        if article["content"]:
            article_textnews=article_textnews.replace("Content1234",article["content"])
        if article["url"]:
            article_textnews=article_textnews.replace("URL1234","For complete news go to this link::: \n"+article["url"]+"\n")
        if article["author"]:
            article_textnews=article_textnews.replace("Author1234","Article By::: "+article["author"]+"\n")
        article_textnews+=text_data
        
    article_textnews=article_textnews.replace("Title1234","")   
    article_textnews=article_textnews.replace("Author1234","")  
    article_textnews=article_textnews.replace("Content1234","") 
    article_textnews=article_textnews.replace("URL1234","")   
    open("e:/FinalOutput.txt","w",encoding="utf-8").write(article_textnews)

type_function()
print_json()
open_file()
replacing()
