import US08

def US06(HUSB_death = "N/A", WIFE_death = "N/A", DIV = "N/A"):

	if DIV != "N/A":	

		div = US08.DetAge(DIV)

		if HUSB_death == "N/A" and WIFE_death  == "N/A":
			return []

		elif HUSB_death == "N/A" and WIFE_death  != "N/A":
			wife = US08.DetAge(WIFE_death)
			if wife[0] > div[0]:
				return ["FalseWife"]
			elif wife[0] == div[0]:
				if wife[1] >div[1]:
					return ["FalseWife"]
				elif wife[1] == div[1] and wife[2] > div[2]:
					return ["FalseWife"]
			return []
			


		elif HUSB_death != "N/A" and WIFE_death  == "N/A":
			husb = US08.DetAge(HUSB_death)
			if husb[0] > div[0]:
				return ["FalseHusb"]
			elif husb[0] == div[0]:
				if husb[1] >div[1]:
					return ["FalseHusb"]
				elif husb[1] == div[1] and husb[2] > div[2]:
					return ["FalseHusb"]
			return []
			
		elif HUSB_death != "N/A" and WIFE_death  != "N/A":
			husb = US08.DetAge(HUSB_death)
			wife = US08.DetAge(WIFE_death)
			err = []
			husbflag,wifeflag = 0,0

			if wife[0] > div[0] and wifeflag != 1:
				err.append("FalseWife")
				wifeflag = 1
			elif wife[0] == div[0] and wifeflag != 1:
				if wife[1] >div[1]:
					err.append("FalseWife")
					wifeflag = 1
				elif wife[1] == div[1] and wife[2] > div[2]:
					err.append("FalseWife")
					wifeflag = 1
			else:
				pass

			if husb[0] > div[0] and husbflag != 1:
				err.append("FalseHusb")
				husbflag = 1
			elif husb[0] == div[0]  and husbflag != 1:
				if husb[1] >div[1]:
					err.append("FalseHusb")
					husbflag = 1
				elif husb[1] == div[1] and husb[2] > div[2]:
					err.append("FalseHusb")
					husbflag = 1
			else:
				pass
			return err		
	else:
		return []

hd = "13 SEP 1978"
wd = "13 NOV 1970"
d =  "7 FEB 1984"
print US06(hd,wd,d)