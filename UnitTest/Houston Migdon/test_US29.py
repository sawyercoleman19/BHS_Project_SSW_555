import US29
   
NODead = {"I01":{"NAME":"BHARATH /KUMAR/"},"I02":{"NAME":"SAWYER /COLEMAN/"},"I03":{"NAME":"HOUSTON /MIGDON/"}}
ONEDead = {"I01":{"NAME":"BHARATH /KUMAR/"},"I02":{"NAME":"SAWYER /COLEMAN/"},"I03":{"NAME":"HOUSTON /MIGDON/","DEAT":"21 JAN 2002"}}
TWODead = {"I01":{"NAME":"BHARATH /KUMAR/"},"I02":{"NAME":"SAWYER /COLEMAN/","DEAT":"21 MAR 2011"},"I03":{"NAME":"HOUSTON /MIGDON/","DEAT":"21 JAN 2002"}}
ALLDead = {"I01":{"NAME":"BHARATH /KUMAR/","DEAT":"21 JAN 2002"},"I02":{"NAME":"SAWYER /COLEMAN/","DEAT":"21 MAR 2011"},"I03":{"NAME":"HOUSTON /MIGDON/","DEAT":"21 JAN 2002"}}

def test_US29_Case1():
    Case1 = US29.US29(NODead)
    assert Case1 == "RESULT: INDIVIDUAL: US29: No Individuals Deceased"
def test_US29_Case2():
    Case2 = US29.US29(ONEDead)
    assert Case2 == "RESULT: INDIVIDUAL: US29: List of Individuals Deceased: [\'ID: I03 Name: HOUSTON /MIGDON/\']"
def test_US29_Case3():
    Case3 = US29.US29(TWODead)
    assert Case3 == "RESULT: INDIVIDUAL: US29: List of Individuals Deceased: [\'ID: I02 Name: SAWYER /COLEMAN/\', \'ID: I03 Name: HOUSTON /MIGDON/\']"    
def test_US29_Case4():
    Case4 = US29.US29(ALLDead)
    assert Case4 == "RESULT: INDIVIDUAL: US29: List of Individuals Deceased: [\'ID: I02 Name: SAWYER /COLEMAN/\', \'ID: I03 Name: HOUSTON /MIGDON/\', \'ID: I01 Name: BHARATH /KUMAR/\']"

