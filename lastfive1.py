#!C:\Users\Romika Rani\AppData\Local\Programs\Python\Python311\python.exe
import pyautogui as acd
import sqlite3  
import cgi,cgitb
cgitb.enable()
print("Content-type:text/html \n")
print("<title>TRANSACTION DETAIL</title>")
conn=sqlite3.connect("bank.db")
c=conn.cursor()
form=cgi.FieldStorage()
account_no=form.getvalue("account_no")		
cd= '''SELECT * FROM trans WHERE account_no=? order by id desc limit 5'''
c.execute(cd,(account_no,))
x=c.fetchall()
print('''<style>body{background-image:url("images1.jpg");background-size:cover;background-repeat:no-repeat;}</style>''')
print("<p style='color:black;font-family:verdana;text-align:center;font-size:100%;'><u><b>")
print("DATE_OF_TRANS,DEPOSIT,WITHDRAW")
print("</b></u></p>")
xx=0
b1=0
for row in x:
	if len(x) != 0:
		if xx==0:
			b1=row[4]
			print("<p style='color:black;font-family:verdana;text-align:center;font-size:150%;'>")
			print(row[1])
			print("   ")
			print(row[2])
			print("   ")
			print(row[3])
			print("</p>")
			
			
		else:
			print("<p style='color:black;font-family:verdana;text-align:center;font-size:150%;'>")
			print(row[1])
			print("  ")
			print(row[2])
			print("  ")
			print(row[3])
			print("</p>")
					
	else:
		print("<p style='color:black;;font-family:verdana;text-align:center;font-size:150%;'><u>")
		print("NO RECORD")
		print("<br><center><input type='button' value='BACK' onclick='history.go(-2)'><center>")
		print("</u><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br></p>")
		
	xx=xx+1
	
print("<p style='color:black;font-family:verdana;text-align:center;font-size:200%;'><u>")	
print("Final Balance: ",b1)
print("</u></p>")
print("")
print("<br><center><input type='button' value='BACK' onclick='history.go(-2)'><center>")
conn.commit()
conn.close()