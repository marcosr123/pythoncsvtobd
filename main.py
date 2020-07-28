
import csv
import pymysql
import os.path
import conectabd as cnt
import testeconexao as tst
from querys import *


import time, threading

WAIT_SECONDS = 10

def sincroniza():
    print(time.ctime())
    conecta()
    threading.Timer(WAIT_SECONDS, sincroniza).start()



def conecta():
    cursor_local = cnt.conecta_local()

    cursor_remoto = cnt.conecta_remoto()

    f = open("teste1.csv",'r')

    csv_read = csv.DictReader(f, delimiter=",")
    for row in csv_read:
        print(row)

    

    cnt.commit_local()
    print("Done")

conecta()
