'''
    Sawyer Coleman
    US10 Function File
    SSW_555_Agile_Methods
    BHS_Project_SSW_555
    Sprint 4
'''

import usefulFunctions

NA = "N/A"

#Compares the birthdate to marriage date and returns false if the difference if over 14 years old

def US10(BIRT = NA, MARR = NA):
    if (MARR != NA):
        if (int(usefulFunctions.Age(BIRT, MARR)) < 14):
            return False
        else:
            return True
    else:
        return True
