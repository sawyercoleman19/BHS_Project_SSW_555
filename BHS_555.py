'''
BHS_555

SSW 555 - Agile Methods for Software Development

Team Members:
	Bharath Kumar
	Sawyer Coleman
	Houston Migdon
    
UPDATE LOG:
6/20 - Sawyer
'''

import datetime
import US01
import US07
import US08
import US09
import US16
import US23

IndDic = {} #Dictionary containing Information of all Individual
FamDic = {} #Dictionary containing Information of all Family
IndRef = [] #List containing Individual ID (Sorted)
FamRef = [] #List containing Family ID (Sorted)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++ Table Decorators ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''Dictionary for month lettered names and numbers'''
TagList = ['INDI', 'NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'FAM', 'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV', 'DATE', 'HEAD', 'TRLR', 'NOTE']
ITagList = ['NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS']
FTagList = ['MARR', 'HUSB', 'WIFE', 'CHIL','DIV']

INDIframe = ["ID","Name","Gender","Birthday","Age","Alive","Death","Child","Spouse"]
FAMframe = ["ID","Married","Divorced","Husband ID","Husband Name","Wife ID","Wife Name","Children"]
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

'''Validates whether the tag is acceptable or not'''

def Validation(tag): #Validates the Tag
	if tag in TagList:
		return True
	else:
		return False

'''Returns the age in years - Wil'''

#Will eventually use something like below, but not for this sprint'''
''' Added: Sawyer 6/20
def Age(BIRT, DEAT):
    birth_date = datetime.strptime(BIRT, '%d %b %Y')
    death_date = datetime.strptime(DEAT, '%d %b %Y')
    age = ((datetime.today() - birth_date) - death_date).days/365
    #ageDeath = (death_date - birth_date).days/365
    return age
'''

''' One way to calculate age - Barath'''

def Age(BIRT, DEAT): #Return the Age in Years
	months = {"JAN": "01","FEB":"02" ,"MAR": "03","APR": "04","MAY": "05","JUN": "06","JUL": "07","AUG":"08","SEP": "09","OCT": "10","NOV": "11","DEC": "12" }
	today = datetime.date.today()
	tod = str(today).split("-")
	bir = BIRT.split(" ")[::-1]
	bir[1] = months[bir[1]]
	
	if DEAT != "N/A":
		tod = DEAT.split(" ")[::-1]
		tod[1] = months[tod[1]]
	
	age = int(tod[0])-int(bir[0])

	if int(tod[1]) < int(bir[1]):
		age -= 1
	elif int(tod[1]) == int(bir[1]) and int(tod[2]) < int(bir[2]):
		age -= 1

	return str(age)


'''Another way to calculate age with life and death separate - Sawyer'''
def AgeLive(DoB):
    ''' JRR: Your logic is correct, but you can simplify it to
        birth_date = datetime.strptime(DoB, '%d %b %Y')
        age = (datetime.today() - birth_date).days/365
        return age
        '''
    birth = DoB.split(" ")[::-1]
    birth[1] = months[birth[1]]
    bDay = str(birth[0])
    bYear = str(birth[2])
    mn = str(birth[1])
    birth_date_orig = bDay+"/"+mn+"/"+bYear
    birth_date = datetime.strptime(birth_date_orig, '%Y/%m/%d')
    age = (datetime.today() - birth_date).days/365
    
    return age

#Calculates age from date of birth to date of death
def AgeDeath(DoB, DoD):
    ''' JRR: Your logic is correct, but you can simplify it to
        birth_date = datetime.strptime(DoB, '%d %b %Y')
        death_date = datetime.strptime(DoD, '%d %b %Y')
        age = (death_date - birth_date).days/365
        return age
        '''
    birth = DoB.split(" ")[::-1]  # why reverse the string?
    birth[1] = months[birth[1]]
    mn = str(birth[1])
    bDay = str(birth[0])
    bYear = str(birth[2])
    birth_date_orig = bDay+"/"+mn+"/"+bYear
    birth_date = datetime.strptime(birth_date_orig, '%Y/%m/%d')
    
    death = DoD.split(" ")[::-1]
    death[1] = months[death[1]]
    mn = str(death[1])
    dDay = str(death[0])
    dYear = str(death[2])
    death_date_orig = dDay+"/"+mn+"/"+dYear
    death_date = datetime.strptime(death_date_orig, '%Y/%m/%d')
    
    age = (death_date - birth_date).days/365
    
    return age


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Data Processing For Table +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#												Updates the FamDic and IndDic processing the data from GEDCOM file											
#														*** Please DO NOT Disturb this Section ***

lin = 0
with open(r'Project01.ged', 'r') as f:

	d = {}
	for line in f:
		info = line.split()
		level = info[0]
		tag = info[1]
		
		if "@" in tag:
			tag = info[2]
			if tag == "INDI":
				IID = info[1].strip("@")
				if len(IID)<3:
					IID = IID[0]+"0"+IID[1:]
				IndRef.append(IID)
				IndDic[IID]={}
				birthcount = 0
				
			else:
				FID = info[1].strip("@")
				if len(FID)<3:
					FID = FID[0]+"0"+FID[1:]
				FamRef.append(FID)
				FamDic[FID]={}
		
		if Validation(tag) == True:
			if tag == 'HEAD':
				pass
			elif tag == 'TRLR':
				pass
			elif tag == 'NOTE':
				pass
			elif tag == "DATE" and level == "2":
				 if IndDic[IID].get("BIRT","N/A") != "N/A" and birthcount == 0:
				 	IndDic[IID]["BIRT"] = " ".join(info[2:])
				 	IndDic[IID]["AGE"] = Age(" ".join(info[2:]),"N/A")
				 	IndDic[IID]["Alive"] = "TRUE" 
				 	birthcount = 1
				 	
				 elif IndDic[IID].get("DEAT","N/A") != "N/A" and birthcount == 1:
				 	IndDic[IID]["DEAT"] = " ".join(info[2:])
				 	IndDic[IID]["AGE"] = Age(IndDic[IID]["BIRT"]," ".join(info[2:]))
				 	IndDic[IID]["Alive"] = "FALSE" 
				 	birthcount = 2

				 elif FamDic[FID].get("MARR","N/A") != "N/A":
				 	FamDic[FID]["MARR"] = " ".join(info[2:])
			elif tag == "FAMS":
				if IndDic[IID].get("Spouse","N/A") == "N/A":
					IndDic[IID]["Spouse"] = [(" ".join(info[2:])).strip("@")]
				else:
					IndDic[IID]["Spouse"].append((" ".join(info[2:])).strip("@"))
			elif tag == "FAMC":
			    IndDic[IID]["Child"] = (" ".join(info[2:])).strip("@")
			elif tag == "HUSB":
				idd = (" ".join(info[2:])).strip("@")
				if len(idd)<3:
					idd = idd[0]+"0"+idd[1:]
				FamDic[FID]["HUSB"] = idd
			elif tag == "WIFE":
				idd = (" ".join(info[2:])).strip("@")
				if len(idd)<3:
					idd = idd[0]+"0"+idd[1:]
				FamDic[FID]["WIFE"] = idd

			elif tag == "CHIL":
				idd = (" ".join(info[2:])).strip("@")
				if len(idd)<3:
					idd = idd[0]+"0"+idd[1:]

				if FamDic[FID].get("CHIL","N/A") == "N/A":
					FamDic[FID]["CHIL"] = [idd]
				else:
					FamDic[FID]["CHIL"].append(idd)
			elif tag in ITagList :
				 IndDic[IID][tag] = " ".join(info[2:])
			elif tag in FTagList:
				 FamDic[FID][tag] = " ".join(info[2:])
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#																	USER STORIES 

#=================================================================================================================================================================================================================================================================================================

""" 
Functions to call User Stories created by Bharath
		US08 - Birth before Marriage of Parents
		US09 - Birth before Death of Parents
"""
def US_08():
	for x in FamRef:
		CHIL = FamDic[x].get("CHIL",[])
		MARR = FamDic[x]["MARR"]
		DIV = (FamDic[x]).get("DIV","N/A")
		for i in CHIL:
			out = US08.US08(MARR,IndDic[i]["BIRT"],DIV)
			if out == "FalseBefore":
				print "ANOMALY: FAMILY: US08: "+x+": Child "+i+" born "+IndDic[i]["BIRT"]+" before marriage on "+ MARR
			elif out == "FalseAfter":
				print "ANOMALY: FAMILY: US08: "+x+": Child "+i+" born "+IndDic[i]["BIRT"]+" after divorce on "+ DIV
			
def US_09():
	for x in FamRef:
		MOM_Death = (IndDic[FamDic[x]["WIFE"]]).get("DEAT","N/A")
		DAD_Death = (IndDic[FamDic[x]["HUSB"]]).get("DEAT","N/A")
		CHIL = FamDic[x].get("CHIL",[])
		for i in CHIL:
			out = US09.US09(MOM_Death,DAD_Death,IndDic[i]["BIRT"])
			if out == "FalseDad":
				print "ANOMALY: FAMILY: US09: "+x+": Child "+i+" born "+IndDic[i]["BIRT"]+" after father's death (after 9 months) on "+ DAD_Death
			elif out == "FalseMom":
				print "ANOMALY: FAMILY: US09: "+x+": Child "+i+" born "+IndDic[i]["BIRT"]+" after mother's death on "+ MOM_Death		


#=========================================================================================================================================

""" 
Functions to call User Stories created by Sawyer
		US01 - Dates before current date
		US07 - Less than 150 years old
"""
def US_01():
    
    for x in IndRef:
        birth_date = IndDic[x].get("BIRT", "N/A")
        death_date = IndDic[x].get("DEAT", "N/A")
        person = IndDic[x].get("NAME",[])
        for i in person:
            out = US01.US01(birth_date, death_date)
            if out == "False Birth":
                print ("ERROR: INDIVIDUAL: US01: "+x+": The date of birth, " + birth_date +", occurs in the future")
            if out == "False Death":
                print ("ERROR: INDIVIDUAL: US01: "+x+": The date of death, " + death_date +", occurs in the future")
    for y in FamRef:
        marr_date = FamDic[y].get("MARR", "N/A")
        div_date = FamDic[y].get("DIV", "N/A")
        fam = FamDic[y].get("ID",[])
        for f in fam:
            out = US01.US01(marr_date, div_date)
            if out == "False Marr":
                print ("ERROR: FAMILY: US01: "+y+": The date of marriage, " + marr_date +", occurs in the future")
            if out == "False Div":
                print ("ERROR: FAMILY: US01: "+y+" The date of divorce, " + div_date +", occurs in the future")
            else:
                None
def US_07():
    for x in IndRef:
        birth_date = IndDic[x].get("BIRT", "N/A")
        death_date = IndDic[x].get("DEAT", "N/A")
        person = IndDic[x].get("NAME",[])
        for i in person:
            out = US07.US07(birth_date, death_date)
            if out == False:
                print("ERROR: INDIVIDUAL: US07: "+x+": Individual is older than 150 years old")
            else:
                None

#=========================================================================================================================================
""" 
Functions to call User Stories created by Houston
		US23 - Unique name and birth date
		US16 - Male last name
"""

"""
imported user stories at the top of this program"""

def US_23():
	for i in FamRef:
		HUSB = IndDic[FamDic[i]["HUSB"]]["NAME"]
		CHIL = FamDic[i].get("CHIL","N/A")
		US23.US_23(HUSB,CHIL)

def US_16():
	US16.US_16(IndDic)
#=================================================================================================================================================================================================================================================================================================

#																				MAIN SECTION


if __name__ == '__main__':

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++  TABLE CREATION  +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	ID,Name,Gender,Birthday,Age,Alive,Death,Child,Spouse = 3,0,0,0,0,0,0,0,0
	for i in IndDic.values():
		Name     = max(Name, len(i["NAME"])) 
		Gender   = max(Gender, len(i["SEX"])) 
		Birthday = max(Birthday, len(i["BIRT"])) 
		Age      = max(Age, len(i["AGE"])) 
		Alive    = max(Alive, len(i["Alive"]))  
		Death    = max(Death, len(i.get("DEAT",""))) 
		Child    = max(Child, len(i.get("Child",""))*7)
		Spouse   = max(Spouse, len(i.get("Spouse",""))*7)  


	print "INDIVIDUAL DATABASE: \n"
	print "+"+"-"*(ID+2)+"+"+"-"*(Name+2)+"+"+"-"*(Gender+7)+"+"+"-"*(Birthday+2)+"+"+"-"*(Age+3)+"+"+"-"*(Alive+2)+"+"+"-"*(Death+2)+"+"+"-"*(Child-4)+"+"+"-"*(Spouse+5)+"+"
	print "| {:<3} | {:<17} | {:<6} | {:<11} | {:<3} | {:<5} | {:<11} | {:<8} | {:<17} |".format("ID","Name","Gender","Birthday","Age","Alive","Death","Child","Spouse")
	print "+"+"-"*(ID+2)+"+"+"-"*(Name+2)+"+"+"-"*(Gender+7)+"+"+"-"*(Birthday+2)+"+"+"-"*(Age+3)+"+"+"-"*(Alive+2)+"+"+"-"*(Death+2)+"+"+"-"*(Child-4)+"+"+"-"*(Spouse+5)+"+"
	for x in IndRef:
	    print "| {:<3} | {:<17} | {:<6} | {:<11} | {:<3} | {:<5} | {:<11} | {:<8} | {:<17} |".format(x,IndDic[x]["NAME"],IndDic[x]["SEX"],IndDic[x]["BIRT"],IndDic[x]["AGE"],IndDic[x]["Alive"],IndDic[x].get("DEAT","N/A"),IndDic[x].get("Child","None"),IndDic[x].get("Spouse","N/A"))
	print "+"+"-"*(ID+2)+"+"+"-"*(Name+2)+"+"+"-"*(Gender+7)+"+"+"-"*(Birthday+2)+"+"+"-"*(Age+3)+"+"+"-"*(Alive+2)+"+"+"-"*(Death+2)+"+"+"-"*(Child-4)+"+"+"-"*(Spouse+5)+"+"

	print "\n\n\n"
	print "FAMILY DATABASE: \n"
	ID,Married,Divorced,HusbandID,HusbandName,WifeID,WifeName,Children = 3,0,0,0,0,0,0,0
	print "+"+"-"*5+"+"+"-"*13+"+"+"-"*10+"+"+"-"*12+"+"+"-"*19+"+"+"-"*9+"+"+"-"*19+"+"+"-"*24+"+"
	print "| {:<3} | {:<11} | {:<8} | {:<10} | {:<17} | {:<7} | {:<17} | {:<22} |".format("ID","Married","Divorced","Husband ID","Husband Name","Wife ID","Wife Name","Children")
	print "+"+"-"*5+"+"+"-"*13+"+"+"-"*10+"+"+"-"*12+"+"+"-"*19+"+"+"-"*9+"+"+"-"*19+"+"+"-"*24+"+"
	for x in FamRef:
	    print "| {:<3} | {:<11} | {:<8} | {:<10} | {:<17} | {:<7} | {:<17} | {:<22} |".format(x,FamDic[x]["MARR"],(FamDic[x]).get("DIV","N/A"),FamDic[x]["HUSB"],IndDic[FamDic[x]["HUSB"]]["NAME"],FamDic[x]["WIFE"],IndDic[FamDic[x]["WIFE"]]["NAME"],(FamDic[x]).get("CHIL","N/A"))
	print "+"+"-"*5+"+"+"-"*13+"+"+"-"*10+"+"+"-"*12+"+"+"-"*19+"+"+"-"*9+"+"+"-"*19+"+"+"-"*24+"+"

	print "\n\n\n"
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	
	#================ << SPRINT 1 >> ================
	US_08() #BK
	US_09() #BK
        US_01() #SC
	US_07() #SC
	US_23() #HM
	US_16() #HM
