import time
import re

start_time = time.time()

with open('C:/Users/fbukman/OneDrive - Capgemini/Desktop/pgm/VS/AoC2021/2022/day 10.txt') as fp:
    lines = fp.readlines()
    lines=[line.rstrip() for line in lines]

def f_check():
    global x
    global i
    global som
    global s
    
    if abs(x-((i-1) % 40)) <= 1:
        s = s + '█'
    else:
        s = s + ' '

    if  (i+20) % 40 == 0:
        som += (x*i)
    if  i % 40 == 0:
        print(s)
        s = '' 
    i+=1

som = 0
i = 1
x = 1
s = ''

for line in lines:
    a = line.split(" ")
    if a[0] == 'addx': 
        f_check()
        f_check()
        x += int(a[1])
    else:
        f_check()

print('deel 1:', som)

print('deel 2:', 'Zie boven')

print("--- %s seconds ---" % (time.time() - start_time))