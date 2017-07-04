'''
    Sawyer Coleman
    US02 Test File
    SSW_555_Agile_Methods
    BHS_Project_SSW_555
    Project06
    '''
import US02

def test1_US02():
    case1 = US02.US02("27 MAR 1997")
    assert case1 == True
    print(case1)

def test2_US02():
    case2 = US02.US02()
    assert case2 == True
    print(case2)

def test3_US02():
    case3 = US02.US02("27 MAR 2003", "12 DEC 2014")
    assert case3 == True
    print(case3)

def test4_US02():
    case4 = US02.US02("27 MAR 2004", "12 DEC 2000")
    assert case4 == False
    print(case4)

def test5_US02():
    case5 = US02.US02("12 DEC 2019", "12 DEC 2019")
    assert case5 == False
    print(case5)
