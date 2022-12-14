import time
import re
import heapq
from numpy import Inf

def c_pos(c,r):
    global rows, cols
    if c<0 or r<0 or c>=cols or r>=rows: return False
    return True

def f_graaf():
    global rows, cols, S, E
    for r in range(rows):
        for c in range(cols):
            lst = []
            if c_pos(c-1,r): 
                if (ord(veld[r][c])-ord(veld[r][c-1])) >= -1:
                    lst.append((c - 1 + r * cols, 1))
            if c_pos(c+1, r):  
                if (ord(veld[r][c])-ord(veld[r][c+1])) >= -1:
                    lst.append((c + 1 + r * cols, 1))
            if c_pos(c, r-1):  
                if (ord(veld[r][c])-ord(veld[r-1][c])) >= -1:
                    lst.append((c + (r-1) * cols, 1))
            if c_pos(c, r+1):  
                if (ord(veld[r][c])-ord(veld[r+1][c])) >= -1:
                    lst.append((c + (r+1) * cols, 1))
            graaf[c+r*cols] = lst

def f_graaf2():
    global rows, cols, S, E
    for c in range(cols):
        for r in range(rows):
            lst = []
            if c_pos(c-1,r): 
                if (ord(veld[r][c])-ord(veld[r][c-1])) <= 1:
                    lst.append((c - 1 + r * cols, 1))
            if c_pos(c+1, r):  
                if (ord(veld[r][c])-ord(veld[r][c+1])) <= 1:
                    lst.append((c + 1 + r * cols, 1))
            if c_pos(c, r-1):  
                if (ord(veld[r][c])-ord(veld[r-1][c])) <= 1:
                    lst.append((c + (r-1) * cols, 1))
            if c_pos(c, r+1):  
                if (ord(veld[r][c])-ord(veld[r+1][c])) <= 1:
                    lst.append((c + (r+1) * cols, 1))
            graaf[c+r*cols] = lst

            
def f_dijkstra(graaf, root):
    n = len(graaf)
    dist = [Inf for _ in range(n)]
    dist[root] = 0
    visited = [False for _ in range(n)]
    pq = [(0, root)]
    while len(pq) > 0:
        _, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        for v, l in graaf[u]:
            if dist[u] + l < dist[v]:
                dist[v] = dist[u] + l
                heapq.heappush(pq, (dist[v], v))
    return dist

start_time = time.time()

with open('C:/Users/fbukman/OneDrive - Capgemini/Desktop/pgm/VS/AoC2021/2022/day 12.txt') as fp:
    lines = fp.readlines()
    lines=[line.rstrip() for line in lines]

rows = len(lines)
cols = len(lines[0])
veld = [['.' for i in range(cols)] for j in range(rows)]
graaf = {}
S = 0
E = 0

for r in range(rows):
    for c in range(cols):
        veld[r][c] = lines[r][c]
        if veld[r][c] == 'S': 
            veld[r][c] = 'a'
            S = c+r*cols
        if veld[r][c] == 'E': 
            veld[r][c] = 'z'
            E = c+r*cols

f_graaf()
res = f_dijkstra(graaf, S)

print('deel 1:', res[E])

graaf = {}
f_graaf2()

res2 = f_dijkstra(graaf, E)
mi = res[E]
for r in range(rows):
    for c in range(cols):
        if veld[r][c] == 'a':
            mi = min(res2[c+r*cols],mi)

print('deel 2:', mi)

print("--- %s seconds ---" % (time.time() - start_time))
