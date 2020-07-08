import pymysql
from pymysql.cursors import DictCursor

mydb_local = None
mydb_remote = None


def conecta_local():
    global mydb_local 
    mydb_local = pymysql.connect(host='192.168.4.94', port=3306, user='root', passwd='', db='test',cursorclass=DictCursor)
    return mydb_local.cursor()

def conecta_remoto():
    global mydb_remote 
    mydb_remote = pymysql.connect(host='mysql.srtma.net',port=3306,user='srtma06',passwd='SEAPTESTE20',db='srtma06')
    return mydb_remote.cursor()

def commit_local():
    global mydb_local
    mydb_local.commit()

def commit_remoto():
    global mydb_remote
    mydb_remote.commit()
