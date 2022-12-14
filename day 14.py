import time

start_time = time.time()

with open('C:/Users/fbukman/OneDrive - Capgemini/Desktop/pgm/VS/AoC2021/2022/day 14.txt') as fp:
    lines = fp.readlines()
    
my = 0
for line in lines:
    for tt in line.split(' -> '):
        cx, cy = (int(x) for x in tt.split(','))
        my=max(my,cy)

yrange, xrange = my+5, 2*(my+5)
veld = [['.' for i in range(yrange)] for j in range(xrange)]
dif = 500-xrange//2

def f_c(x,y,d):
    global my
    if y > my and d == 1: return False
    if veld[x][y+1] == '.': return f_c(x,y+1, d)
    if veld[x-1][y+1] == '.': return f_c(x-1,y+1, d)
    if veld[x+1][y+1] == '.': return f_c(x+1,y+1, d)
    if y == 0: return False
    veld[x][y]='o'
    return True

for line in lines:
    ox, oy = 0, 0
    for tt in line.split(' -> '):
        cx, cy = (int(x) for x in tt.split(','))
        if ox != 0:
            for x in range(min(ox, cx),max(ox, cx)+1):
                for y in range(min(oy, cy),max(oy, cy)+1):
                    veld[x-dif][y] = '#'
        ox, oy = cx, cy

a = 0
while f_c(500-dif,0,1): a+=1

print('deel 1:', a)

for i in range(xrange): veld[i][my+2]='#'
while f_c(500-dif,0,2): a+=1

print('deel 2:', a+1)  #puntje van de boom nog meetellen, vandaar a+1

print("--- %s seconds ---" % (time.time() - start_time))
