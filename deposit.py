#!C:\Users\Romika Rani\AppData\Local\Programs\Python\Python311\python.exe
print("Content-Type: text/html \n")
print("<html>")
print("<title>DEPOSITE</title>")
print('''<style>body{background-image:url("images1.jpg");background-attachment:fixed;background-position:center;background-size:cover;background-repeat:no-repeat;}</style>''')
print("""
<form method='post' action='deposit1.py'><br><br>
<p style="color:black;font-family:arial bold;text-align:center;font-size:200%;"><b><u>DEPOSIT YOUR AMOUNT</u></b></p>
<p style="color:black;font-family:arial bold;text-align:center;font-size:150%;">ACCOUNT_NO: <input type="text" name="account_no" required></p>
<p style="color:black;font-family:arial bold;text-align:center;font-size:150%;">DATE:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="date" name="date_of_trans" required></p>
<p style="color:black;font-family:arial bold;text-align:center;font-size:150%;">DEPOSIT:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="number" name="deposit" required></p><br><br>
<center><input type="submit" value="Submit"><button type="reset" value="Reset">Reset</button><input type='button' value='BACK' onclick='history.back(-1)'></center>
</form>
""")
print("</html>")