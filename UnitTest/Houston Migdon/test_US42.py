import US42
   
def test_US42_Case1():
    Case1 = US42.US42("7 MAR 1994")
    assert Case1 == True
def test_US42_Case2():
    Case2 = US42.US42("31 APR 1995")
    assert Case2 == False
def test_US42_Case3():
    Case3 = US42.US42("30 FEB 2008")
    assert Case3 == False    
def test_US42_Case4():
    Case4 = US42.US42("51 OCT 2015")
    assert Case4 == False
