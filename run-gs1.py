import os

with open("data.txt", "w") as f:

    for i in range(1000, 6500, 500):
        os.system("python3 gs1.py -p" + str(i) + '| tee -a ' + "data.txt")

    f.close()