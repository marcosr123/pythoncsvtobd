# -*- coding: UTF-8 -*-

import requests
import os.path

url = "http://192.168.4.94:8080/phpmyadmin/"

def url_ok():
    global url
    r = requests.head(url)
    return True if r.status_code is 200 or 301 else "Conexão não estabelecida!" 

def checa_arquivo():
   return os.path.isfile('/arquivo.csv')


print url_ok()