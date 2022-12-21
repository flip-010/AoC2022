import time
import re
import heapq
from numpy import Inf

start_time = time.time()

test = False

if test:
    with open('C:/Users/fbukman/OneDrive - Capgemini/Desktop/pgm/VS/AoC2021/2022/day 17 tt.txt') as fp:
        lines = fp.readlines()
        lines=[line.rstrip() for line in lines]
else:
    with open('C:/Users/fbukman/OneDrive - Capgemini/Desktop/pgm/VS/AoC2021/2022/day 17.txt') as fp:
        lines = fp.readlines()
        lines=[line.rstrip() for line in lines]

invoer = lines[0]

def f_c(bl,li, co):
    for a in range(4):
        for b in range(4):
            if blok[bl][a][b] == '#' and veld[li+a][co+b] == '#': return False
    return True
def f_copy(bl,li, co):
    for a in range(4):
        for b in range(4):
            if blok[bl][a][b] == '#': 
                veld[li+a] = veld[li+a][:co+b] + '#' + veld[li+a][co+b+1:]


if test:
    rows = 406800
    cols = 7
else:
    rows = 406800
    cols = 7



rij = '#'+'.' * cols+'#'

blok = [['....' for i in range(4)] for j in range(5)]
veld = [rij for j in range(rows)]
veld[0] = '#'+'#' * cols+'#'

print(blok)
blok[0][0] = '####'
blok[1][0] = '.#..'
blok[1][1] = '###.'
blok[1][2] = '.#..'
blok[2][2] = '..#.'
blok[2][1] = '..#.'
blok[2][0] = '###.'
blok[3][0] = '#...'
blok[3][1] = '#...'
blok[3][2] = '#...'
blok[3][3] = '#...'
blok[4][0] = '##..'
blok[4][1] = '##..'

# for i in range(4):
#     for j in range(4):
#         print(blok[i][j])
#     print('')

bl = 0
ri = 0

if test:
    rocks = 2022
else:
    rocks = 2022 

rocks = 1*7*len(invoer)
rocks += 43618
print('rocks: ', rocks)
blokline=0

for runs in range(rocks):
    startline = blokline
    while veld[startline] != rij:
        startline+=1
    blokline = startline+3

    h = 3
    door = True
    while door:
        door = False
        if f_c(bl, blokline, h):
            door = True
            if ri >= len(invoer): 
                ri = 0
            if invoer[ri] == '<' and f_c(bl, blokline, h-1):
                h -=1
            elif invoer[ri] == '>' and f_c(bl, blokline, h+1):
                h +=1
            blokline -=1
            ri+=1

    f_copy(bl,blokline+1,h)

    # for i in range(startline+3):
    #     print(veld[i])
    bl = (bl+1) % 5

# for i in range(startline+3):
#     print(veld[i])

startline = 0
while veld[startline] != rij:
    startline+=1

print('deel 1:', startline-1)

print('deel 2:', 2)

xx = 1000000000000//280
print(xx)
yy = 1000000000000%280
print(yy)
print((xx-1)*424+startline-1)
print(1514285714288)

dd2 = 220505-110263 
xx = 1000000000000//(len(invoer)*7)
print(xx)
yy = 1000000000000%(len(invoer)*7)
print(yy)
print(dd2)
print((xx-1)*dd2+startline-1)
print(1514285714288)

#Geen fraaie oplossing, deze zoek en vervang aanpak. wel het antwoord na lag wachten


print("--- %s seconds ---" % (time.time() - start_time))