'''import calendar
n=int(input("Enter the year"))
print(calendar.calendar(n))

x=calendar.weekday(2025,4,24)
days=["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
print(days[x])
'''

#To Find the difference between from My brithday to todays date
from datetime import date

birthday = date(2005, 1, 13) 
today = date.today()
difference = today - birthday
print(f"Days since your birthday: {difference.days}")
