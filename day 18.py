import time
import copy

start_time = time.time()

test = False

def dfs_iterative(): 
    queue = []
    row = len(ruimte)
    col = len(ruimte[0])
    dep = len(ruimte[0][0])
    queue.append((0,0,0))

    while queue:
        m = queue.pop(0)
        if ruimte[m[0]][m[1]][m[2]] == 0:
            ruimte[m[0]][m[1]][m[2]] = 1
            ruimte2[m[0]][m[1]][m[2]] = 1
            if m[0]>0: queue.append((m[0]-1,m[1],m[2]))
            if m[1]>0: queue.append((m[0],m[1]-1,m[2]))
            if m[2]>0: queue.append((m[0],m[1],m[2]-1))
            if m[0]<row-1: queue.append((m[0]+1,m[1],m[2]))
            if m[1]<col-1: queue.append((m[0],m[1]+1,m[2]))
            if m[2]<dep-1: queue.append((m[0],m[1],m[2]+1))

if test:
    with open('C:/Users/fbukman/OneDrive - Capgemini/Desktop/pgm/VS/AoC2021/2022/day 18 tt.txt') as fp:
        lines = fp.readlines()
        lines=[line.rstrip() for line in lines]
else:
    with open('C:/Users/fbukman/OneDrive - Capgemini/Desktop/pgm/VS/AoC2021/2022/day 18.txt') as fp:
        lines = fp.readlines()
        lines=[line.rstrip() for line in lines]


sts = []
for line in lines:
    st = tuple([int(x) for x in (line.split(','))])
    sts.append(st)
    
som = 0
for st in sts:
    if (st[0]+1, st[1], st[2]) in sts: som+=1
    if (st[0], st[1]+1, st[2]) in sts: som+=1
    if (st[0], st[1], st[2]+1) in sts: som+=1

print('deel 1:', len(sts)*6-2*som)

ruimte = [[[0 for i in range(23)] for j in range(23)] for k in range(23)]
ruimte2 = copy.deepcopy(ruimte)

for st in sts: ruimte[st[0]][st[1]][st[2]] = 1

dfs_iterative()
som2 = 0
for st in sts:
    if ruimte2[st[0]-1][st[1]][st[2]] == 1: som2+=1
    if ruimte2[st[0]+1][st[1]][st[2]] == 1: som2+=1
    if ruimte2[st[0]][st[1]-1][st[2]] == 1: som2+=1
    if ruimte2[st[0]][st[1]+1][st[2]] == 1: som2+=1
    if ruimte2[st[0]][st[1]][st[2]-1] == 1: som2+=1
    if ruimte2[st[0]][st[1]][st[2]+1] == 1: som2+=1

print('deel 2:', som2)

print("--- %s seconds ---" % (time.time() - start_time))