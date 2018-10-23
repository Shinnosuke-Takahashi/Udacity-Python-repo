#This program asks the user to input two dates and prints the number of days in between them.
#This program assumes that both dates are within the Gregorian calendar.
#This program also assumes that the dates are entered in the following format: yyyy, mm, dd

year1 = int(input("Enter the start year: "))
month1 = int(input("Enter the start month: "))
day1 = int(input("Enter the start day: "))
year2 = int(input("Enter the end year: "))
month2 = int(input("Enter the end month: "))
day2 = int(input("Enter the end day: "))

Month30 = [4, 6, 9, 11]
Month31 = [1, 3, 5, 7, 8, 10, 12]

def isLeapYear(year):
    if year%400 == 0:
        return True
    elif year%100 == 0:
        return False
    elif year%4 == 0:
        return True
    else:
        return False

def daysInMonth(year, month):
    if month in Month30:
        return 30
    elif month in Month31:
        return 31
    elif month == 2:
        if isLeapYear(year):
            return 29
        else:
            return 28
        
def nextDay(year, month, day):
    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
        
def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False        

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

print(daysBetweenDates(year1, month1, day1, year2, month2, day2))
