import time
import re

start_time = time.time()

with open('C:/Users/fbukman/OneDrive - Capgemini/Desktop/pgm/VS/AoC2021/2022/day 08.txt') as fp:
    lines = fp.readlines()
    lines=[line.rstrip() for line in lines]

veld = ['' for i in range(99)]




print('deel 1:', 0)


som = 0
for i in range(1,98):
    for j in range(1,98):
        w = int(lines[i][j])
        t1 = 1
        t2 = 1
        t3 = 1
        t4 = 1
        a = i - 1
        while a > 0 and w > int(lines[a][j]):
            a -= 1
            t1 += 1
        a = i + 1
        while a < 98 and w > int(lines[a][j]):
            a += 1
            t2 += 1
        a = j - 1
        while a > 0 and w > int(lines[i][a]):
            a -= 1
            t3 += 1
        a = j + 1
        while a < 98 and w > int(lines[i][a]):
            a += 1
            t4 += 1
        fact = t1*t2*t3*t4
        if fact > som: som = fact
print('deel 2:', som)



print("--- %s seconds ---" % (time.time() - start_time))