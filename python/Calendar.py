import calendar

cal = calendar.month(2020, 1)

print(calendar.month(2020,1))
print(calendar.calendar(2020))

print("First week")
print(calendar.firstweekday() + 2)

print('Is this year a leap year? : {}'.format(calendar.isleap(2021)))

print(calendar.monthcalendar(2020, 9))

