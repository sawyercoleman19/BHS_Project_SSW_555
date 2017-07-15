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
import usefulFunctions
import US01, US02, US03, US07
import US06, US08, US09, US12
import US16, US23, US42, US29

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
				marrcount = 0
				
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
				 	IndDic[IID]["AGE"] = usefulFunctions.Age(" ".join(info[2:]),"N/A")
				 	IndDic[IID]["Alive"] = "TRUE" 
				 	birthcount = 1
				 	
				 elif IndDic[IID].get("DEAT","N/A") != "N/A" and birthcount == 1:
				 	IndDic[IID]["DEAT"] = " ".join(info[2:])
				 	IndDic[IID]["AGE"] = usefulFunctions.Age(IndDic[IID]["BIRT"]," ".join(info[2:]))
				 	IndDic[IID]["Alive"] = "FALSE" 
				 	birthcount = 2

				 elif FamDic[FID].get("MARR","N/A") != "N/A":
				 	if FamDic[FID].get("DIV","N/A") != "N/A" and marrcount == 1:
				 		FamDic[FID]["DIV"] = " ".join(info[2:])
				 	else:
				 		FamDic[FID]["MARR"] = " ".join(info[2:])
				 		marrcount =1
				 		


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
# 																SPRINT 1
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

#																SPRINT 2
def US_06():
	for x in FamRef:
		MOM_Death = (IndDic[FamDic[x]["WIFE"]]).get("DEAT","N/A")
		DAD_Death = (IndDic[FamDic[x]["HUSB"]]).get("DEAT","N/A")
		DIV = (FamDic[x]).get("DIV","N/A")
		out = US06.US06(DAD_Death,MOM_Death,DIV)
		for i in out:
			if i == "FalseWife":
				print "ERRPR: FAMILY: US06: "+x+": Wife "+IndDic[FamDic[x]["WIFE"]]["NAME"]+" ("+FamDic[x]["WIFE"]+") Died before Divorce on "+(FamDic[x]).get("DIV","N/A")
			if i == "FalseHusb":
				print "ERROR: FAMILY: US06: "+x+": Husband "+IndDic[FamDic[x]["HUSB"]]["NAME"]+" ("+FamDic[x]["HUSB"]+") Died before Divorce on "+(FamDic[x]).get("DIV","N/A")
			


def US_12():
	for x in FamRef:
		MOM_Birth = (IndDic[FamDic[x]["WIFE"]]).get("BIRT","N/A")
		DAD_Birth = (IndDic[FamDic[x]["HUSB"]]).get("BIRT","N/A")
		CHIL = FamDic[x].get("CHIL",[])
		for i in CHIL:
			out = US12.US12(MOM_Birth,DAD_Birth,IndDic[i]["BIRT"])
			for y in out:
				if y == "MOM":
					print "ANOMALY: FAMILY: US12: "+x+": Mother "+IndDic[FamDic[x]["WIFE"]]["NAME"]+" ("+FamDic[x]["WIFE"]+") is more than 60 years older than the child "+i
				if y == "DAD":
					print "ANOMALY: FAMILY: US12: "+x+": Father "+IndDic[FamDic[x]["HUSB"]]["NAME"]+" ("+FamDic[x]["HUSB"]+") is more than 80 years older than the child "+i
				
#																SPRINT 3
def US_35():
	pass

def US_36():
	pass

#=========================================================================================================================================

""" 
Functions to call User Stories created by Sawyer
		US01 - Dates before current date
		US07 - Less than 150 years old
        US02 - Birthdate before marriage
        US03 - Birthdate before death
"""

# 																SPRINT 1
def US_01():
    
    for x in IndRef:
        birth_date = IndDic[x].get("BIRT", "N/A")
        death_date = IndDic[x].get("DEAT", "N/A")
        person = IndDic[x].get("NAME",[])
        out = US01.US01_ind(birth_date, death_date)
        if out == "False Birth":
            print ("ERROR: INDIVIDUAL: US01: "+x+": The date of birth, " + birth_date +", occurs in the future")
        if out == "False Death":
            print ("ERROR: INDIVIDUAL: US01: "+x+": The date of death, " + death_date +", occurs in the future")
    for y in FamRef:
        marr_date = FamDic[y].get("MARR", "N/A")
        div_date = FamDic[y].get("DIV", "N/A")
        fam = FamDic[y].get("ID",[])
        out = US01.US01_fam(marr_date, div_date)
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
        out = US07.US07(birth_date, death_date)
        if out == False:
            print("ERROR: INDIVIDUAL: US07: "+x+": Individual is older than 150 years old")
        else:
            None

#																SPRINT 2
def US_02():

	for x in FamRef:
		marr_date = FamDic[x].get("MARR", "N/A")
		WIFE_Birth = (IndDic[FamDic[x]["WIFE"]]).get("BIRT","N/A")
		HUSB_Birth = (IndDic[FamDic[x]["HUSB"]]).get("BIRT","N/A")
		out = US02.US02(WIFE_Birth,marr_date)
		if out == False:
			print ("ERROR: INDIVIDUAL: US02: "+FamDic[x]["WIFE"]+": The date of birth, " +WIFE_Birth+ " occurs before marriage, "+ marr_date)
		out = US02.US02(HUSB_Birth,marr_date)
		if out == False:
			print ("ERROR: INDIVIDUAL: US02: "+FamDic[x]["HUSB"]+": The date of birth, " +HUSB_Birth+ " occurs before marriage, "+ marr_date)

def US_03():
    for x in IndRef:
        birth_date = IndDic[x].get("BIRT", "N/A")
        death_date = IndDic[x].get("DEAT", "N/A")
        person = IndDic[x].get("NAME",[])
        out = US03.US03(birth_date, death_date)
        if out == False:
            print ("ERROR: INDIVIDUAL: US03: "+x+": The date of birth, " + birth_date +", occurs after death " + death_date)

#																SPRINT 3
def US_04():
	pass

def US_05():
	pass

#=========================================================================================================================================
""" 
Functions to call User Stories created by Houston
		US23 - Unique name and birth date
		US16 - Male last name
"""

"""
imported user stories at the top of this program"""

# 																SPRINT 1
def US_23():
	for i in FamRef:
		HUSB = IndDic[FamDic[i]["HUSB"]]["NAME"]
		CHIL = FamDic[i].get("CHIL","N/A")
		US23.US_23(HUSB,CHIL)

def US_16():
	US16.US_16(IndDic)

#																SPRINT 2
def US_42():
	for i in IndDic:
		if US42.US42(IndDic[i]["BIRT"]) == False:
			print ("ERROR: INDIVIDUAL: US42: "+i+": Birth Date " + IndDic[i]["BIRT"] + " is invalid.")

		if US42.US42((IndDic[i]).get("DEAT","N/A")) == False:
			print ("ERROR: INDIVIDUAL: US42: "+i+": Death Date " + (IndDic[i]).get("DEAT","N/A") + " is invalid.")


	for f in FamDic:
		if US42.US42(FamDic[f]["MARR"]) == False:
			print ("ERROR: FAMILY: US42: "+f+": Marrige Date " + FamDic[f]["MARR"] + " is invalid.")

		if US42.US42((FamDic[f]).get("DIV","N/A")) == False:
			print ("ERROR: FAMILY: US42: "+f+": Divorce Date " + (FamDic[f]).get("DIV","N/A") + " is invalid.")

def US_29():
	US29.US29(IndDic)

#																SPRINT 3
def US_22():
	pass

def US_15():
	pass
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

	print "\n"
	print "FAMILY DATABASE: \n"
	ID,Married,Divorced,HusbandID,HusbandName,WifeID,WifeName,Children = 3,0,0,0,0,0,0,0
	print "+"+"-"*5+"+"+"-"*13+"+"+"-"*10+"+"+"-"*12+"+"+"-"*19+"+"+"-"*9+"+"+"-"*19+"+"+"-"*24+"+"
	print "| {:<3} | {:<11} | {:<8} | {:<10} | {:<17} | {:<7} | {:<17} | {:<22} |".format("ID","Married","Divorced","Husband ID","Husband Name","Wife ID","Wife Name","Children")
	print "+"+"-"*5+"+"+"-"*13+"+"+"-"*10+"+"+"-"*12+"+"+"-"*19+"+"+"-"*9+"+"+"-"*19+"+"+"-"*24+"+"
	for x in FamRef:
	    print "| {:<3} | {:<11} | {:<8} | {:<10} | {:<17} | {:<7} | {:<17} | {:<22} |".format(x,FamDic[x]["MARR"],(FamDic[x]).get("DIV","N/A"),FamDic[x]["HUSB"],IndDic[FamDic[x]["HUSB"]]["NAME"],FamDic[x]["WIFE"],IndDic[FamDic[x]["WIFE"]]["NAME"],(FamDic[x]).get("CHIL","N/A"))
	print "+"+"-"*5+"+"+"-"*13+"+"+"-"*10+"+"+"-"*12+"+"+"-"*19+"+"+"-"*9+"+"+"-"*19+"+"+"-"*24+"+"

	print "\n"
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	
	#================ << SPRINT 1 >> ================
	US_08() #BK
	US_09() #BK
	US_01() #SC
	US_07() #SC
	US_23() #HM
	US_16() #HM
	

	#================ << SPRINT 2 >> ================
	US_06() #BK
	US_12() #BK
	US_02() #SC
	US_03() #SC
	US_42() #HM
	US_29() #HM


	#================ << SPRINT 3 >> ================
	US_35() #BK
	US_36() #BK
	US_04() #SC
	US_05() #SC
	US_22() #HM
	US_15() #HM
