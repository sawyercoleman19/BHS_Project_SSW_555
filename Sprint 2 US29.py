#US29 List Deceased

import BHS_555 as db

def US29_ListDead(IndDic):
    deathList = []
    for a in IndDic:
        if db.IndDic[a]["Deat"] == "N/A":
            pass
        else:
            deathList.append(db.IndDic[a]["NAME"])
    print "These family members seem to have passed away: "  + deathList
    
    
    #add id, name and death dtae to output
            
            
            
