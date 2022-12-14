import time
import re

start_time = time.time()

with open('C:/Users/fbukman/OneDrive - Capgemini/Desktop/pgm/VS/AoC2021/2022/day 11.txt') as fp:
    lines = fp.readlines()
    lines=[line.rstrip() for line in lines]

monkeys = []
monk = []
nr = 0
divi = 1

for line in lines:
    if line == '':
        monk.append(0)
        monkeys.append(monk)
    if line[:6] == "Monkey":
        monk = []
    if line[:9] == "  Startin":
        a = line.split(': ')
        lst = [int(x) for x in a[1].split(", ")]
        monk.append(lst)
    if line[:9] == "  Operati":
        a = line.split(': ')
        lst = a[1].split(" ")
        monk.append(lst)
    if line[:6] == "  Test":
        lst = line.split("  Test: divisible by ")
        monk.append(int(lst[1]))
        divi *= int(lst[1])
    if line[:9] == "    If tr":
        lst = line.split("    If true: throw to monkey ")
        monk.append(int(lst[1]))
    if line[:9] == "    If fa":
        lst = line.split("    If false: throw to monkey ")
        monk.append(int(lst[1]))

monk.append(0)
monkeys.append(monk)

for round in range(20):
    m = 0
    for mm in range(len(monkeys)):
        monk = monkeys[m]
        for item in monk[0]:
            if monk[1][4] == 'old': fact = item
            else: fact = int(monk[1][4])
            if monk[1][3] == '*': new = item * fact
            else: new = item + fact
            new = new // 3
            if new % monk[2] == 0:
                monkeys[monk[3]][0].append(new)
            else:
                monkeys[monk[4]][0].append(new)
            monkeys[m][5] +=1
        monkeys[m][0] = []
        m+=1

mx1 = []

for monk in monkeys:
    mx1.append(monk[5])

mx1.sort(reverse = True)


print('deel 1:', mx1[0], mx1[1], mx1[0]*mx1[1])

monkeys = []
monk = []
nr = 0
divi = 1

for line in lines:
    if line == '':
        monk.append(0)
        monkeys.append(monk)
    if line[:6] == "Monkey":
        monk = []
    if line[:9] == "  Startin":
        a = line.split(': ')
        lst = [int(x) for x in a[1].split(", ")]
        monk.append(lst)
    if line[:9] == "  Operati":
        a = line.split(': ')
        lst = a[1].split(" ")
        monk.append(lst)
    if line[:6] == "  Test":
        lst = line.split("  Test: divisible by ")
        monk.append(int(lst[1]))
        divi *= int(lst[1])
    if line[:9] == "    If tr":
        lst = line.split("    If true: throw to monkey ")
        monk.append(int(lst[1]))
    if line[:9] == "    If fa":
        lst = line.split("    If false: throw to monkey ")
        monk.append(int(lst[1]))

monk.append(0)
monkeys.append(monk)

for round in range(10000):
    m = 0
    for mm in range(len(monkeys)):
        monk = monkeys[m]
        for item in monk[0]:
            if monk[1][4] == 'old': fact = item
            else: fact = int(monk[1][4])
            if monk[1][3] == '*': new = item * fact
            else: new = item + fact
            new = new % divi
            if new % monk[2] == 0:
                monkeys[monk[3]][0].append(new)
            else:
                monkeys[monk[4]][0].append(new)
            monkeys[m][5] +=1
        monkeys[m][0] = []
        m+=1

mx1 = []

for monk in monkeys:
    mx1.append(monk[5])

mx1.sort(reverse = True)


print('deel 2:', mx1[0], mx1[1], mx1[0]*mx1[1])

print("--- %s seconds ---" % (time.time() - start_time))