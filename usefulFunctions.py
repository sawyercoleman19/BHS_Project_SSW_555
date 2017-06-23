"""This file is where group members will copy and paste 
functions used in their user stories and add a brief description
as to what they do. Any group member can use those functions and
tweak them to help their own user stories if they are appropriate"""


#Example

#----------------------------------------------------------------------------------

#This function from US23 checks all male children

def maleChild(CHIL):
	male_Child = []
	for j in CHIL:
		if db.IndDic[j]["SEX"] == "M":
			#print db.IndDic[j]["NAME"]
			male_Child.append(db.IndDic[j]["NAME"])
	return male_Child
  
  #---------------------------------------------------------------------------------
