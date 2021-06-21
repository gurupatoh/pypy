# class Date:
import datetime
    

class Date:
    __MonthNames=[]
    def __init__(self,number,year,month,day):
        self.year=year
        self.month=month
        self.day=day
        self.number=number
        person.__MonthNames=['January','february','march','april','may','june','july','august','september','octonber','november','december']
        def getMonthName (number):
                if number == 1:
                    return "January"
                elif number == 2:
                    return "February"
                elif number == 3:
                    return "March"
                elif number == 4:
                    return "April"
                elif number == 5:
                    return "May"
                elif number == 6:
                    return "June"
                elif number == 7:
                    return "July"
                elif number == 8:
                    return "August"
                elif number == 9:
                    return "September"
                elif number == 10:
                    return "October"
                elif number == 11:
                    return "November"
                elif number == 12:
                    return "December"

def getDaysInMonth(month,year):
    if month == "February":
    	print("No. of days: 28/29 days")
    elif month in ("April", "June", "September", "November"):
        print("No. of days: 30 days")
    elif month in ("January", "March", "May", "July", "August", "October", "December"):
        print("No. of days: 31 day")
        
@classmethod
def isValidYear(year):
    if(year==datetime(int(year))):
        return True
    elif (year !=datetime(int(year))):
        return False
@classmethod
def isValidMonth(month):
    if(month==datetime(int(month))):
        return True
    elif (month==datetime(int(month)) and month >= 1 and month <= 12):
        return False
@classmethod
def isValidDay(day, month, year):
 
         if ((month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and ((day<=31) and (day>=1)) ):
             return True
         elif  ((month == 4 or month == 6 or month == 9 or month == 11) and((day<=30) and (day>=1))):
             return True
         elif ((month == 2) and ((day<=29) and (day>=1))):
             return True
         elif ((month == 2) and  ((day<=28) and (day>=1))):
             return True
         else:
                 return False
         
    


  
    



        
        


