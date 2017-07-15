#US29 List Deceased


def US29(IndDic):
	deathList = []
	for a in IndDic:
		if IndDic[a].get("DEAT","N/A") == "N/A":
			pass
		else:
			deathList.append("=> ID: "+a+"  Name: "+IndDic[a]["NAME"])
	if deathList == []:
		print "RESULT: INDIVIDUAL: US29: No Individuals Deceased"
	else:
		print "RESULT: INDIVIDUAL: US29: List of Individuals Deceased: {}".format(deathList[0])
		if len(deathList)>1:
			for i in deathList[1:]:
				print " "*len("RESULT: INDIVIDUAL: US29: List of Individuals Deceased: ")+i

    
    #add id, name and death dtae to output
            
            
