import mysql.connector as sqltor
 
mydb=sqltor.connect(host="localhost",user="vaishnav35",passwd="khaldrogo35")
my_c=mydb.cursor()
q="CREATE DATABASE phdata;"
r="USE phdata;"
s="CREATE TABLE phdata (platform varchar(15), username varchar(32), password varchar(32));"
my_c.execute(q)
my_c.execute(r)
my_c.execute(s)
mydb.commit()
mydb.close()
my_c.close()
 
 
import os
import sys
 
os.system("pip install django")
os.system("pip install requests")
exit()
 

