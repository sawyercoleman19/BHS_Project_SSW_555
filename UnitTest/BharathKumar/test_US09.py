import US09

"""
$ Test-first tool : PyTest

Case 1: MOM Alive
		Case 11: Dad Alive ==> True                                  
		Case 12: Dad Died after childs birth ==> True               
		Case 13: Dad Died on the day if childs birth ==> True             
		Case 14: Dad Died before 9 months of childs birth ==> False 
		Case 15: Born exactly on 9 months of Divorce ==> False       
Case 2: MOM Died on Birth day of child  
		Case 21: Dad Alive ==> True                                       
		Case 22: Dad Died after childs birth ==> True                    
		Case 23: Dad Died on the day if childs birth ==> True                      
		Case 24: Dad Died before 9 months of childs birth ==> False             
		Case 25: Born exactly on 9 months of Divorce ==> False       
Case 3: MOM Died before child born
		Case 31: Dad Alive ==> False                                
		Case 32: Dad Died after childs birth ==> False                    
		Case 33: Dad Died on the day if childs birth ==> False                      
		Case 34: Dad Died before 9 months of childs birth ==> False                 
  		Case 35: Born exactly on 9 months of Divorce ==> False

Let us Assume Child Birth Date is constant: 05 June 1995

Case 11: MOM N/A          DAD N/A          ==> True
Case 12: MOM N/A          DAD 07 JUL 1996  ==> True
Case 13: MOM N/A          DAD 05 JUN 1995  ==> True
Case 14: MOM N/A          DAD 04 APR 1993  ==> FalseDad
Case 15: MOM N/A          DAD 06 SEP 1994  ==> FalseDad
Case 21: MOM 05 JUN 1995  DAD N/A          ==> True
Case 22: MOM 05 JUN 1995  DAD 07 JUL 1996  ==> True
Case 23: MOM 05 JUN 1995  DAD 05 JUN 1995  ==> True
Case 24: MOM 05 JUN 1995  DAD 04 APR 1993  ==> FalseDad
Case 25: MOM 05 JUN 1995  DAD 06 SEP 1994  ==> FalseDad    
Case 31: MOM 03 SEP 1994  DAD N/A          ==> FalseMom
Case 32: MOM 03 SEP 1994  DAD 07 JUL 1996  ==> FalseMom
Case 33: MOM 03 SEP 1994  DAD 05 JUN 1995  ==> FalseMom
Case 34: MOM 03 SEP 1994  DAD 04 APR 1993  ==> FalseMom
Case 35: MOM 03 SEP 1994  DAD 06 SEP 1994  ==> FalseMom   
"""

def test_US09_Case11():
	Case11 = US09.US09("N/A","N/A","05 JUN 1995")
	assert Case11 == True
def test_US09_Case12():
	Case12 = US09.US09("N/A","07 JUL 1996","05 JUN 1995")
	assert Case12 == True
def test_US09_Case13():
	Case13 = US09.US09("N/A","05 JUN 1995","05 JUN 1995")
	assert Case13 == True
def test_US09_Case14():
	Case14 = US09.US09("N/A","04 APR 1993","05 JUN 1995")
	assert Case14 == "FalseDad"
def test_US09_Case15():
	Case15 = US09.US09("N/A","06 SEP 1994","05 JUN 1995")
	assert Case15 == "FalseDad"
def test_US09_Case21():
	Case21 = US09.US09("05 JUN 1995","N/A","05 JUN 1995")
	assert Case21 == True
def test_US09_Case22():
	Case22 = US09.US09("05 JUN 1995","07 JUL 1996","05 JUN 1995")
	assert Case22 == True
def test_US09_Case23():
	Case23 = US09.US09("05 JUN 1995","05 JUN 1995","05 JUN 1995")
	assert Case23 == True
def test_US09_Case24():
	Case24 = US09.US09("05 JUN 1995","04 APR 1993","05 JUN 1995")
	assert Case24 == "FalseDad"
def test_US09_Case25():
	Case25 = US09.US09("05 JUN 1995","06 SEP 1994","05 JUN 1995")
	assert Case25 == "FalseDad"
def test_US09_Case31():
	Case31 = US09.US09("03 SEP 1994","N/A","05 JUN 1995")
	assert Case31 == "FalseMom"
def test_US09_Case32():
	Case32 = US09.US09("03 SEP 1994","07 JUL 1996","05 JUN 1995")
	assert Case32 == "FalseMom"
def test_US09_Case33():
	Case33 = US09.US09("03 SEP 1994","05 JUN 1995","05 JUN 1995")
	assert Case33 == "FalseMom"
def test_US09_Case34():
	Case34 = US09.US09("03 SEP 1994","04 APR 1993","05 JUN 1995")
	assert Case34 == "FalseMom"
def test_US09_Case35():
	Case35 = US09.US09("03 SEP 1994","06 SEP 1994","05 JUN 1995")
	assert Case35 == "FalseMom"
