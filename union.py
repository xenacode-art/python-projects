odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7,9}

u = odds.union(evens)
print("union =" , u)

i = primes.intersection(evens)
print("intersections = ",i)