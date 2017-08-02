import BHS_555 as db
def US15(FamDic):
	famID = FamDic.keys()
	for x in famID:
		if len((FamDic[x]).get("CHIL","N/A"))>15:
			return x