#!C:\Users\Romika Rani\AppData\Local\Programs\Python\Python311\python.exe
import pyautogui as acd
import sqlite3  
import cgi,cgitb
cgitb.enable()
print("Content-type:text/html \n")
print("<title>STATUS UPDATED</title>")
conn=sqlite3.connect("bank.db")
c=conn.cursor()
form=cgi.FieldStorage()
account_no=form.getvalue("account_no")
Name=form.getvalue("Name")
status=form.getvalue("dropdown1")
cd= '''SELECT * FROM account WHERE account_no=? AND Name=?'''
c.execute(cd,(account_no,Name))
cd='''UPDATE account set status=? WHERE account_no=?'''
c.execute(cd,(status,account_no))
print('''<style>body{background-image:url("images1.jpg");background-size:cover;background-repeat:no-repeat;}</style>''')	
print("<center><u>ACCOUNT STATUS UPDATED SUCCESSFULLY</u></center>")
print("<br><br><center><input type='button' value='Back' onclick='history.go(-2)'></center>")
conn.commit()
conn.close()









