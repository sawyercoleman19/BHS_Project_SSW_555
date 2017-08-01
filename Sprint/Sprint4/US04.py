'''
Sawyer Coleman
US04 File
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

def US04(MARR=NA, DIV=NA):
    marr_dt = toDate(MARR)
    div_dt = toDate(DIV)
    
    if (div_dt == None):
        return True
    
    else:
        if (marr_dt == None):
            return False
    
        else:
            if (marr_dt >= div_dt):
                return False

    return True
