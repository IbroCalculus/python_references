import  datetime

#Today's date and present time
print(f'TODAYS DATE & PRESENT TIME IS: {datetime.datetime.now()}')

#Today's date only
print(f'TODAYS DATE ONLY IS: {datetime.date.today()}')

#Today's date only
print(f'PRESENT TIME ONLY IS: {datetime.datetime.now().time()}')


#Formatting Dates
dateNow = datetime.datetime.now()
print(f'BEFORE FORMATTING: {dateNow}')

dateNowF1 = dateNow.strftime("%d/%m/%Y -- %H:%M:%S")
dateNowF2 = dateNow.strftime("%d/%B/%Y -- %H:%M:%S")
dateNowF3 = dateNow.strftime("%d/%b/%Y -- %H:%M:%S")
print(f'AFTER FORMATTING: {dateNowF1}')
print(f'AFTER FORMATTING: {dateNowF2}')
print(f'AFTER FORMATTING: {dateNowF3}')