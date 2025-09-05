"""
I need to take a date in 

month/day/year and set it to YYYY-MM-DD

So it can be in format of MM/DD/YYYY
or
Month_as_word DD, YYYY 

Two date cases:
---> case with "\" in str
    --->has to be start with digit between 1-12, if not reprompt.
---> case with "," in str
    ---> has to start with month, if not, reprompt
"""

def main():
    return date()

def date():

    months={
    "January":1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12
    }

    while True:
        try:

            date_str=input("Date: ").strip()

            if "/" in date_str:
                mm, dd, yy = date_str.strip().split("/")  #MM/DD/YYYY
                mm, dd, yy = int(mm), int(dd), int(yy)
            
            elif "," in date_str: #month_name date, year
                month_name, rest = date_str.split(" ",1) #split it only once, at first white space
                mm = months[month_name]
                rest = rest.replace(","," ")
                dd, yy = rest.split()
                dd, yy = int(dd), int(yy)

            else:
                continue

            if (1 <= mm <= 12) and (1 <= dd <= 31) and (yy>=1):
                print(f"{yy:04d}-{mm:02d}-{dd:02d}")
                break

        except(ValueError,KeyError):
            continue

if __name__=="__main__":
    main()
