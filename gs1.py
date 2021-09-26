import sys, getopt
import copy
import time
import random
from timeit import default_timer as timer

#set up global vars 

rank = dict()
people = []
men = []
women = []
freeMen = []
freeWomen = []
husband = []
asked = []

def createIntPrefs(p):
    """[Adds p people to the dict rank and assigns each of them preferances]

    Args:
        p ([int]): [P represents the number of people you want to create]
    """
    #males first half of number 
    half = int(p/2)
    for i in range(p):
        if i < half:
            rank[i] = [j for j in range(half, half*2)]
        else:
            rank[i] = [j for j in range(0, half)]


def assignGlobals():
    """[Assigns values to the global variables, needed to be able to use different files for input and output]
    """    

    global people, men, women, freeMen, freeWomen, husband, asked 
    people = list(rank.keys())
    #take first half of people list for men
    men = people[:len(people)//2]
    #take second half of people list women 
    women = people[len(people)//2:]
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


def prefers(w, suiter, partner, f=None):
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
    if f == None:
        wlist = list(rank[w])
        #print(wlist)
        if wlist.index(suiter) < wlist.index(partner):
            return True
        return False
    
    else:
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



def gs(f=None):
    """[Implements the gale shapley algorithm following the psudocode from the slides]

    Args:
        f ([file]): [needed for output file]
    """
    if f == None:
        while len(freeMen) > 0 :
            #Choose such a man m
            m = freeMen[0]
            #w = 1st woman on m's list to whom m has not yet proposed
            w = rank[m][asked[men.index(m)]]
            #increment asked for m
            asked[men.index(m)] += 1
            #if (w is free)
                #assign m and w to be engaged
            if freeWomen.__contains__(w):            
                husband[women.index(w)] = m
                freeWomen.pop(freeWomen.index(w))
                freeMen.pop(freeMen.index(m))
                #print(husband)
            elif prefers(w, m, husband[women.index(w)]):
                #print(w ,"prefers", m)
                freeMen.insert(0, husband[women.index(w)])
                husband[women.index(w)] = m
                freeMen.pop(freeMen.index(m))

    else:    
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
        

def main(argv):
    outputFile = "debug.txt"
    numPeople = 0
    debug = False
    try:
        opts, args = getopt.getopt(argv,"hdp:")
    except getopt.GetoptError:
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("Usage:")
            print("-p <x> or --people <x> (x must be even, where x is the number of people to be created)")
            print("-d enables debug mode. Text will be printed to the terminal and to a file called debug.txt")
            print("-h help")
            
            sys.exit()
        
        elif opt == '-d':
            debug = True
        
        elif opt == "-p":
            numPeople = arg
        else:
            sys.exit()


    if int(numPeople) % 2 != 0:
        print("-p only accepts even numbers")
        sys.exit()

    createIntPrefs(int(numPeople))
    
    assignGlobals()


    if debug == False:
        for person in people:
            FYshuffle(rank[person])        
        
        time.sleep(.3)
        t1_start = time.time()
        gs()
        t1_stop = time.time()
        cpuTime = t1_stop-t1_start
        print(numPeople, f"{cpuTime:.5f}")  
    else:
        with open(outputFile, "w") as f:
            #Print the setup ie. people and prefs
            setup(f)
            
            print(file=f)
            print()

            time.sleep(.3)
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
            
            cpuTime = t1_stop-t1_start
            print(numPeople, f"{cpuTime:.5f}", file=f)
            print(numPeople, f"{cpuTime:.5f}")
 


if __name__ == "__main__":
   main(sys.argv[1:])