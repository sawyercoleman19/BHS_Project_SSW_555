"""This file is where group members will copy and paste 
functions used in their user stories and add a brief description
as to what they do. Any group member can use those functions and
tweak them to help their own user stories if they are appropriate"""

#----------------------------------------------------------------------------------

#UPDATE LOG:

#Sawyer 6/28 - Added NA Variable

#----------------------------------------------------------------------------------


import datetime
#import BHS_555 as db #==> we cannot import BHS or any user stories file in usefulFunctions because it creats a loop causing deadlock situtaion.

#----------------------------------------------------------------------------------

#Global variables should go here

months = {"JAN": 1, "FEB": 2 ,"MAR": 3,"APR": 4,"MAY": 5,"JUN": 6,"JUL": 7,"AUG": 8,"SEP": 9,"OCT": 10,"NOV": 11,"DEC": 12 }

NA = "N/A"
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

#Global functions should go here


#This function from US23 returns all male children given list of children
# Dont Call this function from useful function call this function from US23 there is another copy in that file
# If u call it will be a deadlock

"""

def maleChild(CHIL):
	male_Child = []
	for j in CHIL:
		if db.IndDic[j]["SEX"] == "M":
			#print db.IndDic[j]["NAME"]
			male_Child.append(db.IndDic[j]["NAME"])
	return male_Child.sorted()
"""
#Calculates age in years

def Age(BIRT = NA, DEAT = NA): #Return the Age in Years
    if (DEAT == NA and BIRT == NA):
        return ("Error")
    today = datetime.date.today()
    tod = str(today).split("-")
    bir = BIRT.split(" ")[::-1]
    bir[1] = months[bir[1].upper()]
    
    if DEAT != NA:
        tod = DEAT.split(" ")[::-1]
        tod[1] = months[tod[1]]
    
    age = int(tod[0])-int(bir[0])
        
    if int(tod[1]) < int(bir[1]):
        age -= 1
    elif int(tod[1]) == int(bir[1]) and int(tod[2]) < int(bir[2]):
        age -= 1
        
    return str(age)
"""
#returns the 1st child in a family
# please dont use this function too have this as a template if needed 
def firstChild(CHIL): 
    chilage = {}
    for j in CHIL:
        chilage[int(db.IndDic[j]["AGE"])] = j
    return chilage[sorted(chilage.keys())[-1]]
"""

# This function is used in US08, US09

def leapyear (year):  # Returns true if its a leap year and False if its not a leap year

    if (year % 4) == 0:
       if (year % 100) == 0:
           if (year % 400) == 0:
               return True
           else:
               return False
       else:
           return True
    else:
       return False

# This function is used in US35, US36

def TimeDelta(NOday): #Returns the date after number of days from today if its positive before the number of days from today if negative
    tday = datetime.date.today()
    tdelta = datetime.timedelta(days=NOday)
    return(tday + tdelta)

def NoDays(year,month,date): #Returns the number of days from today
    try:
      startDate = datetime.date(year, month, date)
      tday = datetime.date.today()
      return(startDate - tday).days
    except ValueError:
      return False

def MonthInNum(mon):
    return str(months[mon.upper()])

if __name__ == "__main__":
    pass
