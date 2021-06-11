import jwt
from APIRestConPython.settings import SIMPLE_JWT
import requests
from bs4 import BeautifulSoup
import csv
import random
import mimetypes
from django.http import HttpResponse
import codecs
import xlwt


def get_data_from_header(auth_header):
    #Get Auth token and return the payload
    auth_header = auth_header.split('Bearer ')[1]
    res = jwt.decode(auth_header, SIMPLE_JWT['SIGNING_KEY'], algorithms=[SIMPLE_JWT['ALGORITHM']])
    return res

def get_html(url):
    #Simple GET 
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text

def scrape_html(html):
    #Scrape HTML and extract values
    result = []
    soup = BeautifulSoup(html, "html.parser")
    for link in soup.find_all('a'):
        href = str(link.get('href')).strip()
        text = str(link.text).strip()
        if (len(href) > 0 or len(text) > 0):
            result.append([text, href])
    return result

def route(exported_list, file_type):
    #Route over CSV or XLSX
    if(file_type.upper() == 'XLSX'):
        fl_path = create_xlsx(exported_list)
        return download_xlsx(fl_path)
    else:
        fl_path = create_csv(exported_list)
        return download_csv(exported_list)

def create_csv(exported_list):
    #Write CSV file
    file_name = f'exported_anchors_{random.randint(1, 100)}.csv'
    path = 'DownloadFiles/'+file_name
    with open(path, 'w', newline='', encoding="utf-8", errors='ignore') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for e in exported_list:
            writer.writerow(e)
    return file_name

def create_xlsx(exported_list):
    #Write XLSX file
    index = 0
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet("sheet1")
    for i in exported_list:
        ws.write(index, 0, i[0])
        ws.write(index, 1, i[1])
        index += 1

    return wb

def download_csv(fl_path):
    #Download CSV file
    fl = open('DownloadFiles/'+fl_path, 'r')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type, charset='utf-8')
    response.write(codecs.BOM_UTF8)
    response['Content-Disposition'] = "attachment; filename=%s" % fl_path
    return response

def download_xlsx(wb):
    #Donwload XLSX file
    file_name = f'exported_anchors_{random.randint(1, 100)}.xlsx'
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename='+file_name
    wb.save(response)
    return response