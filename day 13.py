import time
import ast
import re
from copy import copy


start_time = time.time()

with open('C:/Users/fbukman/OneDrive - Capgemini/Desktop/pgm/VS/AoC2021/2022/day 13.txt') as fp:
    lines = fp.readlines()
    lines=[line.rstrip() for line in lines]


def f_c(obj1, obj2):
    obja = copy(obj1)
    objb = copy(obj2)
    if len(obja) == 0: return True
    if len(objb) == 0: return False
    if obja[0] == objb[0]: return f_c(obja[1:],objb[1:])
    if type(obja[0]) == int and type(objb[0]) == int: 
        if obja[0] < objb[0]: return True
        if obja[0] > objb[0]: return False
    if type(obja[0]) == list and type(objb[0]) == list: return f_c(obja[0],objb[0])
    if type(obja[0]) == int: return f_c([obja[0]],objb[0])
    if type(objb[0]) == int: return f_c(obja[0],[objb[0]])
    print('fout')
    return False

def sort(alist):
    blist = copy(alist)
    length = len(blist) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(length):
            if not f_c(blist[i], blist[i+1]):
                sorted = False
                blist[i], blist[i+1] = blist[i+1], blist[i]
    return blist

num = 1
som  = 0
lst = []

for i in range(0, len(lines), 3):

    obj1 = ast.literal_eval(lines[i])
    obj2 = ast.literal_eval(lines[i+1])
    lst.append(obj1)
    lst.append(obj2)
    if f_c(obj1, obj2):
        som+=num
    num+=1

print('deel 1:', num, som)

a = [[2]]
b = [[6]]

lst.append(a)
lst.append(b)
lst = sort(lst)
num = 0
som = 1
for item in lst:
    num+=1
    print(num,item)
    if item == a: som*=num
    if item == b: som*=num

print('deel 2:', som)
print('antwoord deel 2 is fout, wel handmating op de juiste plaats gezet, nl 112 en 199')

print(lst[199])
print(lst[200])
print(f_c(lst[200],lst[199]))

print("--- %s seconds ---" % (time.time() - start_time))