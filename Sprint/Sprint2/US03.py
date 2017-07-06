'''
    Sawyer Coleman
    US03 Functions File
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

def US03(BIRT=NA, DEAT=NA):
    birth_dt = toDate(BIRT)
    death_dt = toDate(DEAT)
    
    if (death_dt == None):
        return True
    
    elif (birth_dt != None):
        if (birth_dt >= death_dt):
            return False

    return True
