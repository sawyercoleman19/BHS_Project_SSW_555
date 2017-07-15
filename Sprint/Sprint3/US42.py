import datetime
months = {"JAN": 1, "FEB": 2 ,"MAR": 3,"APR": 4,"MAY": 5,"JUN": 6,"JUL": 7,"AUG": 8,"SEP": 9,"OCT": 10,"NOV": 11,"DEC": 12 }
def US42(dt):
    if dt == 'N/A':
        return True
    else:
        date = dt.split(" ")[::-1]
        date[1] = months[date[1].upper()]
        #print date
        try:
            newDate = datetime.datetime(int(date[0]),date[1],int(date[2]))
            return True
        except ValueError:
            #print "In US 42, " + idd + "'s " + context + " date of " + dt + " is invalid."
            return False
        else:
            return True

