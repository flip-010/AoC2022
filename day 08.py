import time

start_time = time.time()

with open('C:/Users/fbukman/OneDrive - Capgemini/Desktop/pgm/VS/AoC2021/2022/day 08.txt') as fp:
    lines = fp.readlines()
    lines=[line.rstrip() for line in lines]

print('deel 1:', 'in excel')

som = 0
for i in range(1,98):
    for j in range(1,98):
        w = int(lines[i][j])
        t1, t2, t3, t4 = 1,1,1,1
        a = i - 1
        while a > 0 and w > int(lines[a][j]):
            a -= 1
            t1 += 1
        a = i + 1
        while a < 98 and w > int(lines[a][j]):
            a += 1
            t2 += 1
        a = j - 1
        while a > 0 and w > int(lines[i][a]):
            a -= 1
            t3 += 1
        a = j + 1
        while a < 98 and w > int(lines[i][a]):
            a += 1
            t4 += 1
        som = max(som, t1*t2*t3*t4)
print('deel 2:', som)

print("--- %s seconds ---" % (time.time() - start_time))