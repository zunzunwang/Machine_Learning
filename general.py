#!/usr/bin/env python3

FILENAME = "./bank.csv"

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
    

def classAge(filename):
    """Return the average age of people who said 'yes' and group answers"""
    averageAge = nbPeople = totalPeople = 0
    MIN_AGE =   0
    MAX_AGE = 120
    STEP    =   5
    ageGroup = [0] * ((MAX_AGE - MIN_AGE) // STEP)
    
    with open(filename) as f:
        next(f) # skip first line
        for line in f:
            person = splitLine(line)
            totalPeople += 1
            
            if person['y'] == 'yes':
                age = int(person['age'])
                
                averageAge += age
                nbPeople += 1
                ageGroup[(age - MIN_AGE) // STEP] += 1
            
    averageAge /= nbPeople
    print('Average age: ', "{0:.3f}".format(averageAge))
    print('Succes rate: ', "{0:.3f}".format(nbPeople/totalPeople), '(%d/%d)' % (nbPeople, totalPeople))
    
    for i in range(len(ageGroup)):
        print(MIN_AGE + STEP * i, '-', MIN_AGE + STEP * (i+1), ':', ageGroup[i])
            

def classJob(filename):
    """Group people who said 'yes' by their job"""
    nbPeople = 0
    # there is a typo in the dataset, admin. is a category
    categories = { "admin.":0, "blue-collar":0, "entrepreneur":0,
                   "housemaid":0, "management":0, "retired":0,
                   "self-employed":0, "services":0, "student":0,
                   "technician":0, "unemployed":0, "unknown":0,
                   }
                   
    with open(filename) as f:
        next(f) # skip first line
        for line in f:
            person = splitLine(line)
            
            if person['y'] == 'yes':
                job = person['job']
                nbPeople += 1

                if job in categories:
                    categories[job] += 1
       
    for cat, val in categories.items():
        print(cat, ':', val,'-',  "{0:.2f}".format(val/nbPeople))
            

def classMarital(filename):
    """Group people who said 'yes' by their marital status"""
    nbPeople = 0
    status = { "divorced":0, "married":0, "single":0, "unknown":0,
                   }
                   
    with open(filename) as f:
        next(f) # skip first line
        for line in f:
            person = splitLine(line)
            
            if person['y'] == 'yes':
                marital = person['marital']
                nbPeople += 1

                if marital in status:
                    status[marital] += 1
       
    for sts, val in status.items():
        print(sts, ':', val,'-',  "{0:.2f}".format(val/nbPeople))
        
        
def classEducation(filename):
    """Group people who said 'yes' by their education"""
    nbPeople = 0
    # categories in the datasset are not the same as described
    levels = { "primary":0, "secondary":0, "tertiary":0, "unknown":0
                }
                   
    with open(filename) as f:
        next(f) # skip first line
        for line in f:
            person = splitLine(line)
            
            if person['y'] == 'yes':
                education = person['education']
                nbPeople += 1

                if education in levels:
                    levels[education] += 1
                else:
                    print(education)
                
    for lvl, val in levels.items():
        print(lvl, ':', val,'-',  "{0:.2f}".format(val/nbPeople))
        

def classDebts(filename):
    """Group people by their debts (credit default, housing/personal loan)"""
    nbPeople = nbUnknown = 0
    res = [0] * 8 # 3 binary values -> 8 cells
    
    with open(filename) as f:
        next(f) # skip first line
        for line in f:
            person = splitLine(line)
            
            #~ if person['y'] ==  'yes':
            if "unknown" in (person["default"], person["housing"], person["loan"]):
                nbUnknown += 1
            else:
                default = 0 if person["default"] == 'no' else 1
                housing = 0 if person["housing"] == 'no' else 1
                loan    = 0 if person["loan"] == 'no' else 1
                res[default*4 + housing*2 + loan] += 1
                nbPeople += 1
                
    print("Default  Housing  Loan")
    for i in range(8):
        print(format(i, '03b'), ':', "{0:.2f}".format(res[i]/nbPeople))
        
    print(nbPeople)

#11duration
def classDuration(filename):    
    """Group people who said 'yes' by their days after last contact"""
    nbPeople_yes = 0
    nbPeople_no  = 0
    STEP    = 60
    durationGroup_yes = {}
    durationGroup_no  = {}

                   
    with open(filename) as f:
        next(f) # skip first line
        for line in f:
            person = splitLine(line)           
            if person['y'] == 'yes':
                duration = int(person['duration'])
                nbPeople_yes += 1

                if (duration//STEP) in durationGroup_yes:
                    durationGroup_yes[duration//STEP] +=1
                else:
                    durationGroup_yes[duration//STEP] =1
                    
            else:
                duration = int(person['duration'])
                nbPeople_no += 1

                if (duration//STEP) in durationGroup_no:
                    durationGroup_no[duration//STEP] +=1
                else:
                    durationGroup_no[duration//STEP] =1
            
    print('for Group "yes"')
    for lvl, val in durationGroup_yes.items():
        print(lvl, 'm-',lvl+1,'m:', val,'-',  "{0:.2f}".format(val/nbPeople_yes))
    print('\n' + '*'*30 +'\n')
    print('for Group "no"')
    for lvl, val in durationGroup_no.items():
        print(lvl, 'm-',lvl+1,'m:', val,'-',  "{0:.2f}".format(val/nbPeople_no))


















#12campaign
def classCampaign(filename):
    """Group people who said 'yes' by their number of contact during this campaign"""
    nbPeople = 0
    # categories in the datasset :by number
    nb_contact = {}
                   
    with open(filename) as f:
        next(f) # skip first line
        for line in f:
            person = splitLine(line)           
            if person['y'] == 'yes':
                contact = person['campaign']
                nbPeople += 1

                if contact in nb_contact:
                    nb_contact[contact] += 1
                else:
                    nb_contact[contact] = 1
                    
                
    for lvl, val in nb_contact.items():
        print(lvl, ':', val,'-',  "{0:.2f}".format(val/nbPeople))    

#13pdays
def classPdays(filename):
    """Group people who said 'yes' by their days after last contact"""
    verageAge = nbPeople = 0
    STEP    = 50
    dayGroup = {}
    # categories in the datasset :by number
    #    nb_days = {}
                   
    with open(filename) as f:
        next(f) # skip first line
        for line in f:
            person = splitLine(line)           
            if person['y'] == 'yes':
                days = int(person['pdays'])
                nbPeople += 1

#                if days in nb_days:
                if (days//STEP) in dayGroup:
#                    nb_days[days] += 1
                    dayGroup[days//STEP] +=1
                else:
#                    nb_days[days] = 1
                    dayGroup[days//STEP] =1
                                    
    for lvl, val in dayGroup.items():
        print(lvl, '*50-',lvl+1,'*50:', val,'-',  "{0:.2f}".format(val/nbPeople))



#14.previous
def classPrevious(filename):
    """Group people who said 'yes' by their number of contact"""
    nbPeople = 0
    # categories in the datasset :by number
    nb_contact = {}
                   
    with open(filename) as f:
        next(f) # skip first line
        for line in f:
            person = splitLine(line)           
            if person['y'] == 'yes':
                contact = person['previous']
                nbPeople += 1

                if contact in nb_contact:
                    nb_contact[contact] += 1
                else:
                    nb_contact[contact] = 1
                    
                
    for lvl, val in nb_contact.items():
        print(lvl, ':', val,'-',  "{0:.2f}".format(val/nbPeople))


#15.poutcome
def classPoutcome(filename):
    """Group people who said 'yes' by their outcome"""
    nbPeople = 0
    # categories in the datasset :"failure" "success" "nonexistent"
    etat_outcome = { "failure":0, "success":0, "nonexistent":0, "unknown":0,"other":0,}
                   
    with open(filename) as f:
        next(f) # skip first line
        for line in f:
            person = splitLine(line)           
            if person['y'] == 'yes':
                etat = person['poutcome']
                nbPeople += 1

                if etat in etat_outcome:
                    etat_outcome[etat] += 1
                else:
                    print(etat)
                
    for lvl, val in etat_outcome.items():
        print(lvl, ':', val,'-',  "{0:.2f}".format(val/nbPeople))
    
    
    
    
    
    
        
        
def main():
#    classAge(FILENAME)
#    print('\n' + '*'*20 +'\n')
#    classJob(FILENAME)
#    print('\n' + '*'*20 +'\n')
#    classMarital(FILENAME)
#    print('\n' + '*'*20 +'\n')
#    classEducation(FILENAME)
#    print('\n' + '*'*20 +'\n')
#    classDebts(FILENAME)
#    print('\n' + '*'*20 +'\n')
#    classPoutcome(FILENAME)
#    print('\n' + '*'*20 +'\n')
#    classPrevious(FILENAME)
#    print('\n' + '*'*20 +'\n')
#    classPdays(FILENAME)

#    print('\n' + '*'*20 +'\n')
#    classCampaign(FILENAME)
    print('\n' + '*'*20 +'\n')
    classDuration(FILENAME)

    
    
if __name__ == '__main__':
    main()
