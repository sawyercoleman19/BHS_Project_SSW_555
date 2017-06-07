'''
BHS_555

SSW 555 - Agile Methods for Software Development

Team Members:
	Bharath Kumar
	Sawyer Coleman
	Houston Migdon
'''

import datetime

IndDic = {}
FamDic = {}
IndRef = []
FamRef = []

TagList = ['INDI', 'NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'FAM', 'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV', 'DATE', 'HEAD', 'TRLR', 'NOTE']
ITagList = ['NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS']
FTagList = ['MARR', 'HUSB', 'WIFE', 'CHIL','DIV']

INDIframe = ["ID","Name","Gender","Birthday","Age","Alive","Death","Child","Spouse"]
FAMframe = ["ID","Married","Divorced","Husband ID","Husband Name","Wife ID","Wife Name","Children"]

def Validation(tag):
	if tag in TagList:
		# print True
		return True
	else:
		# print False
		return False

def Age(BIRT, DEAT):
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

lin = 0
with open(r'Project01.ged', 'r') as f:

	d = {}
	for line in f:
		# lin += 1
		# print lin
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
			# print "\n\n\n\n"
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
