def US18(IndDic, FamDic):

	for fam in FamDic:
		husbid = FamDic.get["HUSB", "N/A"]
		wifeid = FamDic.get["WIFE", "N/A"]

		if husbid == "N/A" or wifeid == "N/A":
			pass
		else:
			husbFam = IndDic[husbid].get["CHILD", "N/A"]
			wifeFam = IndDic[wifeid].get["CHILD", "N/A"]



			if husbFam == wifeFam and husbFam != "N/A":
				print "Error: Family: US18: Family ", fam, " has a husband and wife who are siblings."
			else:
				pass
