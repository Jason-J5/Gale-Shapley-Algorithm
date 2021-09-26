import os

with open("data.txt", "a") as f:
    for i in range(1000, 10000, 1000):
        print(os.system("python3 gs1.py -p" + str(i)), file=f)