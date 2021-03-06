'''
    Sawyer Coleman
    US01 Functions File
    SSW_555_Agile_Methods
    BHS_Project_SSW_555
    Project04
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
def US01_ind(BIRT=NA, DEAT=NA):
    CrntDate = datetime.today()
    birth_dt = toDate(BIRT)
    death_dt = toDate(DEAT)
    okay = True
    
    if (birth_dt != None):
        if (birth_dt > CrntDate):
            # I Commented these as we are printing these in the BHS file itself
            #print ("ERROR: INDIVIDUAL: US01: The date of birth, "+ BIRT +", occurs in the future")
            okay = False
            return "False Birth"
        else:
            okay = True
    if (death_dt != None):
        if (death_dt > CrntDate):
            #print ("ERROR: INDIVIDUAL: US01: The date of death, " + DEAT +", occurs in the future")
            okay = False
            return "False Death"
        else:
            okay = True

    return okay    

def US01_fam(MARR=NA, DIV=NA):
    CrntDate = datetime.today()
    marr_dt = toDate(MARR)
    div_dt = toDate(DIV)
    okay = True
    if (marr_dt != None):
        if (marr_dt > CrntDate):
            #print ("ERROR: FAMILY: US01: The marriage date, " + MARR +", occurs in the future")
            okay = False
            return "False Marr"
        else:
            okay = True
    if (div_dt != None):
        if (div_dt > CrntDate):
            #print ("ERROR: FAMILY: US01: The divorce date, " + DIV +", occurs in the future")
            okay = False
            return "False Div"
        else:
            okay = True
    # other date checks go here...
    
    return okay
