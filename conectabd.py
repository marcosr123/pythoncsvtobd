import pymysql

mydb_local = None
mydb_remote = None


def conecta_local():
    global mydb_local 
    mydb_local = pymysql.connect(host='192.168.4.94', port=3306, user='root', passwd='', db='test',cursorclass=pymysql.cursors.SSDictCursor)
    return mydb_local.cursor()

def conecta_remoto():
    global mydb_remote 
    mydb_remote = pymysql.connect(host='*******',port=3306,user='*******',passwd='*******',db='srtma06')
    return mydb_remote.cursor()

def commit_local():
    global mydb_local
    mydb_local.commit()

def commit_remoto():
    global mydb_remote
    mydb_remote.commit()
