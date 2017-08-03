'''
    Sawyer Coleman
    US10 Test File
    SSW_555_Agile_Methods
    BHS_Project_SSW_555
    Sprint 4
'''
import US10

def test1_US10():
    case1 = US10.US10("27 MAR 1997")
    assert case1 == True
    print(case1)

def test2_US10():
    case2 = US10.US10()
    assert case2 == True
    print(case2)

def test3_US10():
    case3 = US10.US10("27 MAR 1994", "12 DEC 2014")
    assert case3 == True
    print(case3)

def test4_US10():
    case4 = US10.US10("27 MAR 2004", "12 DEC 2010")
    assert case4 == False
    print(case4)

def test5_US10():
    case5 = US10.US10("12 DEC 2000", "12 DEC 2014")
    assert case5 == True
    print(case5)
