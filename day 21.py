import time
from numpy import Inf

start_time = time.time()
test = False

def f_get(aap):
    if len(lst[aap][1]) == 1:
        return lst[aap][0]
    else:
        v1 = f_get(lst[aap][1][0])
        v2 = f_get(lst[aap][1][2])
        if lst[aap][1][1] == '+': v1 += v2
        if lst[aap][1][1] == '-': v1 -= v2
        if lst[aap][1][1] == '*': v1 *= v2
        if lst[aap][1][1] == '/': v1 = v1 // v2
        return v1

if test:
    with open('C:/Users/fbukman/OneDrive - Capgemini/Desktop/pgm/VS/AoC2021/2022/day 21 tt.txt') as fp:
        lines = fp.readlines()
        lines=[line.rstrip() for line in lines]
else:
    with open('C:/Users/fbukman/OneDrive - Capgemini/Desktop/pgm/VS/AoC2021/2022/day 21.txt') as fp:
        lines = fp.readlines()
        lines=[line.rstrip() for line in lines]

lst = {}

for line in lines:
    rest = line[6:].split(' ')
    if len(rest) == 1: v = int(rest[0])
    else: v = Inf
    lst[line[:4]] = [v, rest]

print('deel 1:', f_get('root'))

aap1 = lst['root'][1][0]
aap2 = lst['root'][1][2]

#aanname: aap2 is fixed, aap1 wijzigt als humn wijzigt
doel = f_get(aap2)
tussen1 = f_get(aap1)
delta = doel - tussen1
stap = lst['humn'][0]

teller = 0
while delta != 0 and teller < 100:
    teller +=1
    lst['humn'][0] += stap
    tussen2 = f_get(aap1)
    delta = doel - tussen2
    stap = stap * delta // (tussen2 - tussen1)
    tussen1 = tussen2

# er blijken meerdere antoorden goed te zijn. door onderstaande zoek je de laagste
while f_get(aap1) == doel and teller < 100:
    teller +=1
    lst['humn'][0] -= 1
lst['humn'][0] += 1

print('deel 2:', lst['humn'][0])

print("--- %s seconds ---" % (time.time() - start_time))