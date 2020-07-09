# -*- coding: UTF-8 -*-

import csv
import pymysql
import os.path

#from conectabd import *
#from testeconexao import  *


import time, threading

WAIT_SECONDS = 10

def sincroniza():
    print(time.ctime())
    conecta()
    threading.Timer(WAIT_SECONDS, sincroniza).start()



def conecta():
    #cursor_local = conecta_local()

    #cursor_remoto = conecta_remoto()

    f = open("teste1.csv",'r')

    csv_read = csv.DictReader(f, delimiter=",")
    for row in csv_read:
        print row

    #print select(cursor_local)

    #commit_local()
    print "Done"

conecta()
