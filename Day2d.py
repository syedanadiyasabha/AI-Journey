from datetime  import date
import math
name=input("Enter your name : ")
dob=input("Enter your DOB: ")
month=int(input("Enter your birth year: "))
desig=input("Enter your designation:")
qual=input("Enter your Qualification : ")
cntry=input("Enter your country : ")
no=int(input("Enter your phone number : "))
age= date.today().year
currage=age-month
print(f" Hi {name} as per your given date of birth your current age is {currage}")
info=input("Please specify whether you want your details to be in uppercase or lowercase : ")
if (info == "uppercase"):
   
       print( name.upper() ,desig.upper(),
              qual.upper(),
              cntry.upper() )
else:
    
        print( name.lower(),
        desig.lower(),
        qual.lower(),
        cntry.lower())


    