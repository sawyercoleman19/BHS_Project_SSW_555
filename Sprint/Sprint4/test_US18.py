import US18

#for test case 1
Indtest1 = {"I1": {"NAME": "Jim"}, "I2": {"NAME": "Jane"}, "I3": {"NAME": "Harry", "Child": "F2"}, "I4": {"NAME": "Emma", "Child": "F2"}}

Famtest1 = {"F1": {"HUSB": "I3", "WIFE": "I4"}, "F2": {"HUSB": "I1", "WIFE": "I2"}}

def test_us18_1():
	result = US18.US18(Indtest1, Famtest1)
	assert result == ['Error: Family: US18: Family F1 has a husband and wife who are siblings.']




#for test case 2
Indtest2 = {"I1": {"NAME": "Jim"}, "I2": {"NAME": "Jane"}, "I3": {"NAME": "Harry", "Child": "F2"}, "I4": {"NAME": "Emma", "Child": "F2"}}

Famtest2 = {"F1": {"HUSB": "I1", "WIFE": "I2"}, "F2": {"HUSB": "I1", "WIFE": "I2"}}

def test_us18_2():
	result = US18.US18(Indtest2, Famtest2)
	assert result == []



#for test case 3
Indtest3 = {"I1": {"NAME": "Jim"}, "I2": {"NAME": "Jane", "Child": "F5"}, "I3": {"NAME": "Harry", "Child": "F2"}, "I4": {"NAME": "Emma"}}

Famtest3 = {"F1": {"HUSB": "I3", "WIFE": "I4"}, "F2": {"HUSB": "I1", "WIFE": "I2"}}

def test_us18_3():
	result = US18.US18(Indtest3, Famtest3)
	assert result == []




#for test case 4
Indtest4 = {"I1": {"NAME": "Jim", "Child": "F1"}, "I2": {"NAME": "Jane", "Child": "F1"}, "I3": {"NAME": "Harry", "Child": "F5"}, "I4": {"NAME": "Emma"}}

Famtest4 = {"F1": {"HUSB": "I3", "WIFE": "I4"}, "F2": {"HUSB": "I1", "WIFE": "I2"}}

def test_us18_4():
	result = US18.US18(Indtest4, Famtest4)
	assert result == ['Error: Family: US18: Family F2 has a husband and wife who are siblings.']




#for test case 5
Indtest5 = {"I1": {"NAME": "Jim", "Child": "F1"}, "I2": {"NAME": "Jane", "Child": "F1"}, "I3": {"NAME": "Harry", "Child": "F2"}, "I4": {"NAME": "Emma", "Child": "F2"}, "I5": {"NAME": "Alex"}}

Famtest5 = {"F1": {"HUSB": "I3", "WIFE": "I4"}, "F2": {"HUSB": "I1", "WIFE": "I2"}}

def test_us18_5():
	result = US18.US18(Indtest5, Famtest5)
	assert result == ['Error: Family: US18: Family F1 has a husband and wife who are siblings.', 'Error: Family: US18: Family F2 has a husband and wife who are siblings.']
