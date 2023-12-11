import random
import math
l={'A':1,'B':1,'C':1}
cpt={'A':[0.5,[]],'B':[0.6,0.4,['A']],'C':[0.4,0.6,['B']]}
n=0
q=100000
rp=0.48
for i in range(q):
    if l['C'] == 1:
        n = n + 1
    m = random.randint(0, 1)
    if m == 0 and l['C'] == 1:
        p = random.randint(0, 1)
        if p == 0:
            l['B'] = 0
        else:
            l['B'] = 1
    if m == 0 and l['C'] == 0:
        p = random.randint(1, 10000)
        if p <= 6923:
            l['B'] = 0
        else:
            l['B'] = 1
    if m == 1 and l['B'] == 1:
        p = random.randint(1, 10)
        if p <= 4:
            l['C'] = 0
        else:
            l['C'] = 1
    if m == 1 and l['B'] == 0:
        p = random.randint(1, 10)
        if p <= 6:
            l['C'] = 0
        else:
            l['C'] = 1
print(n/q)
print(((n/q)-rp)/rp)

