'''
    Sawyer Coleman
    US02 Functions File
    SSW_555_Agile_Methods
    BHS_Project_SSW_555
    Project06
    '''

from datetime import datetime

NA = "N/A"

def toDate(dateStr):
    if dateStr == NA:
        return None
    else:
        try:
            return datetime.strptime(dateStr, '%d %b %Y')
        except ValueError:
            return None

def US02(BIRT=NA, MARR=NA):
    birth_dt = toDate(BIRT)
    marr_dt = toDate(MARR)
    
    if (marr_dt == None):
        return True
    
    elif (birth_dt != None):
        if (birth_dt >= marr_dt):
            return False

    return True

# print US02("7 FEB 1981","9 NOV 1957")