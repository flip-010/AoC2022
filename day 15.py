import time
import re

start_time = time.time()

with open('C:/Users/fbukman/OneDrive - Capgemini/Desktop/pgm/VS/AoC2021/2022/day 15.txt') as fp:
    lines = fp.readlines()
    lines=[line.rstrip() for line in lines]
    
my = 0
y=11
y=2000000
mx=4000000
#mx=20
set = []
xm0, xm1 = 0, 0
for line in lines:
    tt = re.split(' |=|,|:', line)
    s = (int(tt[3]), int(tt[6]))
    b = (int(tt[13]), int(tt[16]))
    a = abs(s[0]-b[0]) + abs(s[1]-b[1])
    t=abs(s[1]-y)
    if a-t>=0:
        g=a-t
    else:
        g=-1
    if g>=0:
        x0 = s[0]-g
        x1 = s[0]+g
        set.append((max(0,x0),min(mx,x1)))
    else:
        x0, x1 = 0, 0
    xm0 = min(xm0,x0)
    xm1 = max(xm1,x1)


print('deel 1:', xm1-xm0)

coor=[]
for line in lines:
    tt = re.split(' |=|,|:', line)
    s = (int(tt[3]), int(tt[6]))
    b = (int(tt[13]), int(tt[16]))
    a = abs(s[0]-b[0]) + abs(s[1]-b[1])
    coor.append([s,a])

count = 0
y=mx//2
while count == 0 and y<=mx:
    y+=1
    set = []
    for [s, a] in coor:
        t=abs(s[1]-y)
        if a-t>=0:
            g=a-t
            x0 = s[0]-g
            x1 = s[0]+g
            set.append((max(0,x0),min(mx,x1)))

    set.sort()
    m=1
    for s in set:
        if s[0]<=m:
            m = max(m,s[1])
        else:
            count += 1
            break
    # s0 = list(set[0])
    # for s in set:
    #     if s[0]<=s0[1]:
    #         s0[1] = max(s0[1],s[1])
    #     else:
    #         print(y,s0,s)
    #         break

print('deel 2:', y,m+1,y + 4000000*(m+1))

#print('deel 2:', y,s0[1]+1,y + 4000000*(s0[1]+1))

print("--- %s seconds ---" % (time.time() - start_time))