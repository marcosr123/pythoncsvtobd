import pymysql
import csv


def insert(cursor,arq):
    for row in arq:
        cursor.execute('INSERT INTO teste(descricao,status) VALUES("%s","%s")',row)
    cursor.close()

def update(cursor,arq):
    for row in arq:
        cursor.execute('UPDATE teste SET descricao="%s",status="%s"',row)
    cursor.close()

        