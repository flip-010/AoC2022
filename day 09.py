import time
import re

start_time = time.time()

with open('C:/Users/fbukman/OneDrive - Capgemini/Desktop/pgm/VS/AoC2021/2022/day 09.txt') as fp:
    lines = fp.readlines()
    lines=[line.rstrip() for line in lines]

def day09(lengte):
    lst = []
    s = lengte
    slang = [[0,0] for i in range(s)]

    lst.append(slang[-1][0]*1000+slang[-1][1])

    for line in lines:
        r, s = line.split(' ')
        for t in range(int(s)):
            if r == "R": slang[0][1] += 1
            if r == "L": slang[0][1] -= 1
            if r == "D": slang[0][0] += 1
            if r == "U": slang[0][0] -= 1

            lst.append(slang[-1][0]*1000+slang[-1][1])

            for f in range(1,len(slang)):
                if abs(slang[f][0] - slang[f-1][0]) == abs(slang[f][1] - slang[f-1][1]):
                    if slang[f-1][0] - slang[f][0] == 2:
                        slang[f][0] +=1
                    if slang[f-1][0] - slang[f][0] == -2:
                        slang[f][0] -=1
                    if slang[f-1][1] - slang[f][1] == 2:
                        slang[f][1] +=1
                    if slang[f-1][1] - slang[f][1] == -2:
                        slang[f][1] -=1

                else:
                    if slang[f-1][0] - slang[f][0] > 1:
                        slang[f][0] +=1
                        slang[f][1] = slang[f-1][1]
                    else:
                        if slang[f-1][0] - slang[f][0] < -1:
                            slang[f][0] -=1
                            slang[f][1] = slang[f-1][1]
                        else:
                            if slang[f-1][1] - slang[f][1] > 1:
                                slang[f][1] +=1
                                slang[f][0] = slang[f-1][0]
                            else:
                                if slang[f-1][1] - slang[f][1] < -1:
                                    slang[f][1] -=1
                                    slang[f][0] = slang[f-1][0]
            lst.append(slang[-1][0]*1000+slang[-1][1])
    return len(set(lst))

print('deel 1:', day09(2))

print('deel 2:', day09(10))

print("--- %s seconds ---" % (time.time() - start_time))