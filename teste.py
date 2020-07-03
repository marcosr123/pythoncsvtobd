import csv
import pymysql

mydb = pymysql.connect(host='192.168.4.94',
    port=3306,
    user='root',
    passwd='',
    db='test')
cursor = mydb.cursor()

csv_data = csv.reader(file('teste.csv'))
for row in csv_data:

    cursor.execute('INSERT INTO teste(descricao, status )' \
          'VALUES("%s", "%s")', 
          row)
#close the connection to the database.
mydb.commit()
cursor.close()
print "Done"