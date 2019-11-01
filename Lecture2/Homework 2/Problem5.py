import datetime
import time
import calendar

birthday = datetime.date(1994, 2, 12)
print ("My birthday: ", birthday)
print ("The year of my birthday: ", birthday.year)    
print ("The month of my birthday: ", birthday.month) 
print ("The day of my birthday: ", birthday.day) 
print('The weekday of my birthday: ', birthday.isoweekday())

nextbirthday = datetime.date(2020, 2, 12)
print("How many days are left till my upcoming birthday: ", nextbirthday-datetime.date.today())

print (calendar.month(2017, 5))
one_day = datetime.timedelta(days = 1)
print("Yesterday: ", (datetime.datetime.today()-one_day))