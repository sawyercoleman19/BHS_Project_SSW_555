import US36
"""
$ Test-first tool : PyTest

Case 1: NO Death in recent 30 days
Case 2: 1 Death in recent 30 days
Case 3: 2 Deaths in recent 30 days
Case 4: 3 Deaths in recent 30 days
Case 5: Everyone born in recent 30 days		
"""
Case_1 = {"I01":"15 MAR 2010","I02":"20 MAY 2012","I03":"22 SEP 2014","I04":"9 NOV 2016"}  # Returns []                       
Case_2 = {"I01":"15 MAR 2010","I02":"20 MAY 2012","I03":"22 SEP 2014","I04":"13 JUL 2017"} # Returns ["I04"]                  
Case_3 = {"I01":"15 MAR 2010","I02":"9 JUL 2017","I03":"22 SEP 2014","I04":"13 JUL 2017"}  # Returns ["I02","I04"]            
Case_4 = {"I01":"22 JUN 2017","I02":"9 JUL 2017","I03":"22 SEP 2014","I04":"13 JUL 2017"}  # Returns ["I01","I02","I04"]      
Case_5 = {"I01":"22 JUN 2017","I02":"9 JUL 2017","I03":"19 JUN 2017","I04":"13 JUL 2017"}  # Returns ["I01","I02","I03","I04"]




def test_US36_Case1():
    Case1 = US36.US36(Case_1)
    assert Case1 == []                        
def test_US36_Case2():
    Case2 = US36.US36(Case_2)
    assert Case2 == ["I04"]                   
def test_US36_Case3():
    Case3 = US36.US36(Case_3)
    assert Case3 == ["I02","I04"]             
def test_US36_Case4():
    Case4 = US36.US36(Case_4)
    assert Case4 == ["I02","I01","I04"]       
def test_US36_Case5():
    Case5 = US36.US36(Case_5)
    assert Case5 == ["I02","I03","I01","I04"]