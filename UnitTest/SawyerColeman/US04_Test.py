'''
Sawyer Coleman
US04 Test File
SSW_555_Agile_Methods
BHS_Project_SSW_555
Project08
'''
import US04

def test1_US04():
    case1 = US04.US04("27 MAR 1997")
    assert case1 == True
    print(case1)

def test2_US04():
    case2 = US04.US04()
    assert case2 == True
    print(case2)

def test3_US04():
    case3 = US04.US04("27 MAR 2003", "12 DEC 2014")
    assert case3 == True
    print(case3)

def test4_US04():
    case4 = US04.US04("27 MAR 2004", "12 DEC 2000")
    assert case4 == False
    print(case4)

def test5_US04():
    case5 = US04.US04("12 DEC 2019", "12 DEC 2019")
    assert case5 == False
    print(case5)

def test6_US04():
    case6 = US04.US04(DIV = "12 DEC 2012")
    assert case6 == False
    print(case6)
