import requests
from bs4 import BeautifulSoup
import json

URL="https://books.toscrape.com/"
# git config --global user.name "kishor chalise"
# git config --global user.email "kishorchalise01@gamil.com"

# git init
# git status => if you want to check what are the status of files
# git diff => if you want to check what are the changes
# git add .
# git commit -m "Your message"
# copy paste git code from github

# new project 
# git add .
# git commit -m 'messgae'
# git push


def scrape_books():
    response=requests.get(URL)
    if response.status_code !=200:
        return
    response.encoding= response.apparent_encoding 
    
    soup=BeautifulSoup(response.text,"html.parser")
    books=soup.find_all("article",class_="product_pod")
    data=[]
    for book in books:
       title= book.h3.a['title']
       price_text=book.find("p",class_="price_color").text
       currency=price_text[0]
       price=price_text[1:]
       data.append(
          {
              "title":title,
              "price":price,
              "currency":currency,
          }
      )

    with open('data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

    
    
scrape_books()