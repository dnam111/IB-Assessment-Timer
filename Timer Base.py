import time
current = time.localtime()
current_time = time.strftime("%H:%M:%S", current)
print("The Current Time is "+ current_time)

def countdown(t):
    while t != 0:
        hour, secs = divmod(t, 3600)
        mins, secs = divmod(t % 3600, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hour, mins, secs)
        time.sleep(1)
        t -= 1
        print(timer, end="\r")
        if t == 0:
            print("Time Elapsed")

hours = int(input("Please input the number of hours: "))
minutes = int(input("Please input the number of minutes: "))
seconds = int(input("Please input the number of seconds: "))
t = (3600*hours)+(60*minutes)+seconds

countdown(t)
