# Python program to book movie tickets
print("OFF on Wednesdays")
date = str(input("Enter the date of booking: "))
print("type date in format DD MM YYYY")
y=("Monday = 170","{Tuesday = 170}","Wednesday = Off Day","Thursday = 220","Friday = 300","Saturday = 300","Sunday = 320")
for w in y:
  print(w)

import datetime

def findDay(date):
    day, month, year = (int(i) for i in date.split(' '))
    date_obj = datetime.datetime(year, month, day)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[date_obj.weekday()]

day_of_week = findDay(date)
print(f"The day of the week for {date} is: {day_of_week}")
name=str(input("Enter Your Name: "))
contactno=int(input("ENTER YOUR MOBILE NO.: "))
print("select the movie: 1.Bhool Bhulaiyaa 3D")
print( "2.Ghazini 2")
print("3.Higer")
print("4.Raone 2")
t=int(input("Enter the SR.No. of Movie"))
if(t)==int(1):
 u=int(2.5)
if(t)==int(2):
 u=int(1.5)
if(t)==int(3):
 u=int(2)
if(t)==int(4):
 u=int(2.5)
date = str(input("Enter the date of booking: "))
QUANTITY=int(input("No. of People: "))
print(findDay(date))
if (findDay(date))==("Monday"):
 v=int(170)
 AMOUNT=QUANTITY*v*u
 print("Ticket price = ",v*u)
 print("Ticket Amount=",AMOUNT)
elif (findDay(date))==("Tuesday"):
  v=int(170)
  AMOUNT=QUANTITY*v*u
  print("Ticket price = ",v*u)
  print("Ticket Amount=",AMOUNT)
elif (findDay(date))==("Thursday"):
  v=int(220)
  AMOUNT=QUANTITY*v*u
  print("Ticket price = ",v*u)
  print("Ticket Amount=",AMOUNT)
elif (findDay(date))==("Friday"):
   v=int(250)
   AMOUNT=QUANTITY*v*u
   print("Ticket price = ",v*u)    
   print("Ticket Amount=",AMOUNT)
elif (findDay(date))==("Saturday"):
   print("Ticket price = ",v*u)
   v=int(300)
   AMOUNT=QUANTITY*v*u
   print("Ticket Amount",AMOUNT)
elif (findDay(date))==("Sunday"):
   v=int(320)
   print("Ticket price = ",v*u)
   AMOUNT=QUANTITY*v*u
   print("Ticket Amount=",AMOUNT)
else:
    print("Sorry No Booking at that Time")
    exit()

j=int(input("For Confirm Booking Press 1 else 0: "))
if j==1:
 print("Congrats Your Tickets have been booked"
           "    See you at Movies"
       "   Enjoy your movie",name)
elif j==0:
 print("Sorry your booking is cancelled")
 exit()
else:
 print("Server Not Found")

