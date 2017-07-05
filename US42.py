import BHS_555 as db

def checkDate(dt, idd, context):
    if dt == 'N/A':
        pass
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
        checkDate(IndDic[i]["BIRT"], IndDic[i][idd],"birth date")
        checkDate(IndDic[i]["DEAT"], IndDic[i][idd],"death date")
        
        
    for f in FamDic:
        checkDate(FamDic[f]["MARR"], FamDic[f][ID],"marrige date")
        checkDate(FamDic[f]["DEAT"], FamDic[f][ID],"divorce date")
