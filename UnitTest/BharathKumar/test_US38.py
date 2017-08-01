import US38
"""
$ Test-first tool : PyTest

Case 1: NO Birth in next 30 days
Case 2: 1 Birth in next 30 days
Case 3: 2 Births in next 30 days
Case 4: 3 Births in next 30 days
Case 5: Everyone born in next 30 days		
"""
Case_1 = {"I01":"15 MAR 2010","I02":"20 MAY 2012","I03":"22 SEP 2014","I04":"9 NOV 2016"}  # Returns []                       
Case_2 = {"I01":"15 MAR 2010","I02":"20 MAY 2012","I03":"22 SEP 2014","I04":"13 AUG 2010"} # Returns ["I04"]                  
Case_3 = {"I01":"15 MAR 2010","I02":"9 AUG 2010","I03":"22 SEP 2014","I04":"13 AUG 2010"}  # Returns ["I02","I04"]            
Case_4 = {"I01":"22 AUG 2010","I02":"9 AUG 2010","I03":"22 SEP 2014","I04":"13 AUG 2010"}  # Returns ["I01","I02","I04"]      
Case_5 = {"I01":"22 AUG 2010","I02":"9 AUG 2010","I03":"19 AUG 2010","I04":"13 AUG 2010"}  # Returns ["I01","I02","I03","I04"]




def test_US38_Case1():
    Case1 = US38.US38(Case_1)
    assert Case1 == []                        
def test_US38_Case2():
    Case2 = US38.US38(Case_2)
    assert Case2 == ["I04"]                   
def test_US38_Case3():
    Case3 = US38.US38(Case_3)
    assert Case3 == ["I02","I04"]             
def test_US38_Case4():
    Case4 = US38.US38(Case_4)
    assert Case4 == ["I02","I01","I04"]       
def test_US38_Case8():
    Case5 = US38.US38(Case_5)
    assert Case5 == ["I02","I03","I01","I04"]