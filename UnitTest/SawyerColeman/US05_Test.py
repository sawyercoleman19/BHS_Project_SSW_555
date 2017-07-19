'''
    Sawyer Coleman
    US04 Test File
    SSW_555_Agile_Methods
    BHS_Project_SSW_555
    Project08
    '''
import US05

def test1_US05():
    case1 = US05.US05("27 MAR 1997")
    assert case1 == True
    print(case1)

def test2_US05():
    case2 = US05.US05()
    assert case2 == True
    print(case2)

def test3_US05():
    case3 = US05.US05("27 MAR 2003", "12 DEC 2014")
    assert case3 == True
    print(case3)

def test4_US05():
    case4 = US05.US05("27 MAR 2004", "12 DEC 2000")
    assert case4 == False
    print(case4)

def test5_US05():
    case5 = US05.US05("12 DEC 2019", "12 DEC 2019")
    assert case5 == False
    print(case5)

def test6_US05():
    case6 = US05.US05(DEAT = "12 DEC 2012")
    assert case6 == True
    print(case6)
