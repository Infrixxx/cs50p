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
def main():

        time=input("What time is it? ")     #input is always string so keep in mind to cast it to intended type.
        
        final_time=convert(time)
        
        if final_time>=7 and final_time<=8:
                print("breakfast time")
        
        elif final_time>=12 and final_time<=13:
                print("lunch time")
        
        elif final_time>=18 and final_time<=19:
                print("dinner time")


def convert(time):

    time=time.strip() #remove white space
    time_array=time.split(":") #create array of hour and minutes
    time_minute=int(time_array[1])/60 
    final_time=float(int(time_array[0])+time_minute)

    return final_time




if __name__ == "__main__":
    main()
