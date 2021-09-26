import copy
import time
import random
from timeit import default_timer as timer


"""
The file must have a even number of lines
The first half must have all the males names and their preferances
The second half must have all the females names and their preferances
The file should look as follows:

Abe:Abi Eve Cath Ivy Jan Dee Fay Bea Hope Gay 
Abi:Bob Fred Jon Gav Ian Abe Dan Ed Col Hal 

"""


"""
Hard coded values
rank = dict() 
rank ['Victor'] = ('Bertha', 'Amy', 'Diane', 'Erika', 'Clare') 
rank ['Wyatt'] = ('Erika', 'Bertha', 'Amy', 'Clare', 'Diane') 
rank ['Xavier'] = ('Bertha', 'Erika', 'Clare', 'Diane', 'Amy') 
rank ['Yancey'] = ('Amy', 'Diane', 'Clare', 'Bertha', 'Erika') 
rank ['Zeus'] = ('Bertha', 'Diane', 'Amy', 'Erika', 'Clare') 
rank ['Amy'] = ('Zeus', 'Victor', 'Wyatt', 'Yancey', 'Xavier') 
rank ['Bertha'] = ('Xavier', 'Wyatt', 'Yancey', 'Victor', 'Zeus') 
rank ['Clare'] = ('Wyatt', 'Xavier', 'Yancey', 'Zeus', 'Victor') 
rank ['Diane'] = ('Victor', 'Zeus', 'Yancey', 'Xavier', 'Wyatt') 
rank ['Erika'] = ('Yancey', 'Wyatt', 'Zeus', 'Xavier', 'Victor') """

wallTimeStart = time.time()


rank = dict()

#read prefs from file 
name = ''
with open("prefs.txt") as file:
 for line in file:
    name = line.split(':')
    rank[name[0]] = (name[1].strip().split(" "))

people = list(rank.keys())
#take first half of people list for men
men = people[:len(people)//2]
#take second half of people list women 
women = people[len(people)//2:]


def FYshuffle(list):
    """[Implementation of the fisher yates shuffle algo]

    Args:
        list ([list]): [list of things to shuffle]

    Returns:
        [list]: [shuffled version of the original list]
    """   
    for i in range(len(list)):
        a = random.randint(0, len(list) - 1)
        b = random.randint(0, len(list) - 1)
        list[a], list[b] = list[b], list[a]
    return list


def setup(f):
    """[Shuffles the preferances and writes the participants and their preferances to the file]

    Args:
        f ([file]): [needed to print output to the file]
    """ 
    #Shuffle all the preferances
    for person in people:
        FYshuffle(rank[person])
        #print(rank[person])

    """
    Print out the participants and the preferances
    """
    print("Participants:", file=f)
    print("Participants:")

    print(men, file=f)
    print(men)
    print(women, file=f)
    print(women)

    print('', file=f)
    print('')

    print("Preferences:", file=f)
    print("Preferences:")
    for person in people:
        print(person,":", rank[person], file=f)
        print(person,":", rank[person])





#list of free men in a queue
freeMen = copy.deepcopy(men)
#list of free women in a queue
freeWomen =  copy.deepcopy(women)

"""Maintain two arrays wife[m], and husband[w].
– set entry to 0 if unmatched
– if m matched to w then wife[m]=w and husband[w]=m"""
husband = [0] * len(freeMen) 


"""
Men proposing.
    For each man, maintain a list of women, ordered by preference.
    Maintain an array count[m] that counts the number of proposals
    made by man m.
"""
#list of women ordered by preferance is in the dict accessed via rank[men[0]] where men[0] is the mans name or rank[x] where x is the mans name
#print(rank['Victor'])

#asked is a list of keeps count of the number of proposals made by man m  
#ex: asked[0] is the number of women that man[0] has asked 
#ex: if man[0] has asked 3 people then asked[0] == 3 
asked = [0] * len(men)  

"""
#   man1 asks choice 1
man1 = men[0]
indexOfPick = asked[men.index(man1)]
print(rank[man1][indexOfPick])
"""


def prefers(w, suiter, partner, f):
    """[returns who woman w prefers, her suiter or her partner]

    Args:
        w ([str]): [womans name]
        suiter ([str]): [suiters name]
        partner ([str]): [partners name]
        f ([file]): [output file to write to it]

    Returns:
        [bool]: [true when the woman prefers her suiter to her current partner 
        and false if she prefers her current partner]
    """
    wlist = list(rank[w])
    #print(wlist)
    if wlist.index(suiter) < wlist.index(partner):
        print(w, "prefers", suiter, "over", partner, file=f)
        print(w, "prefers", suiter, "over", partner)
        print(w, "dumps", partner, file=f)
        print(w, "dumps", partner)
        return True

    print(w, "prefers", partner, "over", suiter, file=f)
    print(w, "prefers", partner, "over", suiter)
    return False

"""p = husband[women.index("Bertha")] = "Victor"
#print(husband)
prefers("Bertha", "Xavier", p)

husband[women.index("Bertha")] = "Yancey"
print(husband)
prefers("Bertha", "Victor", husband[women.index("Bertha")])"""


def gs(f):
    """[Implements the gale shapley algorithm following the psudocode from the slides]

    Args:
        f ([file]): [needed for output file]
    """  
    """
    Initialize each person to be free.
    while (some man is free and hasn't proposed to every woman) {
        
        Choose such a man m
        w = 1st woman on m's list to whom m has not yet proposed
        
        if (w is free)
            assign m and w to be engaged

        else if (w prefers m to her fiancé m')
            assign m and w to be engaged, and m' to be free

        else
            w rejects m
    }

    """
    #starting all people are free ie freeMen and freeWomen have all males and females
    while len(freeMen) > 0 :
        #Choose such a man m
        m = freeMen[0]

        #print space for new man
        print(file=f)
        print()

        #w = 1st woman on m's list to whom m has not yet proposed
        w = rank[m][asked[men.index(m)]]
        
        #increment asked for m
        asked[men.index(m)] += 1

        print(m, "proposes to", w, file=f)
        print(m, "proposes to", w)
        
        #if (w is free)
            #assign m and w to be engaged
        if freeWomen.__contains__(w):
            print(m ,"and", w, "are engaged", file=f)
            print(m ,"and", w, "are engaged")
            
            husband[women.index(w)] = m

            freeWomen.pop(freeWomen.index(w))
            freeMen.pop(freeMen.index(m))

            #print(husband)

        elif prefers(w, m, husband[women.index(w)], f):
            #print(w ,"prefers", m)
            freeMen.insert(0, husband[women.index(w)])
            husband[women.index(w)] = m
            print(m, "and", w, "are engaged", file=f)
            print(m, "and", w, "are engaged")
            freeMen.pop(freeMen.index(m))
        
        else:
            print(w, "rejects", m, file=f)
            print(w, "rejects", m)


run =  True

with open("output.txt", "w") as f:
    while run:
        #Print the setup ie. people and prefs
        setup(f)
        
        print(file=f)
        print()

        time.sleep(.1)
        #t1_start = timer() 
        t1_start = time.time()          
        #call to gale shapely
        gs(f)
        #t1_stop = timer()
        t1_stop = time.time()


        #print the partners
        print('', file=f)
        print('')
        print("Pairings:", file=f)
        print("Pairings:")
        for i in range(len(husband)):
            print(husband[i],":",women[i], file=f)
            print(husband[i],":",women[i])

        print(file=f)
        print('')
        
        wallTimeEnd = time.time()
        wallTime = wallTimeEnd-wallTimeStart
        print(f"Elapsed wall clock time: {wallTime:f}", file=f)
        print(f"Elapsed wall clock time: {wallTime:f}")
        cpuTime = t1_stop-t1_start
        print(f"Elapsed CPU time:        {cpuTime:.5f}", file=f)
        print(f"Elapsed CPU time:        {cpuTime:.5f}")  

        print("Another trial? (y)es, (n)o?", file=f)
        print("Another trial? (y)es, (n)o?")
        repeat = input()
        print(repeat, file=f)
        if repeat == 'n' or repeat == "no":
            f.close()
            run = False