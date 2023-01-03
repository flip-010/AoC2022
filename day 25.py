import time
import math

start_time = time.time()
test = False

if test:
    with open('C:/Users/fbukman/OneDrive - Capgemini/Desktop/pgm/VS/AoC2021/2022/day 25 tt.txt') as fp:
        lines=[line.rstrip() for line in fp.readlines()]
else:
    with open('C:/Users/fbukman/OneDrive - Capgemini/Desktop/pgm/VS/AoC2021/2022/day 25.txt') as fp:
        lines=[line.rstrip() for line in fp.readlines()]

digits = {
    '=' : -2,
    '-': -1,
    '0': 0,
    '1': 1,
    '2': 2
}
digitsvv = {
    -2: '=',
    -1: '-',
    0: '0',
    1: '1',
    2: '2'
}

som = sum(sum(pow(5,len(x)-i-1)*digits[c] for i, c in enumerate(x)) for x in lines)

print('deel 1:', som, end=' ')

exp = math.ceil(math.log(som // 2, 5))+1
snafu = ''
for i in range(exp):
    fact = pow(5,exp-i-1)
    tus2 = (som + (fact // 2)) // fact
    som -= tus2*fact
    snafu+=digitsvv[tus2]

print(snafu)

print("--- %s seconds ---" % (time.time() - start_time))