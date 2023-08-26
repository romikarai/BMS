#!C:\Users\Romika Rani\AppData\Local\Programs\Python\Python311\python.exe
import sqlite3  
import cgi,cgitb
cgitb.enable()
print("Content-type:text/html \n")
conn=sqlite3.connect("bank.db")
print("<title>FORGOTTEN ACCOUNT</title>")
c=conn.cursor()
form=cgi.FieldStorage()
print("")

Name=form.getvalue("Name")
mobile_no=form.getvalue("mobile_no")
print('''<style>
body
{
background-image:url("images1.jpg");background-size:cover;background-repeat:no-repeat;}
</style>''')
cd= '''SELECT * FROM login WHERE Name=? AND mobile_no=?'''
c.execute(cd,(Name,mobile_no))
data=c.fetchall()
for row in data:
	print("<p style=text-align:center;font-size:300%;color:black;><i><ins>Forgotten Password</ins></i>")
	print( "<br><br><br>User_id=",row[0])
	print( "<br>Password=",row[1])
	print(" <br><br><br>  ")
	print("<br><br><br>   ")
	print("""<center><input type="button" value="Back" onclick="history.back(-1)" /></center>""")
	print("</p>")
	
if len(data) == 0:
	print('''<style>body{background-image:url("images1.jpg");background-size:cover;background-repeat:no-repeat;}</style>''')
	print("<p style=text-align:center;font-size:200%;color:black;><i><del>user password doesnot exist</del></i></p>")

conn.commit()
conn.close()


