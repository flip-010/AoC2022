import time
from collections import deque

start_time = time.time()

test = False

if test:
    with open('C:/Users/fbukman/OneDrive - Capgemini/Desktop/pgm/VS/AoC2021/2022/day 20 tt.txt') as fp:
        lines = fp.readlines()
        lines=[line.rstrip() for line in lines]
else:
    with open('C:/Users/fbukman/OneDrive - Capgemini/Desktop/pgm/VS/AoC2021/2022/day 20.txt') as fp:
        lines = fp.readlines()
        lines=[line.rstrip() for line in lines]

def f_p():
    for itm in lst0:
        print(itm[1], end=' ')
    print(' ')
def f_p1():
    for itm in lst1:
        print(itm[1], end=' ')
    print(' ')

lst0 = deque()

for i, line in enumerate(lines):
    lst0.append((i,int(line)))

for i, line in enumerate(lines):
#    ix0 = lst0.index((i,int(line)))
    lst0.rotate(-lst0.index((i,int(line))))
    lst0.popleft()
    lst0.rotate(-int(line))
    lst0.append((i,int(line)))
    

for i, v in lst0:
    if v == 0: break

ix = lst0.index((i,v))
a1000 = lst0[(ix+1000)%len(lines)][1] + lst0[(ix+2000)%len(lines)][1] + lst0[(ix+3000)%len(lines)][1]

print('deel 1:', a1000)
dk = 811589153
lst1 = deque()

for i, line in enumerate(lines):
    lst1.append((i,line))

for _ in range(10):
    for i, line in enumerate(lines):
        lst1.rotate(-lst1.index((i,line)))
        lst1.popleft()
        lst1.rotate(-(dk*int(line)) % (len(lines)-1))
        lst1.append((i,line))

for i, v in lst1:
    if int(v) == 0: break
ix = lst1.index((i,v))
a1000 = int(lst1[(ix+1000)%len(lines)][1]) + int(lst1[(ix+2000)%len(lines)][1]) + int(lst1[(ix+3000)%len(lines)][1])

print('deel 2:', dk*a1000)

print("--- %s seconds ---" % (time.time() - start_time))