#!C:\Users\Romika Rani\AppData\Local\Programs\Python\Python311\python.exe
print("Content-Type: text/html \n")
print("<html>")

print("<title>SIGN_UP</title>")
print('''<style>
body
{
background-image:url("images1.jpg");background-size:cover;background-repeat:no-repeat;}
</style>''')
print("""

<form style="font-family:verdana;width:1000px;height:600px;" method='post' action='all.py'>
<table>


         <tr>
		 

<p style="color:blue;font-family:verdana;font-size:300%;text-align:center;"><i><ins>Fill your Info</ins></i></p>


</tr>

<tr>
		

<p style="color:black;font-family:arial bold;text-align:center;font-size:150%;">user_id:<span style="color:red">&#42;</span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <input type="text" name="user_id" required></p></tr>

<tr>
		

<p style="color:black;font-family:arial bold;text-align:center;font-size:150%;">password:<span style="color:red">&#42;</span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <input type="password" name="password" placeholder="ex: 123ABCab" pattern="^(?=.*[A-Za-z])(?=.*\d)[A-za-z\d]{8,}$" required></p></tr>

<tr>
		

<p style="color:black;font-family:arial bold;text-align:center;font-size:150%;">Name:<span style="color:red">&#42;</span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <input type="text" name="Name" required></p></tr>
<tr>
		

<p style="color:black;font-family:arial bold;text-align:center;font-size:150%;">Designation:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<select name="dropdown"><option value="adminstrator" selected>adminstrator</option><option value="PO">PO</option><option value="cashier">cashier</option><option value="clerk">clerk</option></select></p></tr>
<tr>
		

<p style="color:black;font-family:arial bold;text-align:center;font-size:150%;">Mobile_No:<span style="color:red">&#42;</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="tel" name="mobile_no" pattern="^\d{10}$" required></p></tr>
<tr>
		

<p style="color:black;font-family:arial bold;text-align:center;font-size:150%;">Type:&nbsp; &nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <select name="dropdown1"><option value="admin" selected>admin</option><option value="user">user</option></select></p></tr>



<tr>
		

<p style="color:black;font-family:arial bold;text-align:center;font-size:150%;"><input type="submit" value="Submit">&nbsp;&nbsp;<button type="reset" value="Reset">Reset</button>&nbsp;&nbsp;<input type="button" value="Back" onclick="history.back(-1)"></p></tr>

</table>


</form>

""")
print("</html>")