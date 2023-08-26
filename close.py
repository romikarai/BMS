#!C:\Users\Romika Rani\AppData\Local\Programs\Python\Python311\python.exe
print("Content-Type: text/html \n")
print("<html>")
print("<title>UPDATE STATUS</title>")
print('''<style>
body
{
background-image:url("images1.jpg");background-attachment:fixed;background-position:center;background-size:cover;background-repeat:no-repeat;}
</style>''')
print("""
<form  method='post' action='close1.py'>

<p style="color:black;font-family:arial bold;text-align:center;font-size:200%;"><b><u>UPDATE ACCOUNT STATUS</u></b></p>

<p style="color:black;font-family:arial bold;text-align:center;font-size:150%;">ACCOUNT_NO: <input type="text" name="account_no" required></p>

<p style="color:black;font-family:arial bold;text-align:center;font-size:150%;">NAME:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <input type="text" name="Name" required></p>

<p style="color:black;font-family:arial bold;text-align:center;font-size:150%;">STATUS:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<select name="dropdown1"><option value="OPERATED" selected>OPERATED</option><option value="NONOPRATED">NONOPRATED</option><option value="CLOSE">CLOSE</option></select><br><br>
<input type="submit" value="Submit"><input type='button' value='Cancel' onclick='history.back(-1)'>
</form>
""")
print("</html>")