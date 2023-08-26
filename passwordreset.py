#!C:\Users\Romika Rani\AppData\Local\Programs\Python\Python311\python.exe
print("Content-Type: text/html \n")
print("<html>")
print("<title>PASSWORD RESET</title>")
print('''<style>body{background-image:url("images1.jpg");background-attachment:fixed;background-position:center;background-size:cover;background-repeat:no-repeat;}</style>''')
print("""
<form  method='post' action='passwordreset1.py'><br><br>
<p style="color:black;font-family:arial bold;text-align:center;font-size:200%;"><b><u>RESET YOUR PASSWORD</u></b></center></p>
<p style="color:black;font-family:arial bold;text-align:center;font-size:150%;">user_id: <input type="text" name="user_id"></p>
<center><input type="submit" value="Submit"></center>
</form>
""")
print("</html>")