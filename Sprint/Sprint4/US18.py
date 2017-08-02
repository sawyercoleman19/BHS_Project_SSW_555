def US18(IndDic, FamDic):

	err = []
	for fam in FamDic.keys():

		husbid = FamDic[fam].get("HUSB", "N/A")
		wifeid = FamDic[fam].get("WIFE", "N/A")

		if husbid == "N/A" or wifeid == "N/A":
			pass
		else:
			husbFam = IndDic[husbid].get("Child", "N/A")
			wifeFam = IndDic[wifeid].get("Child", "N/A")

			if husbFam == wifeFam and husbFam != "N/A" and wifeFam != "N/A":
				err.append("Error: Family: US18: Family "+fam+" has a husband and wife who are siblings.")
			else:
				pass
	return err
