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
 [gs.py](https://github.com/PurpleVS/CSC-321-/blob/main/gs.py) :

 gs.py is a command line program. This means you launch it either from a Windows command prompt or Linux console, or create shortcuts to predefined command lines using a Linux Bash script or Windows batch/cmd file.

```
python3 gs.py -h 

-o <path to output file>

-i <path to input file> (if not specified it the program will create a list of integers representing people and preferances)

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
