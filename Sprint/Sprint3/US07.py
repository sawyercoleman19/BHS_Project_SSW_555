'''
    Sawyer Coleman
    US07 Functions File
    SSW_555_Agile_Methods
    BHS_Project_SSW_555
    Homework04
    '''

from datetime import datetime
import calendar
import BHS_555
import usefulFunctions

NA = "N/A"

'''Calculates Age'''

#Calculates the age from date of birth to current date, assuming there is no date of death

def US07(BIRT = NA, DEAT = NA):
    if (DEAT == NA):
        if (int(usefulFunctions.Age(BIRT, DEAT)) < 150):
            return True
        else:
            #print("ERROR: INDIVIDUAL: US07: Individual is older than 150 years old")
            return False
    elif (int(usefulFunctions.Age(BIRT, DEAT)) < 150):
        return True
    else:
        #print("ERROR: INDIVIDUAL: US07: Individual was older than 150 years old")
        return False
