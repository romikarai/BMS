#!C:\Users\Romika Rani\AppData\Local\Programs\Python\Python311\python.exe
print("Content-Type: text/html \n")
print("<html>")
print("<title>LOGIN PAGE</title>")
print('''<style>
body
{
background-image:url("index.jpg");background-size:cover;background-repeat:no-repeat;}
</style>''')
print("""
<table width="100%" height="100%">
         <tr>
            <td>
            <p style="color:black;font-family:courier;font-size:50px;text-align:center"><b><u>BANK MANAGEMENT SYSTEM</u></b></p>
               	   
            </td>
          
         </tr>
	    <td>
		<center>
		<br>
		<h1 style="font-size:150%;color:blue"><u><b>Login To Your Account</b></u></h1>
		<form style="font-family:verdana;" method='post' action='login1.py'>
		<p style="color:black;font-family:arial bold;font-size:150%;">user_id:<span style="color:red">&#42;</span>&nbsp;&nbsp; <input type="text" name="user_id" required></p>
		<p style="color:black;font-family:arial bold;font-size:150%;">password:<span style="color:red">&#42;</span><input type="password" name="password" placeholder="ex: 123ABCab" pattern="^(?=.*[A-Za-z])(?=.*\d)[A-za-z\d]{8,}$" required></p>
		<b><input type="submit" value="login">
		<button type="reset" value="Reset">Reset</button>
		<p><a href="all1.py">Sign_up</a></p>
		<p><a href="Forgot1.py">Forgot_account</a></p>
		</center>
	     </td>
	</tr>
         
      </table>
</form>

""")
print("</html>")