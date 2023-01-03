import time
import copy

start_time = time.time()
test = False

def f_c8(x,y):
    aa = veld[x-1][y-1] + veld[x-1][y] + veld[x-1][y+1] + veld[x][y-1] + veld[x][y+1] + veld[x+1][y-1] + veld[x+1][y] + veld[x+1][y+1]
    if aa == 0:
        return True
    else:
        return False

#volgorde:
# 0 = N is eerste pos -1
# 1 = Z is eerste pos +1
# 2 = W is tweede pos -1
# 3 = O is tweede pos +1
def f_cr(r,x,y):
    if r == 0:
        aa = veld[x-1][y-1] + veld[x-1][y] + veld[x-1][y+1]
        if aa == 0: return x-1, y
        else: return x, y
    if r == 1:
        aa = veld[x+1][y-1] + veld[x+1][y] + veld[x+1][y+1]
        if aa == 0: return x+1, y
        else: return x, y
    if r == 2:
        aa = veld[x-1][y-1] + veld[x][y-1] + veld[x+1][y-1]
        if aa == 0: return x, y-1
        else: return x, y
    if r == 3:
        aa = veld[x-1][y+1] + veld[x][y+1] + veld[x+1][y+1]
        if aa == 0: return x, y+1
        else: return x, y

if test:
    with open('C:/Users/fbukman/OneDrive - Capgemini/Desktop/pgm/VS/AoC2021/2022/day 23 tt.txt') as fp:
        lines = fp.readlines()
        lines=[line.rstrip() for line in lines]
else:
    with open('C:/Users/fbukman/OneDrive - Capgemini/Desktop/pgm/VS/AoC2021/2022/day 23.txt') as fp:
        lines = fp.readlines()
        lines=[line.rstrip() for line in lines]

ref = len(lines[0])
veld = [[0 for i in range(ref*3)] for j in range(ref*3)]
veldempty = copy.deepcopy(veld)
checkline = veld[0].copy()

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == '#':
            veld[i+ref][j+ref]=1

richt = 0
door = True
rondje = 0
while door and rondje < 30000:
    rondje+=1
    door = False
    veld2 = copy.deepcopy(veldempty)
    veld3 = copy.deepcopy(veldempty)
# deel 1: check een zet en schrijf de gewenste zet in cel van veld2 +1
    for i in range(1, len(veld)-1):
        for j in range(1, len(veld[i])-1):
            if veld[i][j] == 1:
                if f_c8(i,j):
                    veld2[i][j] +=1
                else:
                    i1, j1 = f_cr(richt, i, j)
                    if i1 == i and j1 == j:
                        i1, j1 = f_cr((richt+1)%4, i, j)
                        if i1 == i and j1 == j:
                            i1, j1 = f_cr((richt+2)%4, i, j)
                            if i1 == i and j1 == j:
                                i1, j1 = f_cr((richt+3)%4, i, j)
                    veld2[i1][j1] +=1

# deel 2: doe dit nog eens. Is de gewenste zet naar een cel van veld2 met waarde 1? dan doe de zet naar veld3
    for i in range(1, len(veld)-1):
        for j in range(1, len(veld[i])-1):
            if veld[i][j] == 1:
                if f_c8(i,j):
                    veld3[i][j] +=1
                else:
                    i1, j1 = f_cr(richt, i, j)
                    if i1 == i and j1 == j:
                        i1, j1 = f_cr((richt+1)%4, i, j)
                        if i1 == i and j1 == j:
                            i1, j1 = f_cr((richt+2)%4, i, j)
                            if i1 == i and j1 == j:
                                i1, j1 = f_cr((richt+3)%4, i, j)
                    if veld2[i1][j1] ==1:
                        door = True
                        veld3[i1][j1] = 1
                    else:
                        veld3[i][j] = 1
# slot: haal alles over naar veld
    veld = copy.deepcopy(veld3)
    richt = (richt+1)%4
    if rondje == 10: #vanwege deel 1 van opdracht
        r1, c1 = ref*3, ref*3
        r2, c2 = 0, 0
        cnt = 0
        for i in range(len(veld)):
            firstrow = 0
            for j in range(len(veld[i])):
                if veld[i][j] == 1:
                    r1 = min(i, r1)
                    c1 = min(j, c1)
                    r2 = max(i, r2)
                    c2 = max(j, c2)
                    cnt+=1

print('deel 1:',(r2-r1+1)*(c2-c1+1) - cnt)
print('deel 2:', rondje)

print("--- %s seconds ---" % (time.time() - start_time))