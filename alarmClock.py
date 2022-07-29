from datetime import datetime
from playsound import playsound
alarm time = input("Enter the time of alarm to be set:HH: MM: SS\n")
alarm_hour=alarm_time[0:2]
alarm_minute=alarm_time[3:5]
alarm seconds=alarm time[6:8]
print ("Setting up alarm..
while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    if (alarm hour==current hour):
        current_minute = now.strftime ("%M" )
        if (alarm minute==current_minute):
            current seconds = now.strftime(''%5"')
            if (alarm_seconds==current_seconds):
                print ("Wake Up!")
                playsound('audio.mp3")
                break