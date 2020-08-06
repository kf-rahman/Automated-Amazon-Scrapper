import requests
from bs4 import BeautifulSoup
import smtplib

URL='https://www.amazon.ca/Paring-Knife-Stainless-Comfortable-Ergonomic/dp/B07W7TJCQX/ref=sr_1_2_sspa?keywords=pairing+knife&qid=1590113642&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyNkhPUVpIRUsxR1VXJmVuY3J5cHRlZElkPUEwNDE4MjQxWDFCOUs1RzAyUjFEJmVuY3J5cHRlZEFkSWQ9QTAyMDUzMDJCS0w0UVdaRDg4SUEmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl'
headers={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}


def check_price():
    page= requests.get(URL,headers=headers)
    soup= BeautifulSoup(page.content,'html.parser')
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[4:8])
    if(converted_price<50):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('kazrocks.bd@gmail.com','dpgzvlkdharnvray')
    subject = 'DROP IN PRICE!'
    body= 'Check the link: https://www.amazon.ca/Paring-Knife-Stainless-Comfortable-Ergonomic/dp/B07W7TJCQX/ref=sr_1_2_sspa?keywords=pairing+knife&qid=1590113642&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyNkhPUVpIRUsxR1VXJmVuY3J5cHRlZElkPUEwNDE4MjQxWDFCOUs1RzAyUjFEJmVuY3J5cHRlZEFkSWQ9QTAyMDUzMDJCS0w0UVdaRDg4SUEmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl'
    msg =f"Subject: {subject}\n\n {body}"
    server.sendmail('kazrocks.bd@gmail.com','kazi.zayeed@gmail.com',msg)
    print('Email has been sent')
    server.quit()



check_price()