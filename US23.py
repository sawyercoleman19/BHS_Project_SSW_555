import BHS_555 as db

def US_23(HUSB, CHIL):
	''' user story 23 from Houston, make sure all male members of a family have the same last name'''
	if CHIL != "N/A":
		male_Child = maleChild(CHIL)
	else:
		male_Child = "N/A"

	if HUSB != "N/A":
		fatherLast = HUSB.split("/")[1]
	elif male_Child != "N/A" and len(male_Child)>0:
		fatherLast = male_Child[0].split("/")[1]

	if male_Child != "N/A" and len(male_Child)>0:
		
		for x in male_Child:
			chilLast = x.split("/")[1]
			#print chilLast, fatherLast
			if fatherLast != chilLast:
				print "Error " + HUSB + "is not father of "+ x

def maleChild(CHIL):
	male_Child = []
	for j in CHIL:
		if db.IndDic[j]["SEX"] == "M":
			#print db.IndDic[j]["NAME"]
			male_Child.append(db.IndDic[j]["NAME"])
	return male_Child
