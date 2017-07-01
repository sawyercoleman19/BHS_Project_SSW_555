"""This file is where group members will copy and paste 
functions used in their user stories and add a brief description
as to what they do. Any group member can use those functions and
tweak them to help their own user stories if they are appropriate"""

#----------------------------------------------------------------------------------

#UPDATE LOG:

#Sawyer 6/28 - Added NA Variable

#----------------------------------------------------------------------------------


import datetime

#----------------------------------------------------------------------------------

#Global variables should go here

months = {"JAN": 1, "FEB": 2 ,"MAR": 3,"APR": 4,"MAY": 5,"JUN": 6,"JUL": 7,"AUG": 8,"SEP": 9,"OCT": 10,"NOV": 11,"DEC": 12 }

NA = "N/A"
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

#Global functions should go here


#This function from US23 returns all male children given list of children

def maleChild(CHIL):
	male_Child = []
	for j in CHIL:
		if db.IndDic[j]["SEX"] == "M":
			#print db.IndDic[j]["NAME"]
			male_Child.append(db.IndDic[j]["NAME"])
	return male_Child

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

if __name__ == "__main__":
    pass
