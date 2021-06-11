import jwt
from APIRestConPython.settings import SIMPLE_JWT
import requests
from bs4 import BeautifulSoup
import csv
import random
import mimetypes
from django.http import HttpResponse
import codecs
from openpyxl import Workbook

def get_data_from_header(auth_header):
    auth_header = auth_header.split('Bearer ')[1]
    res = jwt.decode(auth_header, SIMPLE_JWT['SIGNING_KEY'], algorithms=[SIMPLE_JWT['ALGORITHM']])
    return res

def get_html(url):
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text

def scrape_html(html):
    result = []
    soup = BeautifulSoup(html, "html.parser")
    for link in soup.find_all('a'):
        href = str(link.get('href')).strip()
        text = str(link.text).strip()
        if (len(href) > 0 or len(text) > 0):
            result.append([href, text])
    return result

def route(exported_list, file_type):
    if(file_type.upper() == 'XLSX'):
        return create_xlsx(exported_list)
    else:
        return create_csv(exported_list)

def create_csv(exported_list):
    file_name = f'exported_anchors_{random.randint(1, 100)}.csv'
    path = 'DownloadFiles/'+file_name
    with open(path, 'w', newline='', encoding="utf-8", errors='ignore') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for e in exported_list:
            writer.writerow(e)
    return file_name

def create_xlsx(exported_list):
    file_name = f'exported_anchors_{random.randint(1, 100)}.xlsx'
    path = 'DownloadFiles/'+file_name
    workbook = Workbook()
    sheet = workbook.active

    sheet["A1"] = "hello"
    sheet["B1"] = "world!"
    
    workbook.save(filename=path)
    return file_name

def download_file(fl_path):
    fl = open('DownloadFiles/'+fl_path, 'r')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type, charset='utf-8')
    response.write(codecs.BOM_UTF8)
    response['Content-Disposition'] = "attachment; filename=%s" % fl_path
    return response