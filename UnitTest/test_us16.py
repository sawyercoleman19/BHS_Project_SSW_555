def find_dups(IndNameBirth):
    found = False
    for i, val in enumerate(IndNameBirth): 
        if val in IndNameBirth[i+1:]:
            print val, " is a duplicate."
            
            found = True
    return found 
     
        
    


def test1():
    IndNameBirth = [("Joe", "1/1/2000"), ("Joe", "1/1/2000"), ("Joe", "2/2/2002")]
    find_dups(IndNameBirth)
    assert find_dups == True 


def test2():
    IndNameBirth = [("Joe", "1/1/2000"), ("Joe", "1/1/2000"), ("Ed", "1/1/2000")]
    find_dups(IndNameBirth)
    assert find_dups == True 
    
    
def test3():
    IndNameBirth = [("Alex", "1/1/2000"), ("Joe", "1/1/2000"), ("Joe", "2/2/2002")]
    find_dups(IndNameBirth)
    assert find_dups == False 


def test4():
    IndNameBirth = [("Joe", "1/1/2000"), ("Joe", "1/1/2000"), ("Joe", "1/1/2000")]
    find_dups(IndNameBirth)
    assert find_dups == True 


def test5():
    IndNameBirth = []
    find_dups(IndNameBirth)
    assert find_dups == False 



test1(IndNameBirth) 
test2(IndNameBirth) 
test3(IndNameBirth) 
test4(IndNameBirth) 
test5(IndNameBirth) 
