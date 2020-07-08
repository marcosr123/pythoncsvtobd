# -*- coding: UTF-8 -*-

import csv
import pymysql
import os.path

from conectabd import *
from testeconexao import  *
from querys import *


import time, threading

WAIT_SECONDS = 10

def sincroniza():
    print(time.ctime())
    conecta()
    threading.Timer(WAIT_SECONDS, sincroniza).start()



def conecta():
    cursor_local = conecta_local()

    cursor_remoto = conecta_remoto()

    csv_read = csv.reader(file("teste1.csv"))

    update(cursor_local,csv_read)
    commit_local()
    print "Done"

if url_ok():
    sincroniza()
else:
    print "Deu erro!"
