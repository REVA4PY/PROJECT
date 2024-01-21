#TO PRINT THE CALENDAR OF THE YEAR
import calendar
yy = int(input("enter the year:"))
x = calendar.calendar(yy)
print(x)
print ("----------------------")

#TO CHECK WHETHER THE GIVEN YEAR IS LEAP YEAR OR NOT
yy = int(input("enter the year:"))
if yy % 4 == 0:
    print(yy,"is a leap year")
else:
    print(yy,"is not a leap year")
