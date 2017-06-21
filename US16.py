def US_16(IndDic):
	Indref = IndDic.keys()
	IndName = []
	Birth = []
	for a in Indref:
		IndName.append(IndDic[a]["NAME"])
		Birth.append(IndDic[a]["BIRT"])

	namelist = {}
	for i in Indref:
		namelist[i] = IndDic[i]["NAME"]

	if len(IndName) != len(set(IndName)):
		for p in range(len(IndName)):
			ql = IndName[0:p]+IndName[p+1:]
			for q in ql :
				if IndName[p] == q and Birth[p] == Birth[ql.index(q)]:
					print "Error: INDIVIDUAL: US16: " + namelist.keys()[namelist.values().index(IndName[p])] + ": The Individual "+namelist.keys()[namelist.values().index(IndName[p])]+" is sharing the Same Name \""+IndName[p]+"\" and Date of Birth \""+Birth[p] +"\" with another individual"
