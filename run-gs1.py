# Program Name: gs1.py
# Created by: Jason Jacobs
# Date: 9/23/2021
# PURPOSE: See README.md
# INPUT(S): N/A
# OUTPUT(S): data.txt, gnuplot output
# EXAMPLES: 1000 0.04668
          # 1500 0.13671
          # 2000 0.19805
          # 2500 0.39101
          # 3000 0.71319
          # 3500 0.90007
          # 4000 1.09339

import os

with open("data.txt", "w") as f:

    for i in range(1000, 6500, 500):
        os.system("python3 gs1.py -p" + str(i) + '| tee -a ' + "data.txt")

    f.close()

os.system("/usr/bin/gnuplot -persist model.plt")