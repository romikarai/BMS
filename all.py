#!C:\Users\Romika Rani\AppData\Local\Programs\Python\Python311\python.exe
import sqlite3  
import cgi,cgitb
cgitb.enable()
print("Content-type:text/html \n")
print("<title>ACCOUNT CREATED</title>")
conn=sqlite3.connect("bank.db")

form=cgi.FieldStorage()
#c.execute("CREATE TABLE login (user_id TEXT, password TEXT,Name TEXT,designation TEXT,mobile_no integer,type TEXT);")

user_id=form.getvalue("user_id")
password=form.getvalue("password")

Name=form.getvalue("Name")

designation = form.getvalue('dropdown')

mobile_no=form.getvalue("mobile_no")
type = form.getvalue('dropdown1')
data=(user_id,password,Name,designation,mobile_no,type)
c=conn.cursor()
insert_query='''INSERT INTO login VALUES (?,?,?,?,?,?)'''

c.execute(insert_query,data)
print('''<style>
body
{
background-image:url("images1.jpg");background-size:cover;background-repeat:no-repeat;}
</style>''')
print('<h1 style="font-size:200%;color:black;text-align:center;"><i><u>your account is created successfully</i><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br></h1>')
print("""<br><center><input type="button" value="Back" onclick="history.go(-2)" /></center>""")




conn.commit()
conn.close()