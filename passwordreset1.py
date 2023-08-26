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
print('''<style>body{background-image:url("images1.jpg");background-attachment:fixed;background-position:center;background-size:cover;background-repeat:no-repeat;}</style>''')
cd= '''SELECT * FROM login WHERE user_id=?'''
c.execute(cd,(user_id,))
data=c.fetchall()
for row in data:
	print("""
	<form method='post' action='passwordreset2.py'><center>
	<p style="color:black;font-family:arial bold;text-align:center;font-size:150%;">User_id:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="text" name="user_id"></p>
	<p style="color:black;font-family:arial bold;text-align:center;font-size:150%;">new_pasword:&nbsp;&nbsp;&nbsp;&nbsp;<input type="password" name="password" placeholder="ex: 123ABCab" pattern="^(?=.*[A-Za-z])(?=.*\d)[A-za-z\d]{8,}$" required></p>
	<p style="color:black;font-family:arial bold;text-align:center;font-size:150%;">repeat_password:<input type="password" name="password" placeholder="ex: 123ABCab" pattern="^(?=.*[A-Za-z])(?=.*\d)[A-za-z\d]{8,}$" required></p>
	<input type="submit" value="ok">
	<button type="reset" value="Reset">Reset</button></center>
	</form>

	""")	
if len(data)==0: 
	print('''<style>body{background-image:url("images1.jpg");background-attachment:fixed;background-position:center;background-size:cover;background-repeat:no-repeat;}</style>''')
	print('<p style="color:blue;font-family:verdana;text-align:center;font-size:200%;"><i><del>Invalid User name and password</del></i></p>')
	print("""<input type='button' value='Back' onclick='history.back(-1)'>""")	

conn.commit()
conn.close()