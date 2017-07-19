'''
Sawyer Coleman
US05 File
SSW_555_Agile_Methods
BHS_Project_SSW_555
Project08
'''

from datetime import datetime

NA = "N/A"

def toDate(dateStr):
    if dateStr == NA:
        return None
    else:
        return datetime.strptime(dateStr, '%d %b %Y')

def US05(MARR=NA, DEAT=NA):
    death_dt = toDate(DEAT)
    marr_dt = toDate(MARR)
    
    if (marr_dt == None):
        return True
    
    elif (death_dt != None):
            if (marr_dt >= death_dt):
                return False

    return True
