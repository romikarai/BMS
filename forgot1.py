#!C:\Users\Romika Rani\AppData\Local\Programs\Python\Python311\python.exe
print("Content-Type: text/html \n")
print("<html>")
print("<title>FORGOTTEN ACCOUNT</title>")
print('''<style>
body
{
background-image:url("images1.jpg");background-size:cover;background-repeat:no-repeat;}
</style>''')
print("""
<form style=" width:1000px;height:600px;" method='post' action='Forgot.py'>
<table>
	<tr>
<p style="color:blue;font-family:arial bold;font-size:300%;text-align:center;"><i><ins>Forgotten Account</ins></i></p></tr>

<tr>

<p style="color:black;font-family:arial bold;text-align:center;font-size:150%;">Name:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="text" name="Name"></p></tr>
<tr>

<p style="color:black;font-family:arial bold;text-align:center;font-size:150%;">Mobile_no: <input type="tel" name="mobile_no" pattern="^\d{10}$"></p></tr>
<tr>


<p style="color:black;font-family:arial bold;text-align:center;">
<input type="submit" value="login">
<button type="reset" value="Reset">Reset</button>
<input type="button" value="Back" onclick="history.back(-1)" /></p></tr>
</table>
</form>
""")
print("</html>")