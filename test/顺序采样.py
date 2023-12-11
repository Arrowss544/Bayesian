import random
import math
l={'A':1,'B':1,'C':1}
cpt={'A':[0.5,[]],'B':[0.6,0.4,['A']],'C':[0.4,0.6,['B']]}
#固定A=1，查询C
rp=0.48
q=40000
n=0
m=0
for i in range(q):
    if l['C']==1:
        n=n+1
    if m == 0:
        m=1
        p=random.randint(1,10)
        if p <= 4:
            l['B']=1
        else:
            l['B']=0
    if m == 1:
        m = 0
        p = random.randint(1, 10)
        if l['B'] ==1:
            if p <= 6:
                l['C'] = 1
            else:
                l['C'] = 0
        else:
            if p <= 4:
                l['C'] = 1
            else:
                l['C'] = 0
print(n/q)
print((n/q-rp)/rp)
