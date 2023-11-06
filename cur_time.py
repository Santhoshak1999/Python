#Write a Python program to display the current date and time.

#The strftime() method returns a string representing date and time using date, time or datetime object.


import datetime
print("Date and time is: ")
now = datetime.datetime.now()
print(now)
#to specify the formate for date and time
print("Year :" + now.strftime("%Y"))
print("Month:"+ now.strftime("%m"))
print("Day :" + now.strftime("%d")) #%D specifies the hole day
#but %d specifies the only day
print("Date : "+ datetime.datetime.now().strftime("%D"))
print("Time Details :")
print("Hour : " + now.strftime("%H"))
print("Min : " + now.strftime("%M"))
print("Hour : " + now.strftime("%S"))
print("Date and Time is: ")
print(now.strftime("%d-%m-%Y, %H:%M:%S"))


