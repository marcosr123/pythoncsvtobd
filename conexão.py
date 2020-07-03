import pymysql

mydb = pymysql.connect(host='192.168.4.94',
    port=8080,
    user='root',
    passwd='',
    db='test')
cursor = mydb.cursor()
