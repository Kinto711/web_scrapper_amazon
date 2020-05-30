import requests
from bs4 import BeautifulSoup
import smtplib
import time
import json

URL = 'https://www.amazon.com/Apple-MacBook-16-Inch-512GB-Storage/dp/B081FZV45H/ref=sr_1_1?dchild=1&keywords=macbook+pro+16+inch&qid=1588216533&sr=8-1'

headers = {
    "User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
    }

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id = 'productTitle').get_text()
    price = soup.find(id = "priceblock_ourprice").get_text()

    price = price.replace(',' , '')
    converted_price = float(price[1:])

    if converted_price > 2.100:
        with open(filename, 'w' ) as checker:
            json.dump('The price has dropped! Go check the website "https://www.amazon.com/Apple-MacBook-16-Inch-512GB-Storage/dp/B081FZV45H/ref=sr_1_1?dchild=1&keywords=macbook+pro+16+inch&qid=1588216533&sr=8-1" !. Here is the new price: ' + price, checker)
        

    print(title.strip())
    print(converted_price)

filename = 'checker.txt'




#def send_mail():
 #   server = smtplib.SMTP('smtp.gmail.com', 587)
#    server.ehlo()
 #   server.starttls()
  #  server.ehlo()
#
 #   server.login('email','password' )
#
 #   subject = 'Price fell down'
  ## 
 #   msg = f"Subject: {subject}\n\n{body}"

#    server.sendmail(
 #       'ed.email@gmail.com',
  #      'simo.email',
   #     msg
  #  )
   # print("Hey! Email has been sent!")





while(True):
    check_price()
    time.sleep(60)