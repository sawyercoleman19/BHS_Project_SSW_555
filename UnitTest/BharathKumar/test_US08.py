import US08 

"""
Case 1: Marriage Date is more than 9 months before Childs Birth Date 
		Case 11: Not Divorced ==> True
		Case 12: Born after 9 months of Divorce ==> False
		Case 13: Born before 9 months of Divorce ==> True
		Case 14: Born exactly on 9 months of Divorce ==> True
Case 2: Marriage Date is less than 9 months before Childs Birth Date 
		Case 21: Not Divorced ==> False
		Case 22: Born after 9 months of Divorce ==> False 
		Case 23: Born before 9 months of Divorce  ==> False
		Case 24: Born exactly on 9 months of Divorce  ==> False
Case 3: Marriage Date is exactly 9 months before Childs Birth Date 
		Case 31: Not Divorced ==> True
		Case 32: Born after 9 months of Divorce  ==> False
		Case 33: Born before 9 months of Divorce  ==> True
		Case 34: Born exactly on 9 months of Divorce ==> True
Case 4: Marriage Date is after Childs Birth Date 
		Case 41: Not Divorced ==> False
		Case 42: Born after 9 months of Divorce ==> False
		Case 43: Born before 9 months of Divorce ==> False
		Case 44: Born exactly on 9 months of Divorce ==> False
Case 5: Marriage Date is on Childs Birth Date 
		Case 51: Not Divorced ==> False
		Case 52: Born after 9 months of Divorce ==> False
		Case 53: Born before 9 months of Divorce ==> False
		Case 54: Born exactly on 9 months of Divorce ==> False

Let us Assume Child Birth Date is constant: 05 June 1995

Case 11: MARR 03 MAR 1994  DIV N/A         ==> True
Case 12: MARR 03 MAR 1994  DIV 15 JUL 1994 ==> False
Case 13: MARR 03 MAR 1994  DIV 20 APR 1996 ==> True
Case 14: MARR 03 MAR 1994  DIV 27 SEP 1994 ==> True
Case 21: MARR 13 NOV 1994  DIV N/A         ==> False
Case 22: MARR 13 NOV 1994  DIV 15 JUL 1994 ==> False
Case 23: MARR 13 NOV 1994  DIV 20 APR 1996 ==> False
Case 24: MARR 13 NOV 1994  DIV 27 SEP 1994 ==> False
Case 31: MARR 09 SEP 1994  DIV N/A         ==> True
Case 32: MARR 09 SEP 1994  DIV 15 JUL 1994 ==> False
Case 33: MARR 09 SEP 1994  DIV 20 APR 1996 ==> True
Case 34: MARR 09 SEP 1994  DIV 27 SEP 1994 ==> True
Case 41: MARR 09 MAY 1997  DIV N/A         ==> False
Case 42: MARR 09 MAY 1997  DIV 15 JUL 1994 ==> False
Case 43: MARR 09 MAY 1997  DIV 20 APR 1996 ==> False
Case 44: MARR 09 MAY 1997  DIV 27 SEP 1994 ==> False
Case 51: MARR 05 JUN 1995  DIV N/A         ==> False
Case 52: MARR 05 JUN 1995  DIV 15 JUL 1994 ==> False
Case 53: MARR 05 JUN 1995  DIV 20 APR 1996 ==> False
Case 54: MARR 05 JUN 1995  DIV 27 SEP 1994 ==> False
"""

def test_US08_Case11():
	Case11 = US08.US08("03 MAR 1994","05 JUN 1995")
	assert Case11 == True
def test_US08_Case12():
	Case12 = US08.US08("03 MAR 1994","05 JUN 1995","15 JUL 1994")
	assert Case12 == False
def test_US08_Case13():
	Case13 = US08.US08("03 MAR 1994","05 JUN 1995","20 APR 1996")
	assert Case13 == True
def test_US08_Case14():
	Case14 = US08.US08("03 MAR 1994","05 JUN 1995","27 SEP 1994")
	assert Case14 == True
def test_US08_Case21():
	Case21 = US08.US08("13 NOV 1994","05 JUN 1995")
	assert Case21 == False
def test_US08_Case22():
	Case22 = US08.US08("13 NOV 1994","05 JUN 1995","15 JUL 1994")
	assert Case22 == False
def test_US08_Case23():
	Case23 = US08.US08("13 NOV 1994","05 JUN 1995","20 APR 1996")
	assert Case23 == False
def test_US08_Case24():
	Case24 = US08.US08("13 NOV 1994","05 JUN 1995","27 SEP 1994")
	assert Case24 == False
def test_US08_Case31():
	Case31 = US08.US08("09 SEP 1994","05 JUN 1995")
	assert Case31 == True
def test_US08_Case32():
	Case32 = US08.US08("09 SEP 1994","05 JUN 1995","15 JUL 1994")
	assert Case32 == False
def test_US08_Case33():
	Case33 = US08.US08("09 SEP 1994","05 JUN 1995","20 APR 1996")
	assert Case33 == True
def test_US08_Case34():
	Case34 = US08.US08("09 SEP 1994","05 JUN 1995","27 SEP 1994")
	assert Case34 == True
def test_US08_Case41():
	Case41 = US08.US08("09 MAY 1997","05 JUN 1995")
	assert Case41 == False
def test_US08_Case42():
	Case42 = US08.US08("09 MAY 1997","05 JUN 1995","15 JUL 1994")
	assert Case42 == False
def test_US08_Case43():
	Case43 = US08.US08("09 MAY 1997","05 JUN 1995","20 APR 1996")
	assert Case43 == False
def test_US08_Case44():
	Case44 = US08.US08("09 MAY 1997","05 JUN 1995","27 SEP 1994")
	assert Case44 == False
def test_US08_Case51():
	Case51 = US08.US08("05 JUN 1995","05 JUN 1995")
	assert Case51 == False
def test_US08_Case52():
	Case52 = US08.US08("05 JUN 1995","05 JUN 1995","15 JUL 1994")
	assert Case52 == False
def test_US08_Case53():
	Case53 = US08.US08("05 JUN 1995","05 JUN 1995","20 APR 1996")
	assert Case53 == False
def test_US08_Case54():
	Case54 = US08.US08("05 JUN 1995","05 JUN 1995","27 SEP 1994")
	assert Case54 == False
