'''from collections import namedtuple

Point = namedtuple('Point', 'x,y')

pt = Point(1 ,-4)
print(pt)'''
'''
from collections import defaultdict

d = defaultdict(float)

#d={int}

d ['a']=1
d ['b']=2
d ['c']=3
print(d['e'])'''
'''
from itertools import product
a=[1,2]
b=[3]

prod=product(a,b,repeat=2)
print(list(prod))'''

from itertools import combinations

a=[1,2,3,4]

perm=combinations(a, 2)
print(tuple(perm))