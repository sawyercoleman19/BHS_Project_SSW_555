import US12

"""
$ Test-first tool : PyTest

Case 1: Diff between Mom and child is less than 60
		Case 11: Diff between Dad and Child is less than 80 ==> True
		Case 12: Diff between Dad and Child is equal to 80 ==> False
		Case 13: Diff between Dad and Child is greater than 80 ==> False
Case 2: Diff between Mom and child is equal to 60
		Case 21: Diff between Dad and Child is less than 80 ==> False
		Case 22: Diff between Dad and Child is equal to 80 ==> False
		Case 23: Diff between Dad and Child is greater than 80 ==> False
Case 3: Diff between Mom and child is greater than 60
		Case 31: Diff between Dad and Child is less than 80 ==> False
		Case 32: Diff between Dad and Child is equal to 80 ==> False
		Case 33: Diff between Dad and Child is greater than 80 ==> False

Let us Assume Child Birth Date is constant: 05 June 1995

Case 11: MOM 15 MAY 1980  DAD 20 MAR 1972  ==> []        
Case 12: MOM 15 MAY 1980  DAD 07 JUN 1915  ==> [DAD]    
Case 13: MOM 15 MAY 1980  DAD 05 JUN 1905  ==> [DAD]     
Case 21: MOM 05 JUN 1935  DAD 20 MAR 1972  ==> [MOM]     
Case 22: MOM 05 JUN 1935  DAD 07 JUN 1915  ==> [MOM,DAD]
Case 23: MOM 05 JUN 1935  DAD 05 JUN 1905  ==> [MOM,DAD]
Case 31: MOM 03 SEP 1904  DAD 20 MAR 1972  ==> [MOM]     
Case 32: MOM 03 SEP 1904  DAD 07 JUN 1915  ==> [MOM,DAD]
Case 33: MOM 03 SEP 1904  DAD 05 JUN 1905  ==> [MOM,DAD]
"""

def test_US12_Case11():
	Case11 = US12.US12("15 MAY 1980","20 MAR 1972","05 JUN 1995")
	assert Case11 == []       
def test_US12_Case12():
	Case12 = US12.US12("15 MAY 1980","07 JUN 1915","05 JUN 1995")
	assert Case12 == ["DAD"]    
def test_US12_Case13():
	Case13 = US12.US12("15 MAY 1980","05 JUN 1905","05 JUN 1995")
	assert Case13 == ["DAD"]    
def test_US12_Case21():
	Case21 = US12.US12("05 JUN 1935","20 MAR 1972","05 JUN 1995")
	assert Case21 == ["MOM"]    
def test_US12_Case22():
	Case22 = US12.US12("05 JUN 1935","07 JUN 1915","05 JUN 1995")
	assert Case22 == ["MOM","DAD"]
def test_US12_Case23():
	Case23 = US12.US12("05 JUN 1935","05 JUN 1905","05 JUN 1995")
	assert Case23 == ["MOM","DAD"]
def test_US12_Case31():
	Case31 = US12.US12("03 SEP 1904","20 MAR 1972","05 JUN 1995")
	assert Case31 == ["MOM"]    
def test_US12_Case32():
	Case32 = US12.US12("03 SEP 1904","07 JUN 1915","05 JUN 1995")
	assert Case32 == ["MOM","DAD"]
def test_US12_Case33():
	Case33 = US12.US12("03 SEP 1904","05 JUN 1905","05 JUN 1995")
	assert Case33 == ["MOM","DAD"]
