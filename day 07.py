import time
import re

start_time = time.time()

with open('C:/Users/fbukman/OneDrive - Capgemini/Desktop/pgm/VS/AoC2021/2022/day 07.txt') as fp:
    lines = fp.readlines()
    lines=[line.rstrip() for line in lines]

def f_dir():
    global line
    global mx
    global som
    global unused
    global opdr2
    size = 0
    door = 1
    while door == 1 and line < mx:
        if lines[line][0:4] == '$ cd' and lines[line] != '$ cd ..': 
            line+=1
            size += f_dir()
        else:
            if lines[line] == '$ cd ..': 
                line +=1
                door = 0
            else:
                if lines[line] == '$ ls' or lines[line][0:3] == 'dir':
                    line+=1
                else:
                    deel = re.split(' ', lines[line])
                    size += int(deel[0])
                    line += 1
    print(size)
    if size <= 100000:
        som += size 
    if size < opdr2 and size+unused > 30000000:
        opdr2 = size
    return size
    





deel = []
line = 0
size = 0
som = 0
mx = len(lines)
opdr2 = 30000000
unused = 29610082


if lines[line][0:4] == '$ cd': 
    line+=1
    size += f_dir()

print('deel 1:', som)


print('deel 2:', opdr2)



print("--- %s seconds ---" % (time.time() - start_time))