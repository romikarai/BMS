#!C:\Users\Romika Rani\AppData\Local\Programs\Python\Python311\python.exe
import pyautogui as acd
import sqlite3  
import cgi,cgitb
cgitb.enable()
print("Content-type:text/html \n")
print("<title>DEPOSITED</title>")
conn=sqlite3.connect("bank.db")
c=conn.cursor()
form=cgi.FieldStorage()
account_no=form.getvalue("account_no")
print(type(account_no))
date_of_tans=form.getvalue("date_of_trans")
depo=form.getvalue("deposit","0")
		
def deposite(depo):
	bal = 0	
	cd= '''SELECT * FROM trans WHERE account_no=? order by id desc'''
	c.execute(cd,(account_no,))
	x=c.fetchall()
	withd=0
	if len(x)==0:
		n1=int(depo)
		l=1
		bal = bal + n1
		data1=(account_no,date_of_tans,depo,withd,bal,l)
		insert_query='''INSERT INTO trans VALUES (?,?,?,?,?,?)'''
		c.execute(insert_query,data1)
		print('''<style>body{background-image:url("images1.jpg");background-size:cover;background-repeat:no-repeat;}</style>''')
		print("<p style='color:black;font-family:verdana;text-align:center;font-size:200%;'><u>")
		print("BALANCE",bal)
		print("<br><center><input type='button' value='BACK' onclick='history.go(-2)'></center>")
		print("</u><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br></p>")
	else:
			for row in x:
				l=row[5]
				l=l+1;
				b=(row[4])
				b=b+int(depo)
				cd1='''insert into trans values (?,?,?,?,?,?)'''
				data1=(account_no,date_of_tans,depo,withd,b,l) 
				c.execute(cd1,(data1))
				print('''<style>body{background-image:url("images1.jpg");background-size:cover;background-repeat:no-repeat;}</style>''')
				print("<p style='color:black;font-family:verdana;text-align:center;font-size:200%;'><u>")
				print("BALANCE:",b)
				print("<br><center><input type='button' value='BACK' onclick='history.go(-2)'></center>")
				print("</u><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br></p>")
				x=0
				if x==0:
					break
	
		
			

deposite(depo);
conn.commit()
conn.close()