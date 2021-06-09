import jwt
from APIRestConPython.settings import SIMPLE_JWT
import requests
from bs4 import BeautifulSoup

def get_data_from_header(auth_header):
    auth_header = auth_header.split('Bearer ')[1]
    res = jwt.decode(auth_header, SIMPLE_JWT['SIGNING_KEY'], algorithms=[SIMPLE_JWT['ALGORITHM']])
    # print(res)
    return res

def get_html(url):
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text

def scrape_html(html):
    soup = BeautifulSoup(html)
    for link in soup.find_all('a'):
        print(link.get('href'), link.text) 

