#Test for user story 29
##US29 List Deceased

#import BHS_555 as db

#def US29_ListDead(IndDic):
#    deathList = []
#    for a in IndDic:
#        if db.IndDic[a]["Deat"] == "N/A":
#            pass
#        else:
#            deathList.append(db.IndDic[a]["NAME"])
#    print "These family members seem to have passed away: "  + deathList

       
            
    
 def deadTest(IndNameDeath):
        for i, val in enumerate(IndNameDeath):
            if val != "N/A":
                print i + "has passed away" 
                return True
        
                
                
            
def test1():
    IndNameDeath = [("Joe", "1/1/2000"), ("Mike", "N/A"), ("Ed", "N/A")]
    deadTest(IndNameDeath)
    #Joe is dead

def test2():
    IndNameDeath = [("Joe", "N/A"), ("Mike", "N/A"), ("Ed", "N/A")]
    deadTest(IndNameDeath)
    #nobody is dead

def test3():
    IndNameDeath = [("Joe", "1/1/2000"), ("Mike", "2/3/1880"), ("Ed", "1/1/1990")]
    deadTest(IndNameDeath)
    #Everyone is dead
    
def test4():
    IndNameDeath = [("Joe", "N/A"), ("Mike", "1/1/2000"), ("Ed", "5/7/2007")]
    deadTest(IndNameDeath)
    #Mike and Ed are dead

def test5():
    IndNameDeath = [("Joe", "N/A"), ("Mike", "N/A"), ("Ed", "1/2/2009")]
    deadTest(IndNameDeath)
    #Ed is dead