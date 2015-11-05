#!/usr/bin/env python3
FILENAME = "./bank.csv"
import time
import datetime
#today
#today=int(time.strftime("%w"))
#print today
#give a date http://yige.org
#anyday=datetime.datetime(2012,4,23).strftime("%w")
#print (anyday)





def splitLine(line):
    """Return a dict object containing all infos of a person"""
    ar = line.split(';')
    categories = ["age", "job", "marital", "education", 
                  "default", "balance", "housing", "loan", 
                  "contact", "day", "month", "duration", 
                  "campaign", "pdays", "previous", "poutcome", "y" ]
    person = {}
                  
    for i in range(len(ar)):
        person[categories[i]] = ar[i].replace('"', '').replace('\n', '')
        
    return person



def classDayOfWeek(filename):
    """Group people who said 'yes' by their date of contact"""
    nbPeople = 0
    date_contact = {}
    categories_month = { "jan":1, "feb":2, "mar":3, "apr":4, "may":5, "jun":6,
                         "jul":7, "aug":8, "sep":9, "oct":10, "nov":11, "dec":12,}
                   
    with open(filename) as f:
        next(f) # skip first line
        for line in f:
            person = splitLine(line)           
            if person['y'] == 'yes':
                day = int(person['day'])
                month = person['month']
                weekday=datetime.datetime(2012,categories_month[month],day).strftime("%w")
                nbPeople += 1

                if weekday in date_contact:
                    date_contact[weekday] += 1
                else:
                    date_contact[weekday] = 1
                    
                
    for lvl, val in date_contact.items():
        print(lvl, ':', val,'-',  "{0:.2f}".format(val/nbPeople))



def main():
    print('\n' + '*'*20 +'\n')
    classDayOfWeek(FILENAME)



if __name__ == '__main__':
    main()

