#!/usr/bin/python
# -*- coding: utf-8 -*-

'''

Simple School bell

It's time to finish the school, take a Music file and select and hour. Be saved by the bell with style!

Example writted by Julián Caro Linares

Partially based in the code of user2340615 and the fixed example of Noelkd at Stackoverflow. Thank you so much!

https://stackoverflow.com/questions/16325039/python-alarm-clock

jcarolinares@gmail.com

CC-BY-SA

'''

import time
import os
import pygame #For playing a wav sound file



class Alarm():
    def __init__(self, hours, minutes,hours_2, minutes_2,music_time):
        super(Alarm, self).__init__()
        self.hours = int(hours)
        self.minutes = int(minutes)
        self.hours_2 = int(hours_2)
        self.minutes_2 = int(minutes_2)
        self.music_time=int(music_time)
        self.fadeout=2000
        #self.keep_running = True

    def run(self):

            while True:
                now = time.localtime()
                if ((now.tm_hour == self.hours and now.tm_min == self.minutes) or (now.tm_hour == self.hours_2 and now.tm_min == self.minutes_2)):
                    print("\n\nBELL TIME!!!\n\n")
                    pygame.mixer.init()
                    sound = pygame.mixer.Sound("music.wav")
                    sound.play()
                    time.sleep(self.music_time-(int(self.fadeout/1000)))
                    sound.fadeout(self.fadeout)
                    print("\n\nWaiting fot the next alarm at: "+str(self.hours)+" : "+str(self.minutes)+"\n\n")
                    time.sleep(60)


#Main execution
def main():

    alarm_HH = input("\n\nEnter the hour you want to play the bell: \n\n")#Put here directly the hours if you want alarm_HH=14
    alarm_MM = input("\n\nEnter the minute you want to play the bell: \n\n") #Put here directly the minutes if you want alarm_MM=10

    print("\n\nYou'll be saved by the bell at: " + str(alarm_HH) +" : "+ str(alarm_MM) +"\n\n")

    alarm_HH_2 = input("\n\nEnter the hour you want to play the bell for the second time: \n\n")#Put here directly the hours if you want alarm_HH=14
    alarm_MM_2 = input("\n\nEnter the minute you want to play the bell for the second time: \n\n") #Put here directly the minutes if you want alarm_MM=10
    music_time=input("\n\nEnter the number of seconds that you want to play the music file\n\n")

    print("\n\nYou'll be saved by the second bell at: " + str(alarm_HH_2) +" : "+ str(alarm_MM_2) +"\n\n")

    alarm = Alarm(alarm_HH, alarm_MM,alarm_HH_2,alarm_MM_2,music_time)
    alarm.run()



if __name__ == "__main__":
 main()
