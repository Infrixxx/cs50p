#!/usr/bin/env python3

"""
program that prompts the user for a time
---->outputs whether:
        ---->it’s breakfast time, (7-8 am)
        ---->lunch time, ( 12:00 - 13:00 pm)
        ---->or dinner time. (18:00 - 19:00)

conditions:
            has to be in between a range.

"""

time=input("What time is it? ").split(":")

if int(time[0])>=7 and int(time[0])<=8:
    if int(time[1])>=0 and int(time[1])<=59:
        print("breakfast time")

elif int(time[0])>=12 and int(time[0])<=13:
    if int(time[1])>=0 and int(time[1])<=59:
        print("lunch time")

elif int(time[0])>=18 and int(time[0])<=19:
    if int(time[1])>=0 and int(time[1])<=59:
        print("dinner time")

