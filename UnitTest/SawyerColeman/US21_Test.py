'''
    Sawyer Coleman
    US21 Test File
    SSW_555_Agile_Methods
    BHS_Project_SSW_555
    Sprint 4
'''
import US21

def test1_US21():
    case1 = US21.US21()
    assert case1 == False
    print(case1)

def test2_US21():
    case2 = US21.US21("F")
    assert case2 == False
    print(case2)

def test3_US21():
    case3 = US21.US21("M")
    assert case3 == False
    print(case3)

def test4_US21():
    case4 = US21.US21("F", "M")
    assert case4 == True
    print(case4)

def test5_US21():
    case5 = US21.US21("M", "M")
    assert case5 == False
    print(case5)

def test6_US21():
    case6 = US21.US21("F", "F")
    assert case6 == False
    print(case6)

def test7_US21():
    case7 = US21.US21("M", "F")
    assert case7 == False
    print(case7)
