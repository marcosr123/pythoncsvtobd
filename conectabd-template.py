import pymysql

mydb_local = None
mydb_remote = None


def conecta_local():
    global mydb_local 
    mydb_local = pymysql.connect(host='yourlocal', port=3306, user='youruser', passwd='', db='yourdb',cursorclass=pymysql.cursors.SSDictCursor)
    return mydb_local.cursor()

def conecta_remoto():
    global mydb_remote 
    mydb_remote = pymysql.connect(host='yourremote',port=3306,user='youruser',passwd='yourpass',db='yourdb')
    return mydb_remote.cursor()

def commit_local():
    global mydb_local
    mydb_local.commit()

def commit_remoto():
    global mydb_remote
    mydb_remote.commit()
