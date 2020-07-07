# -*- coding: UTF-8 -*-

import csv
import pymysql

try:
    mydb = pymysql.connect(host='192.168.4.94', #Conexão com BD
        port=3306,
        user='root',
        passwd='',
        db='test')
    cursor = mydb.cursor()

    csv_data = csv.reader(file('teste1.csv'))
    for row in csv_data:
    #Inserção dos dados no BD
        cursor.execute('INSERT INTO teste(descricao, status ) VALUES("%s", "%s")', row)

    mydb.commit()
    cursor.close()

except pymysql.err.OperationalError:
    print "Erro ao estabelecer conexão com o Banco de Dados, verifique os dados e tente novamente!"
except pymysql.err.InternalError:
    print "Banco de dados não existente!"
except IOError: 
    print "Arquivo de CSV não encontrado!"

