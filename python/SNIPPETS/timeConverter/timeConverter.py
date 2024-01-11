#Convert seconds to the equivalent hour, min, and seconds

time = int(input("Enter time in seconds: "))

seconds = 0
minutes = 0
hours = 0
hrs = ""
mins = ""
secs = ""

hours = time//3600
time %= 3600

minutes = time//60
time %= 360

seconds = time

if hours > 1:
    hrs = "hrs"
else: hrs = "hr"

if minutes > 1:
    mins = "mins"
else: mins = "min"

if seconds > 1:
    secs = "secs"
else: secs = "sec"

print('The time: {0}{3} : {1}{4} : {2}{5}'.format(hours, minutes, seconds, hrs, mins, secs))


