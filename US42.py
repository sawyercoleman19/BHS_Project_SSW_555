import BHS_555 as db

def checkDate(dt, idd, context):
    if dt == 'N/A':
        return True
    else:
        try:
            datetime.date(datetime.strptime(dt, "%d %b %Y"))
        except ValueError:
            print "In US 42, " + idd + "'s " + context + " date of " + dt + " is invalid."
            return False
        else:
            return True


def US42():
    for i in IndDic:
        checkDate(IndDic[i]["BIRT"], i,"birth date")
        checkDate(IndDic[i]["DEAT"], i,"death date")
        
        
    for f in FamDic:
        checkDate(FamDic[f]["MARR"], f,"marrige date")
        checkDate(FamDic[f]["DEAT"], f,"divorce date")
