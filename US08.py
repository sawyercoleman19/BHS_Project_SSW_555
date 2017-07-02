import datetime

def leapyear (year):

	if (year % 4) == 0:
	   if (year % 100) == 0:
	       if (year % 400) == 0:
	           return True
	       else:
	           return False
	   else:
	       return True
	else:
	   return False


def DetAge(BIRT):
	months = {"JAN": "01","FEB":"02" ,"MAR": "03","APR": "04","MAY": "05","JUN": "06","JUL": "07","AUG":"08","SEP": "09","OCT": "10","NOV": "11","DEC": "12" }
	today = datetime.date.today()
	tod = str(today).split("-")
	bir = BIRT.split(" ")[::-1]
	bir[1] = months[bir[1]]
	
	ageflag = 0
	age = int(tod[0])-int(bir[0])
	mon = int(tod[1])-int(bir[1])
	day = int(tod[2])-int(bir[2])

	if mon < 0:
		mon = 12 + mon
		ageflag = 1

	if day < 0:
		if mon != 0:
			mon -= 1

		if int(tod[1])%2 == 0:
			day = 31 + day
		elif tod[1] != "03":
			day = 30 + day
		elif leapyear(int(tod[0])):
			day = 29 + day
		else:
			day = 28 + day

		if int(tod[1]) == int(bir[1]) and int(tod[2]) < int(bir[2]):
			ageflag = 1

	if ageflag != 0:
		age -= 1
	compage = [age, mon, day]
	return compage


def US08(MARR,CHIL_BIRT,DIV="N/A"):
	if DIV == "N/A":
		MARR_AGE = DetAge(MARR)
		CHIL_BIRT_AGE = DetAge(CHIL_BIRT)

		if MARR_AGE[0] - CHIL_BIRT_AGE[0] <0:
			return "FalseBefore"
		elif MARR_AGE[0] - CHIL_BIRT_AGE[0] == 0 and MARR_AGE[1] - CHIL_BIRT_AGE[1] < 9:
			return "FalseBefore"
		else:
			return True

	else:
		DIV_AGE = DetAge(DIV)
		MARR_AGE = DetAge(MARR)
		CHIL_BIRT_AGE = DetAge(CHIL_BIRT)

		if MARR_AGE[0] - CHIL_BIRT_AGE[0] <0:
			return "FalseBefore"
		elif MARR_AGE[0] - CHIL_BIRT_AGE[0] == 0 and MARR_AGE[1] - CHIL_BIRT_AGE[1] < 9:
			return "FalseBefore"
		elif DIV_AGE[0] - CHIL_BIRT_AGE[0] > 0:
			return "FalseAfter"
		elif DIV_AGE[0] - CHIL_BIRT_AGE[0] == 0 and DIV_AGE[1] - CHIL_BIRT_AGE[1] < 9:
			return "FalseAfter"
		else:
			return True
