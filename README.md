# CSC-321-Lab0

## Table of contents
* [General info](#general-info)
* [Run-Time](#Run-Time)
* [Requirements](#Requirements)
* [Usage and Functionality](#Usage-and-Functionality)



## General info
This project is my implementation of the Gale–Shapley algorithm.

An important note about the timing of gs() in gsDemo.py, gs.py, and gs1.py: In cases where the program is writting to a file it will have a significant impact on the time. To obtain a more accurate timing of the gs() function please use gs1.py without the debug flag.

# Run-Time
A sample output from [run-gs1.py](https://github.com/PurpleVS/CSC-321-/blob/main/run-gs1.py):

![run time graph](https://i.imgur.com/Q48OQZB.png)

# Requirements
* Python 3.9.x
* gnuplot 5.0.x



# Usage and Functionality
The input file file must have a even number of lines
The first half must have all the males names and their preferances
The second half must have all the females names and their preferances
The file should look as follows:

```
Abe:Abi Eve Cath Ivy Jan Dee Fay Bea Hope Gay 
Abi:Bob Fred Jon Gav Ian Abe Dan Ed Col Hal
etc
```

[gsDemo.py](https://github.com/PurpleVS/CSC-321-/blob/main/gsDemo.py): is a interactive termianl application which requires no arguments. It is a demo implementation of the Gale-Shapley algorithm written in python. The program runs for 10 suitors and 10 girls supplied in [prefs.txt](https://github.com/PurpleVS/CSC-321-/blob/main/prefs.txt). The output of the program is the particpants their preferances and the stable matchings along with the time taken to execute the algorithm.
    

    python3 gsDemo.py


[gs.py](https://github.com/PurpleVS/CSC-321-/blob/main/gs.py): is a command line program. It can take parameters through the command line and preform tasks based on the arguments supplied. The program can accept either a file containing a arbitray amount of people (so long as it is a even number), or it will accept a number argument in which the number represents the number of people(so long as that number is even). These valuse can be suppplied to the program via the command line. The output of the program is the particpants their preferances and the stable matchings along with the time taken to execute the algorithm.

```
python3 gs.py -h 

-o <path to output file> (if not specified, output.txt will be the default path)

-i <path to input file> (if not specified, the program will create a list of integers representing people and preferances)

-p <x> or --people <x> (x must be even, where x is the number of people to be created)
```

[gs1.py](https://github.com/PurpleVS/CSC-321-/blob/main/gs1.py):
This is a modification of the previous program gs. It requires a single parameter, which is the number of people. The first half of the number will represent the men and the second half the women. It has the option to enable debugging by suppling a second flag in the command line. Otherwise it's default output is the time elapsed between the beginning and the end of the proposal round. At the end of each round the program writes an integer for the trial input size (number of people used), and a floating point number with the time in seconds (up to ms, at least). The preference lists is generated at random.

```
python3 gs1.py -h
-p <x> or --people <x> (x must be even, where x is the number of people to be created)
-d enables debug mode. Text will be printed to the terminal and to a file called debug.txt
```

[run-gs1.py](https://github.com/PurpleVS/CSC-321-/blob/main/run-gs1.py):
A python script that calls [gs1.py](https://github.com/PurpleVS/CSC-321-/blob/main/gs1.py) with the values [1000, 1500, 2000, 2500,3000, 3500, 4000, 4500, 5000, 5500, 6000]. The script writes to file data.txt, appending the outputs of consecutive runs. The script ends with a call to the gnuplot program to perform the fit and plot the graph.

```
python3 run-gs1.py
```

[model.plt](https://github.com/PurpleVS/CSC-321-/blob/main/model.plt):
Calls gnuplot on data.txt and attempts to fit data.txt to the equation

```
y(x)=a0 + a1*x + a2 * x**2
```
and then plots the line of best fit on the graph 