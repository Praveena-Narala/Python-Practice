from datetime import datetime   
from playsound import playsound
while True:
    alarm_time = input("Enter the time of alarm to be set:HH:MM:SS:am/pm \n")
    try:
        alarm_hour=int(alarm_time[0:2])
        alarm_minute=int(alarm_time[3:5])
        alarm_seconds=int(alarm_time[6:8])
        alarm_period = ''
        if alarm_time[9:11].isalpha():
            alarm_period = alarm_time[9:11].upper()
    except:
        print('Invalid Time')
    if int(alarm_hour)<=12 and int(alarm_minute)<=59 and int(alarm_seconds)<=59 and alarm_period in ('AM','PM'):
        print('Valid Time')
        break
    else:
        print('Input Out of range')
    print("Please Enter Time Correctly")
print(alarm_hour,alarm_minute,alarm_seconds,alarm_period)
print("Setting up alarm..")
while True:
    now = datetime.now()
    current_hour = int(now.strftime("%I"))
    current_minute = int(now.strftime("%M"))
    current_seconds = int(now.strftime("%S"))
    current_period = now.strftime("%p")
    if(alarm_period==current_period):
        if(alarm_hour==current_hour):
            if(alarm_minute==current_minute):
                if(alarm_seconds==current_seconds):
                    print("Wake Up!")
                    playsound('C:\\Users\\narala.reddy\\Documents\\audio.mp3')
                    break