import time

#The time.time() (NOT time.clock() which is deprecated) function allows us measure the time of parts of a program's execution. returns a floating point value representing elapsed time in seconds
#The time.sleep() function gives delay
#time.time() is time in seconds from the epoch time.

#TIME.TIME()
print(time.time()) #Epoch time. ie. from 12:00am jan 1 1970
input("Press enter to begin ")
start_time = time.time()
name = input("Start typing text here: ")
end_time = time.time()
elapsted_time = end_time - start_time
print("ELAPSED TIME: ", elapsted_time)

#TIME.SLEEP()
statement = "Launch begins in t - "
def launch():
    for i in range(10, 0, -1):
        print('{} {} seconds'.format(statement, i))
        time.sleep(1)       # time in seconds. ie 1 -> 1 second
    print("LAUNCH was successful")
#launch()

#CURRENT TIME
currentTime = time.localtime(time.time())
currentTime2 = time.localtime(2000)
print('The current time is: {}'.format(currentTime))
print("The current time2 is: {}".format(currentTime2))
print('The current time is: {}'.format(time.ctime()))
print('The date, 2000 seconds from the epoch time .ie 1 Jan 1970 is: {}'.format(time.ctime(2000)))
print('The time current date is: {}'.format(time.gmtime()))
print('The date, 2000 seconds from the epoch time .ie 1 Jan 1970 is: {}'.format(time.gmtime(2000)))

print('\n')

formattedTime = time.asctime(currentTime)
print('The formatted time is: {}'.format(formattedTime))


splittedTime = formattedTime.split(' ')
print(splittedTime)
des = ["Day", "Month", "Month2", "Time", "Year"]

for i,j in zip(des, splittedTime):
    print(i,j)

print("\n")

splittedTime2 = splittedTime[3].split(":")
print(splittedTime2)
dec2 = ["Hour","Minute","Seconds"]
for i,j in zip(dec2, splittedTime2):
    print(i,j)

