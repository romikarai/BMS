#!C:\Users\Romika Rani\AppData\Local\Programs\Python\Python311\python.exe
print("Content-Type: text/html \n")
print("<html>")
print("<title>CREATE ACCOUNT</title>")
print('''<style>
body
{
background-image:url("images1.jpg");background-attachment:fixed;background-position:center;background-size:cover;background-repeat:no-repeat;}
</style>''')
print("""

<form style="font-family:verdana;" method='post' action='account.py'>
<table>
         <tr>
        
            <p style="color:black;font-family:courier;font-size:50px;text-align:center;margin-top:0;"><b><u>BANK MANAGEMENT SYSTEM</u></b><br></p>
            	   
            </tr>
          
	

         <tr>
		 

<p style="color:blue;font-family:verdana;font-size:250%;text-align:center;"><i><ins>ACCOUNT OPENING FORM</ins></i></p>


</tr>

<tr>
		

<p style="color:black;font-family:arial bold;text-align:center;font-size:150%;">Branch_Code:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<select name="dropdown"><option value="BANK001" selected>BANK001</option><option value="BANK002">BANK002</option><option value="BANK003">BANK003</option><option value="BANK004">BANK004</option></select></p></tr>


<tr>
		

<p style="color:black;font-family:arial bold;text-align:center;font-size:150%;">Type_of_Account:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="text" name="type_of_account" value="Saving" required></p></tr>
<tr>
		

<p style="color:black;font-family:arial bold;text-align:center;font-size:150%;">Status:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<select name="dropdown1"><option value="OPEN" selected>OPEN</option><option value="CLOSE">CLOSE</option></select></p></tr>
<tr>
		

<p style="color:black;font-family:arial bold;text-align:center;font-size:150%;">Name:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="text" name="Name"></p></tr>
<tr>
		

<p style="color:black;font-family:arial bold;text-align:center;font-size:150%;">Father's_Name/Husband's_Name:<input type="text" name="f_name"></p></tr>
<tr>
		

<p style="color:black;font-family:arial bold;text-align:center;font-size:150%;">Nominee_Name:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="text" name="n_name"></p></tr>
<tr>
		

<p style="color:black;font-family:arial bold;text-align:center;font-size:150%;">Relationship_A/C_Holder:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="text" name="relationship"></p></tr>
<tr>
		

<p style="color:black;font-family:arial bold;text-align:center;font-size:150%;">Address:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="text" name="address"></p></tr>
<tr>
		

<p style="color:black;font-family:arial bold;text-align:center;font-size:150%;">Aadhar_No:<span style="color:red">&#42;</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="text" name="aadhar_no" required></p></tr>
<tr>
		

<p style="color:black;font-family:arial bold;text-align:center;font-size:150%;">Pan_No:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="text" name="pan_no"></p></tr>
<tr>
		

<p style="color:black;font-family:arial bold;text-align:center;font-size:150%;">Mobile_no:<span style="color:red">&#42;</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="tel" name="mobile_no" pattern="^\d{10}$" required></p></tr>

<tr>
		

<p style="color:black;font-family:arial bold;text-align:center;font-size:150%;">E-mail:<span style="color:red">&#42;</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="text" name="email" required></p></tr>

<tr>		

<p style="color:black;font-family:arial bold;text-align:center;font-size:150%;"><input type="submit" value="Submit">&nbsp;&nbsp;<button type="reset" value="Reset">Reset</button>&nbsp;&nbsp;<input type="button" value="Back" onclick="history.back(-1)"></p></tr>

</table>


</form>

""")
print("</html>")