'''
    Sawyer Coleman
    US07 Functions File
    SSW_555_Agile_Methods
    BHS_Project_SSW_555
    Homework04
'''

from datetime import datetime
import calendar

'''Calculates Age'''

months = {"JAN": 1,"FEB": 2 ,"MAR": 3,"APR": 4,"MAY": 5,"JUN": 6,"JUL": 7,"AUG":8,"SEP": 9,"OCT": 10,"NOV": 11,"DEC": 12 }

#Calculates the age from date of birth to current date, assuming there is no date of death

def AgeLive(DoB):
    '''JRR: Your logic is correct, but you can simplify it to
        birth_date = datetime.strptime(DoB, '%d %b %Y') 
        age = (datetime.today() - birth_date).days/365
        return age
    '''
    birth = DoB.split(" ")[::-1]
    birth[1] = months[birth[1]]
    bDay = str(birth[0])
    bYear = str(birth[2])
    mn = str(birth[1])
    birth_date_orig = bDay+"/"+mn+"/"+bYear
    birth_date = datetime.strptime(birth_date_orig, '%Y/%m/%d')
    age = (datetime.today() - birth_date).days/365

    return age

#Calculates age from date of birth to date of death

def AgeDeath(DoB, DoD):

    '''JRR: Your logic is correct, but you can simplify it to
        birth_date = datetime.strptime(DoB, '%d %b %Y') 
        death_date = datetime.strptime(DoD, '%d %b %Y')
        age = (death_date - birth_date).days/365
        return age
    '''
    birth = DoB.split(" ")[::-1]  # why reverse the string?
    birth[1] = months[birth[1]]
    mn = str(birth[1])
    bDay = str(birth[0])
    bYear = str(birth[2])
    birth_date_orig = bDay+"/"+mn+"/"+bYear
    birth_date = datetime.strptime(birth_date_orig, '%Y/%m/%d')
    
    death = DoD.split(" ")[::-1]
    death[1] = months[death[1]]
    mn = str(death[1])
    dDay = str(death[0])
    dYear = str(death[2])
    death_date_orig = dDay+"/"+mn+"/"+dYear
    death_date = datetime.strptime(death_date_orig, '%Y/%m/%d')
    
    age = (death_date - birth_date).days/365
    
    return age

def US07(BirthDate, DeathDate = "N/A"):
    ''' JRR: I like how you used optional parameters for the DeathDate.   Just beware that BirthDate may be unknown as well.
        GEDCOM allows you specify both but doesn't require it.
    '''
    # AgeLive = BHS_555.AgeLive(DoB)
    # AgeDeath = BHS_555.AgeDeath(DoB, DoD)
    if (DeathDate == "N/A"):
        if (AgeLive(BirthDate) < 150):
            return True
        elif (AgeLive(BirthDate) >= 150):
            print("ERROR: INDIVIDUAL: US07: Individual "+ +" is older than 150 years old")
            return False
    elif (AgeDeath(BirthDate, DeathDate) < 150):
        return True
    elif (AgeDeath(BirthDate, DeathDate) >= 150):
        print("ERROR: INDIVIDUAL: US07: Individual "+ +" was older than 150 years old")
        return False
