'''
    Bharath Kumar
    US35 Functions File
    SSW_555_Agile_Methods
    BHS_Project_SSW_555
    Sprint 3
    '''

import usefulFunctions as fun

def US35(BirthDic):
	Tframe = fun.TimeDelta(-30)
	error = []
	for i,j in zip(BirthDic.values(),BirthDic.keys()):
		if i != "N/A":
			bir = i.split(" ")[::-1]
			bir[1] = fun.MonthInNum(bir[1])
			if fun.NoDays(int(bir[0]),int(bir[1]),int(bir[2])) != False:
				dayz = (fun.NoDays(int(bir[0]),int(bir[1]),int(bir[2])))*(-1)
				if dayz <= 30:
					error.append(j)
	return error