'''
    Bharath Kumar
    US38 Functions File
    SSW_555_Agile_Methods
    BHS_Project_SSW_555
    Sprint 4
    '''

import usefulFunctions as fun
import datetime

def US38(BirthDic):
	Tframe = fun.TimeDelta(30)
	error = []
	for i,j in zip(BirthDic.values(),BirthDic.keys()):
		if i != "N/A":
			bir = i.split(" ")[::-1]
			bir[1] = fun.MonthInNum(bir[1])
			if fun.NoDays(int(bir[0]),int(bir[1]),int(bir[2])) != False:
				dayz = (fun.NoDays(datetime.date.today().year,int(bir[1]),int(bir[2])))
				if dayz <= 30 and dayz >= 0:
					error.append(j)
	return error
