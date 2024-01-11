import datetime
import pytz

#NAIVE vs AWARE DATE&TIME
#Naive date/time don't have enough info to determine things like; timezone, daylight savings time etc
#Naive date & Time are easier to work with
#Aware date/time is the opposite of Naive date/time

#THERE ARE 3 PARTS; DATETIME.DATE, DATETIME.TIME and DATETIME.DATETIME

#============================================ DATETIME.DATE ==============================
#CREATE A DATE
date = datetime.date(2020, 12, 19)
print(f'THE DATE YOU CREATED IS:  {date}')

#GET TODAY'S DATE
today = datetime.date.today()
print(f"TODAY'S DATE IS: {today}")



#GET YEAR, MONTH OR DAY
today = datetime.date.today()
todayDay = today.day
todayMonth = today.month
todayYear = today.year
print(f"TODAY'S DATE IS; DAY:{todayDay}, MONTH:{todayMonth}, YEAR:{todayYear}")

#GET THE DAY OF THE WEEK
today = datetime.date.today()
todayWeekDay = today.weekday()      #Takes Monday as the first day of the week counting from 0 (ie: 0-6)
todayWeekDay2 = today.isoweekday()  #Takes Monday as the first day of the week counting from 1 (ie: 1-7)
print(f"TODAY'S WEEKDAY IS: {todayWeekDay} AND ALSO: {todayWeekDay2}")


#TIME DELTAS (Difference between two days or times)
today = datetime.date.today()
#timeDelta = datetime.timedelta(days=14)
timeDelta = datetime.timedelta(days=14, hours=12, minutes=56, seconds=33, milliseconds=2000)
nextDate = today + timeDelta
previousDate = today - timeDelta
print(f"14 DAYS FROM NOW WILL BE: {nextDate}")
print(f"14 DAYS AGO WAS {previousDate}")


#NOTE: -- Date1 = todayDate + timeDelta --
#      -- (+-)timeDelta = (+-)Date1 - today
date = datetime.date(2021, 12, 19)
today = datetime.date.today()
difference = date - today
print(f"DIFFERENCE BETWEEN DATE TO COME AND TODAY(in days) IS: {difference}, OR:{difference.days}")
print(f"DIFFERENCE BETWEEN DATE TO COME AND TODAY(in seconds) IS: {difference.total_seconds()}")


#================================== DATETIME.TIME ==============================
#SET TIME
time = datetime.time(9,30,45,1250)
print(f"THE TIME YOU DEFINED IS: {time}")

#PRESENT TIME
time2 = datetime.datetime.now().time()
print(f'THE TIME NOW IS: {time2}')

#============================ DATETIME.DATETIME =================================
t = datetime.datetime(2020,8,28,11,54,33,2000)
print(f'THE DATE-TIME YOU DEFINED IS: {t}')
print(f'THE DATE ONLY IS: {t.date()}')
print(f'THE TIME ONLY IS {t.time()}')
print(f'THE YEAR ENTERED IS: {t.year}')

#=================== USING TIME DELTA WITH THE DATETIME.DATETIME ===============
timeDelta = datetime.timedelta(hours=26)
tTime = t + timeDelta
print(f'26 HOURS FROM NOW WILL BE: {tTime}')


#====================================   SIMILAR DATETIME METHODS ============================
dt_today = datetime.datetime.today() #Returns current datetime with a timezone of none
dt_now = datetime.datetime.now()     #Returns current datetime with optional timezone
dt_utcnow = datetime.datetime.utcnow()

print(f'DATETIME.TODAY IS: {dt_today}')
print(f'DATETIME.NOW IS: {dt_now}')
print(f'DATETIME.UTCNOW IS: {dt_utcnow}')


# ======================================    AWARE DATETIME  ===================================
# =======================================   USING PYTZ  ========================

t = datetime.datetime(2020,8,28,11,54,33,2000, tzinfo=pytz.UTC)
print(f'THE DATETIME USING pytz is: {t}')
