import BHS_555 as db

def US_16(IndDic):
	Indref = IndDic.keys()
	IndName = []
	Birth = []
	for a in Indref:
		IndName.append(IndDic[a]["NAME"])
		Birth.append(IndDic[a]["BIRT"])
	#print IndName

	if len(IndName) != len(set(IndName)):
		for p in range(len(IndName)):
			for q in IndName[0:p]+IndName[p:]:
				if IndName[p] == q and Birth[IndName.index(p)] == Birth[IndName.index(q)]:
					print "Error: There are 2 " + p + "Having Same Date of Birth "+Birth[IndName.index(p)] 
