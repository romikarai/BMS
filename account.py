#!C:\Users\Romika Rani\AppData\Local\Programs\Python\Python311\python.exe
import sqlite3  
import cgi,cgitb
import random
cgitb.enable()
print("Content-type:text/html \n")
print("<title>ACCOUNT CREATED</title>")
conn=sqlite3.connect("bank.db")
c=conn.cursor()
form=cgi.FieldStorage()
c.execute("CREATE TABLE account (branch_code TEXT,account_no TEXT,type_of_account TEXT, status TEXT,Name TEXT,f_name TEXT,n_name TEXT,relationsip TEXT, address TEXT,aadhar_no INTEGER,pan_no INTEGER, mobile_no INTEGER,email TEXT);")
account_no=random.randint(1000000000,10000000000)
branch_code=form.getvalue("dropdown")
type_of_account="Saving"
status=form.getvalue("dropdown1")
Name=form.getvalue("Name")
f_name=form.getvalue("f_name")
n_name=form.getvalue("n_name")
relationship=form.getvalue("relationship")
address=form.getvalue("address")
aadhar_no=form.getvalue("aadhar_no")
pan_no=form.getvalue("pan_no")
mobile_no=form.getvalue("mobile_no")
email=form.getvalue("email")



data=(branch_code,account_no,type_of_account,status, Name, f_name, n_name,relationship, address,aadhar_no,pan_no, mobile_no, email)
insert_query='''INSERT INTO account VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)'''
c.execute(insert_query,data)



print('''<style>body{background-image:url("images1.jpg");background-size:cover;background-repeat:no-repeat;}</style>''')
print('<h1 style="font-size:200%;color:black;text-align:center;height:550px"><u><i>your account is created successfully</i><br><br>')
print("ACCOUNT_NO:",account_no)
print("</u></h1>")
print("""<br><center><input type="button" value="Back" onclick="history.go(-2)" /></center>""")





conn.commit()
conn.close()