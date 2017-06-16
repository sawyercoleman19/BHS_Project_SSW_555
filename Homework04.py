import unittest
import datetime
import BHS_555.py

def Age(BIRT, DEAT):
    months = {"JAN": "01","FEB":"02" ,"MAR": "03","APR": "04","MAY": "05","JUN": "06","JUL": "07","AUG":"08","SEP": "09","OCT": "10","NOV": "11","DEC": "12" }
        today = datetime.date.today()
        tod = str(today).split("-")
        bir = BIRT.split(" ")[::-1]
        bir[1] = months[bir[1]]
        
        if DEAT != "N/A":
            tod = DEAT.split(" ")[::-1]
                tod[1] = months[tod[1]]
    
        age = int(tod[0])-int(bir[0])
        
        if int(tod[1]) < int(bir[1]):
            age -= 1
        elif int(tod[1]) == int(bir[1]) and int(tod[2]) < int(bir[2]):
            age -= 1
        
                return str(age)
