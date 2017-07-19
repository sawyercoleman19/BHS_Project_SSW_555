import US22

def test1_US22():
    case1 = US22.US22(["I01", "I02", "I03", "I04", "I05"])
    assert case1 == True
    print(case1)

def test2_US22():
    case2 = US22.US22(["I01", "I06", "I03", "I04", "I05"])
    assert case2 == True
    print(case2)

def test3_US22():
    case3 = US22.US22(["I01", "I01", "I01", "I01", "I01"])
    assert case3 == False
    print(case3)

def test4_US22():
    case4 = US22.US22(["I02", "I02", "I03", "I04", "I05"])
    assert case4 == False
    print(case4)

def test5_US22():
    case5 = US22.US22(["I02", "I02", "I04", "I04", "I05"])
    assert case5 == False
    print(case5)
