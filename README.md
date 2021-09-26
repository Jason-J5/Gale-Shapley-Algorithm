# CSC-321-Lab0

## Table of contents
* [General info](#general-info)
* [Requirements](#Reqirements)
* [Usage](#Usage)


## General info
This project is my implementation of the Gale–Shapley algorithm

# Requirements
* Python 3.9.x
* gnuplot 



# Usage 
[gsDemo.py](https://github.com/PurpleVS/CSC-321-/blob/main/gsDemo.py): is a interactive termianl application which requires no arguments. It is a demo implementation of the Gale-Shapley algorithm written in python. The program runs for 10 suitors and 10 girls supplied in [prefs.txt](https://github.com/PurpleVS/CSC-321-/blob/main/prefs.txt). The output of the program is the particpants their preferances and the stable matchings along with the time taken to execute the algorithm.
    

    python3 gsDemo.py


[gs.py](https://github.com/PurpleVS/CSC-321-/blob/main/gs.py): is a command line program. It can take parameters through the command line and preform tasks based on the arguments supplied. The program can accept either a file containing a arbitray amount of people (so long as it is a even number), or it will accept a number argument in which the number represents the number of people(so long as that number is even). These valuse can be suppplied to the program via the command line. The output of the program is the particpants their preferances and the stable matchings along with the time taken to execute the algorithm.

```
python3 gs.py -h 

-o <path to output file> (if not specified, output.txt will be the default path)

-i <path to input file> (if not specified, the program will create a list of integers representing people and preferances)

-p <x> or --people <x> (x must be even, where x is the number of people to be created)


```


The input file file must have a even number of lines
The first half must have all the males names and their preferances
The second half must have all the females names and their preferances
The file should look as follows:

```
Abe:Abi Eve Cath Ivy Jan Dee Fay Bea Hope Gay 
Abi:Bob Fred Jon Gav Ian Abe Dan Ed Col Hal
etc
```