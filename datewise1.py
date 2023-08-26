#!C:\Users\Romika Rani\AppData\Local\Programs\Python\Python311\python.exe
import pyautogui as acd
import datetime
import sqlite3  
import cgi,cgitb
cgitb.enable()
print("Content-type:text/html \n")
print("<title>TRANSACTION DETAIL</title>")
conn=sqlite3.connect("bank.db")
c=conn.cursor()
form=cgi.FieldStorage()
account_no=form.getvalue("account_no")
from1=form.getvalue("from_date")

to1=form.getvalue("to_date")
fr1=datetime.datetime.strptime(from1,'%Y-%m-%d').date()
t1=datetime.datetime.strptime(to1,'%Y-%m-%d').date()

cd= '''SELECT * FROM trans WHERE account_no=? AND date_of_tans BETWEEN ? AND ?'''
c.execute(cd,(account_no,fr1,t1))
x=c.fetchall()
cd1= '''SELECT * FROM trans WHERE account_no=? order by id desc'''
c.execute(cd1,(account_no,))
x1=c.fetchall()
xx=0
for r in x1:
	if xx==0:
		bal=r[4]
		break
print('''
<style>
body{
background-image:url("images1.jpg");background-attachment:fixed;background-position:center;background-size:cover;background-repeat:no-repeat;
}
</style>''')
print("<p style='color:black;font-family:verdana;text-align:center;font-size:100%;'><u><b>")
print("DATE_OF_TRANS,DEPOSIT,WITHDRAW")
print("</b></u></p>")
for row in x:
	if (len(x)) != 0:
		print("<p style='color:black;font-family:verdana;text-align:center;font-size:200%;'>")
		print(row[1])
		print("")
		print(row[2])
		print("")
		print(row[3])
		print("")
		print("</p>")

	else:
		print('''<style>body{background-image:url("images1.jpg");background-attachment:fixed;background-position:center;background-size:cover;background-repeat:no-repeat;}</style>''')
		print("<p style='color:blue;font-family:verdana;text-align:center;font-size:100%;'><u>")
		print("NO RECORD")
		print("</u><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br></p>")
		print("<br><center><input type='button' value='BACK' onclick='history.go(-2)'></center>")	
	
print("<p style='color:black;font-family:verdana;text-align:center;font-size:200%;'><u>")		
print("Final Balance: ",bal)
print("</u></p>")
print("<br><center><input type='button' value='BACK' onclick='history.go(-2)'></center>")		
conn.commit()
conn.close()