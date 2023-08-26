#!C:\Users\Romika Rani\AppData\Local\Programs\Python\Python311\python.exe
print("Content-Type: text/html \n")
print("<html>")
print("<title>TRANSACTION DETAIL</title>")
print('''<style>body{background-image:url("images1.jpg");background-attachment:fixed;background-position:center;background-size:cover;background-repeat:no-repeat;}</style>''')
print("""
<form  method='post' action='lastfive1.py'><br><br>
<p style="color:black;font-family:arial bold;text-align:center;font-size:200%;"><b><u>LAST FIVE TRANSACTION</u></b></p>
<p style="color:black;font-family:arial bold;text-align:center;font-size:150%;">ACCOUNT_NO: <input type="text" name="account_no" required></p>
<center><input type="submit" value="Submit"><button type="reset" value="Reset">Reset</button><input type='button' value='BACK' onclick='history.back(-1)'></center>
</form>
""")
print("</html>")