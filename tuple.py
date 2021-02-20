import sys
mylist = [0,1,2,3, 'hello',True]
mytuple = (0,1,2,3, 'hello',True)

#del mylist[0,1,2,]


print(sys.getsizeof(mylist),'bytes')
print(sys.getsizeof(mytuple),'bytes')

