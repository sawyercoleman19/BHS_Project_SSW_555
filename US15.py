#US15 make sure every indiv has no more than 15 siblings
def US_15(FamDic):
	famID = FamDic.keys() """a list of all families"""
	for x in famID:
		if len(FamDic[x].get("CHIL","N/A")) > 16:
			print "Error in US 15: There are too many children in family " + x
		else:
			pass



