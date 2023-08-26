#!C:\Users\Romika Rani\AppData\Local\Programs\Python\Python311\python.exe
import sqlite3  
import cgi,cgitb
cgitb.enable()
print("Content-type:text/html \n")
conn=sqlite3.connect("bank.db")
c=conn.cursor()
form=cgi.FieldStorage()
print("<title>INVALID PASSWORD</title>")
user_id=form.getfirst("user_id")
password=form.getfirst("password")

cd= '''SELECT * FROM login WHERE user_id=? AND password=?'''
c.execute(cd,(user_id,password,))
data=c.fetchall()
for row in data:
	print('''<head> <meta http-equiv="refresh" content="0;URL='mainpage.html'"/></head>''')	
#print("<p style=text-align:center;font-size:300%;color:blue;><b>WELCOME!!!\n\n </p>",row[2])


if len(data)==0:  
   	print("<p style=text-align:center;font-size:200%;color:blue;><del><i>Invalid User name and password</p>")

print("""<center><input type="button" value="Back" onclick="history.back(-1)" /></center>""")


conn.commit()
conn.close()