import US39
"""
$ Test-first tool : PyTest

Case 1: NO Anniversary in next 30 days
Case 2: 1 Anniversary in next 30 days
Case 3: 2 Anniversaries in next 30 days
Case 4: 3 Anniversaries in next 30 days
Case 5: Everyone have Anniversaries in next 30 days		
"""
Case_1 = {"F01":"15 MAR 2010","F02":"20 MAY 2012","F03":"22 SEP 2014","F04":"9 NOV 2016"}  # Returns []                       
Case_2 = {"F01":"15 MAR 2010","F02":"20 MAY 2012","F03":"22 SEP 2014","F04":"13 AUG 2010"} # Returns ["F04"]                  
Case_3 = {"F01":"15 MAR 2010","F02":"9 AUG 2010","F03":"22 SEP 2014","F04":"13 AUG 2010"}  # Returns ["F02","F04"]            
Case_4 = {"F01":"22 AUG 2010","F02":"9 AUG 2010","F03":"22 SEP 2014","F04":"13 AUG 2010"}  # Returns ["F01","F02","F04"]      
Case_5 = {"F01":"22 AUG 2010","F02":"9 AUG 2010","F03":"19 AUG 2010","F04":"13 AUG 2010"}  # Returns ["F01","F02","F03","F04"]




def test_US39_Case1():
    Case1 = US39.US39(Case_1)
    assert Case1 == []                        
def test_US39_Case2():
    Case2 = US39.US39(Case_2)
    assert Case2 == ["F04"]                   
def test_US39_Case3():
    Case3 = US39.US39(Case_3)
    assert Case3 == ["F04","F02"]             
def test_US39_Case4():
    Case4 = US39.US39(Case_4)
    assert Case4 == ["F04","F01","F02"]       
def test_US39_Case5():
    Case5 = US39.US39(Case_5)
    assert Case5 == ["F04","F01","F03","F02"]