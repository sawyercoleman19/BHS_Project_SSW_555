'''
    Bharath Kumar
    US06 Functions File
    SSW_555_Agile_Methods
    BHS_Project_SSW_555
    Sprint 2
    '''
import usefulFunctions as UF


def US12(MOM,DAD,CHIL = "N/A"): #mother should be less than 60 years older than her children and father should be less than 80 years older than his children
    # print "OK"
    MOMAGE = int(UF.Age(MOM))
    DADAGE = int(UF.Age(DAD))
    CHILAGE =int(UF.Age(CHIL))
    # print "OK"
    err = []
    if CHIL != "N/A":
        if MOMAGE - CHILAGE < 60 and DADAGE - CHILAGE < 80:
            pass
        else:
            if MOMAGE - CHILAGE >= 60:
                err.append("MOM")
            if DADAGE - CHILAGE >= 80:
                err.append("DAD")
    return err


# US12("15 MAY 1980","20 MAR 1972","05 JUN 1995")