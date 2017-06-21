'''
Sawyer Coleman
US07 Test File
SSW_555_Agile_Methods
BHS_Project_SSW_555
Homework04
'''
import US07

def test1_US07():
    case1 = US07.US07("27 MAR 1997")
    assert case1 == True
    print(case1)

def test2_US07():
    case2 = US07.US07("27 DEC 1994")
    print(case2)
    assert case2 == True

def test3_US07():
    case3 = US07.US07("20 MAY 1884")
    print(case3)
    assert case3 == True

def test4_US07():
    case4 = US07.US07("13 JUN 1890")
    print(case4)
    assert case4 == True

def test5_US07():
    case5 = US07.US07("02 JUL 1100")
    print(case5)
    assert case5 == False

def test7_US07():
    case7 = US07.US07("06 JUN 1867")
    print(case7)
    assert case7 == False

def test8_US07():
    case8 = US07.US07("06 JUN 1867", "17 DEC 1943")
    print(case8)
    assert case8 == True

def test9_US07():
    case9 = US07.US07("18 OCT 1944", "30 JUL 2006")
    print(case9)
    assert case9 == True

def test10_US07():
    case10 = US07.US07("19 OCT 1700", "21 FEB 1900")
    print(case10)
    assert case10 == False

def test11_US07():
    case11 = US07.US07("06 FEB 1867", "06 FEB 2017")
    print(case11)
    assert case11 == False

