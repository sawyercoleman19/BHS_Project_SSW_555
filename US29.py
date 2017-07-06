#US29 List Deceased


def US29(IndDic):
	deathList = []
	for a in IndDic:
		if IndDic[a].get("DEAT","N/A") == "N/A":
			pass
		else:
			deathList.append("ID: "+a+" Name: "+IndDic[a]["NAME"])

	print "RESULT: INDIVIDUAL: US29: List of Individuals Deceased: {}".format(deathList)

    
    #add id, name and death dtae to output
            
            
