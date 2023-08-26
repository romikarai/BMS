#!C:\Users\Romika Rani\AppData\Local\Programs\Python\Python311\python.exe
import sqlite3  
import cgi,cgitb
cgitb.enable()
print("Content-type:text/html \n")
print("<title>PASSWORD RESET</title>")
conn=sqlite3.connect("bank.db")
c=conn.cursor()
form=cgi.FieldStorage()
user_id=form.getvalue("user_id")
new_password=form.getvalue("new_password")
repeat_password=form.getvalue("repeat_password")

if new_password==repeat_password:
	cd='''UPDATE login set password=? WHERE user_id=?'''
	c.execute(cd,(new_password,user_id))
	print('''<style>body{background-image:url("images1.jpg");background-size:cover;background-repeat:no-repeat;}</style>''')
	print('<p style="color:blue;font-family:verdana;text-align:center;font-size:200%;"><i><del>password reset succesfully</del></i></p>')
else:
	print('''<style>body{background-image:url("images1.jpg");background-size:cover;background-repeat:no-repeat;}</style>''')
	print('<p style="color:blue;font-family:verdana;text-align:center;font-size:200%;"><i><del>newpassword and repeatpassword is not same</del></i></p>')
	
print("<center><input type='button' value='Back' onclick='history.go(-3)'></center>")
conn.commit()
conn.close()