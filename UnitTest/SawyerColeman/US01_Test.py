'''
    Sawyer Coleman
    US01 Test File
    SSW_555_Agile_Methods
    BHS_Project_SSW_555
    Project04
'''
import US01

def test1_US01():
    case1 = US01.US01("27 MAR 1997")
    assert case1 == True
    print(case1)

def test2_US01():
    case2 = US01.US01("27 MAR 2029")
    assert case2 == False
    print(case2)

def test3_US01():
    case3 = US01.US01("27 MAR 2003", "12 DEC 2014")
    assert case3 == True
    print(case3)

def test4_US01():
    case4 = US01.US01("27 MAR 2004", "12 DEC 2019")
    assert case4 == False
    print(case4)

def test5_US01():
    case5 = US01.US01("27 MAR 2019", "12 DEC 2019")
    assert case5 == False
    print(case5)

def test6_US01():
    case6 = US01.US01("27 MAR 2000", "12 DEC 2004", "10 DEC 2016")
    assert case6 == True
    print(case6)

def test7_US01():
    case7 = US01.US01("27 MAR 2000", "12 DEC 2004", "10 DEC 2020")
    assert case7 == False
    print(case7)

def test8_US01():
    case8 = US01.US01("27 MAR 2019", "12 DEC 2019", "10 DEC 2020")
    assert case8 == False
    print(case8)

def test9_US01():
    case9 = US01.US01("27 MAR 2000", "12 DEC 2009", "10 DEC 2016", "09 JAN 2017")
    assert case9 == True
    print(case9)

def test10_US01():
    case10 = US01.US01("27 MAR 2000", "12 DEC 2009", "10 DEC 2016", "09 JAN 2019")
    assert case10 == False
    print(case10)

def test11_US01():
    case11 = US01.US01("27 MAR 2018", "12 DEC 2018", "10 DEC 2019", "09 DEC 2020")
    assert case11 == False
    print(case11)

def test12_US01():
    case12 = US01.US01("27 MAR 2000", MARR = "10 DEC 2019", DIV = "09 JAN 2019")
    assert case12 == False
    print(case12)
