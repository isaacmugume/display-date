#MUGUME ISAAC
#16/U/648
#BELE



import datetime,calendar
current_year = 2017
date = input("ENTER YOUR DATE OF BIRTH (1-31)\n")
endings = ["st","nd","rd"] + 17*["th"]+ ["st","nd","rd"] + 7*["th"] + ["st"]
days = ['Monday','Tuesday','Wednesday','Thursday',
        'Friday','Saturday','Sunday']

month = int(input("ENTER THE MONTH IN WHICH YOU WERE BORN (1-12)\n"))
month_names = ['January', 'February', 'March', 'April', 'May',
               'June', 'July', 'August', 'September', 'October',
               'November', 'December']
year = int(input("WHAT'S YOUR AGE?\n"))
Y1 = month_names[month-1]
Y2 = int(date)
Y3 = (current_year-year)
Y4 = date+endings[Y2-1]
Y5 = calendar.weekday(Y3,month,Y2)
Y6 = days[Y5]

this = Y1+" ", Y2, ",", Y3
print("YOU CAME INTO THIS WORLD ON ",Y6,Y4,Y1, "of the year",Y3)
