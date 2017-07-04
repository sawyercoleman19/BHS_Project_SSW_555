import US06

"""
$ Test-first tool : PyTest

Case 1: Not Divorced ==> True
Case 2: Divorced
		Case 1: Both Husband and Wife Alive ==> True
		Case 2: Husband Alive but Wife Died 
				Case 1: Divoreced before Death of Wife ==> True
				Case 2: Divoreced on Death of Wife ==> True
				Case 3: Divorced After Death of Wife ==> False
		Case 3: Husband Died but Wife Alive
				Case 1: Divoreced before Death of Husband ==> True
				Case 2: Divoreced on Death of Husband ==> True
				Case 3: Divorced After Death of Husband ==> False
		Case 4: Both Husband and Wife Died
				Case 1: Husband Died before Wife Died
					Case 1: Divoreced before Death of Husband ==> True
					Case 2: Divoreced between Death of Husband and Wife ==> False
					Case 3: Divorced After Death of Wife ==> False
				Case 2: Husband Died After Wife Died
					Case 1: Divoreced before Death of Wife ==> True   
					Case 2: Divoreced between Death of Husband and Wife ==> False 
					Case 3: Divorced After Death of Husband ==> False
				Case 3: Husband and Wife Died on same Day
					Case 1: Divoreced before Death of both ==> True
					Case 2: Divoreced on Death of both ==> True
					Case 3: Divorced After Death of both ==> False

Let us Assume Child Birth Date is constant: 05 June 1995

Case 1:    DIV = N/A ==> []
Case 21:   DIV = 06 JUN 1995 HUBS = N/A WIFE = N/A  ==> []
Case 221:  DIV = 06 JUN 1995 HUBS = N/A WIFE = 05 MAY 1998  ==> []
Case 222:  DIV = 06 JUN 1995 HUBS = N/A WIFE = 06 JUN 1995  ==> []
Case 223:  DIV = 06 JUN 1995 HUBS = N/A WIFE = 12 OCT 1993  ==> [FalseWife]
Case 231:  DIV = 06 JUN 1995 HUBS = 15 MAY 1999 WIFE = N/A   ==> []
Case 232:  DIV = 06 JUN 1995 HUBS = 06 JUN 1995 WIFE = N/A   ==> []
Case 233:  DIV = 06 JUN 1995 HUBS = 22 OCT 1991 WIFE = N/A   ==> [FalseHusb]
Case 2411: DIV = 06 JUN 1995 HUBS = 27 DEC 1999 WIFE = 03 MAR 2000   ==> []
Case 2412: DIV = 06 JUN 1995 HUBS = 01 MAR 1994 WIFE = 09 SEP 1998  ==> [FalseHusb]
Case 2413: DIV = 06 JUN 1995 HUBS = 17 JUL 1991 WIFE = 02 AUG 1992  ==> [FalseWife,FalseHusb]
Case 2421: DIV = 06 JUN 1995 HUBS = 03 MAR 2000 WIFE = 27 DEC 1999  ==> []
Case 2422: DIV = 06 JUN 1995 HUBS = 09 SEP 1998 WIFE = 01 MAR 1994  ==> [FalseWife]
Case 2423: DIV = 06 JUN 1995 HUBS = 02 AUG 1992 WIFE = 17 JUL 1991  ==> [FalseWife,FalseHusb]
Case 2431: DIV = 06 JUN 1995 HUBS = 12 NOV 1998 WIFE = 12 NOV 1998  ==> []
Case 2432: DIV = 06 JUN 1995 HUBS = 06 JUN 1995 WIFE = 06 JUN 1995  ==> []
Case 2433: DIV = 06 JUN 1995 HUBS = 30 APR 1990 WIFE = 30 APR 1990  ==> [FalseWife,FalseHusb]

"""

def test_US06_Case1():
	Case1 = US06.US06("N/A","N/A","N/A")
	assert Case1 == []

def test_US06_Case21():
	Case21 = US06.US06("N/A","N/A","06 JUN 1995")
	assert Case21 == []

def test_US06_Case221():
	Case221 = US06.US06("N/A","05 MAY 1998","06 JUN 1995")
	assert Case221 == []

def test_US06_Case222():
	Case222 = US06.US06("N/A","06 JUN 1995","06 JUN 1995")
	assert Case222 == []

def test_US06_Case223():
	Case223 = US06.US06("N/A","12 OCT 1993","06 JUN 1995")
	assert Case223 == ["FalseWife"]

def test_US06_Case231():
	Case231 = US06.US06("15 MAY 1999","N/A","06 JUN 1995")
	assert Case231 == []

def test_US06_Case232():
	Case232 = US06.US06("06 JUN 1995","N/A","06 JUN 1995")
	assert Case232 == []

def test_US06_Case233():
	Case233 = US06.US06("22 OCT 1991","N/A","06 JUN 1995")
	assert Case233 == ["FalseHusb"]

def test_US06_Case2411():
	Case2411 = US06.US06("27 DEC 1999","03 MAR 2000","06 JUN 1995")
	assert Case2411 == []

def test_US06_Case2412():
	Case2412 = US06.US06("01 MAR 1994","09 SEP 1998","06 JUN 1995")
	assert Case2412 == ["FalseHusb"]

def test_US06_Case2413():
	Case2413 = US06.US06("17 JUL 1991","02 AUG 1992","06 JUN 1995")
	assert Case2413 == ["FalseWife","FalseHusb"]

def test_US06_Case2421():
	Case2421 = US06.US06("03 MAR 2000","27 DEC 1999","06 JUN 1995")
	assert Case2421 == []

def test_US06_Case2422():
	Case2422 = US06.US06("09 SEP 1998","01 MAR 1994","06 JUN 1995")
	assert Case2422 == ["FalseWife"]

def test_US06_Case2423():
	Case2423 = US06.US06("02 AUG 1992","17 JUL 1991","06 JUN 1995")
	assert Case2423 == ["FalseWife","FalseHusb"]

def test_US06_Case2431():
	Case2431 = US06.US06("12 NOV 1998","12 NOV 1998","06 JUN 1995")
	assert Case2431 == []

def test_US06_Case2432():
	Case2432 = US06.US06("06 JUN 1995","06 JUN 1995","06 JUN 1995")
	assert Case2432 == []

def test_US06_Case2433():
	Case2433 = US06.US06("30 APR 1990","30 APR 1990","06 JUN 1995")
	assert Case2433 == ["FalseWife","FalseHusb"]

