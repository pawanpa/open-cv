import mysql.connector

mydb = mysql.connector.connect(host= 'localhost',user='root',password="")


cu = mydb.cursor()

cu.execute('create database cust')

mydb.commit()