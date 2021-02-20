def reverse_integer(x):
 sign = -1 if x < 0 else 1
 x *= sign

 # Removing leading zero in reverse int

 while x:
  if x % 10 == 0:
   x /= 10
  else:
   break

 #string manipulator 

 x = str(x)
 lst = list(x) #list('1234') returns['2','3','4']
 lst.reverse()

 x = "".join(lst)
 x = int(x)
 return sign * x   