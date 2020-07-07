# -*- coding: UTF-8 -*-

import csv
import pymysql

#Usar Python2

mydb = pymysql.connect(host='192.168.4.94', #Conexão com BD
    port=3306,
    user='root',
    passwd='',
    db='test3')
cursor = mydb.cursor()

csv_data = csv.reader(file('teste1.csv')) #Abrir arquivo CSV
for row in csv_data:
    #Inserção dos dados no BD
    cursor.execute('INSERT INTO teste(descricao, status )'  
          'VALUES("%s", "%s")', 
          row)

#close the connection to the database.
mydb.commit()
cursor.close()
print "Done"