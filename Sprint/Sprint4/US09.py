'''
    Bharath Kumar
    US06 Functions File
    SSW_555_Agile_Methods
    BHS_Project_SSW_555
    Sprint 1 
    '''
import datetime
import US08

def US09(MOM, DAD ,CHIL_BIRT): #Child should be born before death of mother and before 9 months after death of father

	if MOM == "N/A":
		if DAD == "N/A":
			return True
		else:
			DADAGE = US08.DetAge(DAD)
			CHIL_BIRT_AGE = US08.DetAge(CHIL_BIRT)

			if DADAGE[0] - CHIL_BIRT_AGE[0] < 0:
				return True
			elif DADAGE[0] - CHIL_BIRT_AGE[0] == 0 and DADAGE[1] - CHIL_BIRT_AGE[1] < 9:
				return True
			else:
				return "FalseDad"
	else:
		MOMAGE = US08.DetAge(MOM)
		if DAD != "N/A":
			DADAGE = US08.DetAge(DAD)
		else:
			DADAGE = [0,0,0]
		CHIL_BIRT_AGE = US08.DetAge(CHIL_BIRT)
		if MOMAGE[0] - CHIL_BIRT_AGE[0] < 0:
			if DADAGE[0] - CHIL_BIRT_AGE[0] < 0:
				return True
			elif DADAGE[0] - CHIL_BIRT_AGE[0] == 0 and DADAGE[1] - CHIL_BIRT_AGE[1] < 9:
				return True
			else:
				return "FalseDad"
		elif MOMAGE[0] - CHIL_BIRT_AGE[0] == 0:
			if MOMAGE[1] - CHIL_BIRT_AGE[1] < 0:
				if DADAGE[0] - CHIL_BIRT_AGE[0] < 0:
					return True
				elif DADAGE[0] - CHIL_BIRT_AGE[0] == 0 and DADAGE[1] - CHIL_BIRT_AGE[1] < 9:
					return True
				else:
					return "FalseDad"
			elif MOMAGE[1] - CHIL_BIRT_AGE[1] == 0 and MOMAGE[2] - CHIL_BIRT_AGE[2] <= 0:
				if DADAGE[0] - CHIL_BIRT_AGE[0] < 0:
					return True
				elif DADAGE[0] - CHIL_BIRT_AGE[0] == 0 and DADAGE[1] - CHIL_BIRT_AGE[1] < 9:
					return True
				else:
					return "FalseDad"
			else:
				return "FalseMom"
		else:
			return "FalseMom"

