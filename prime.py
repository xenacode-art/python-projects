import time


print("-" * 35)
print("Prime-Check " * 3)
print("-" * 35)

while True:

 time.sleep(2)
  
 number = int(input("Enter The Number: "))

 if number > 1:
    for i in range(2,int(number/2)+1):
        if (number % i == 0):
            print(number, "is not a Prime Number \n")
            break
    else:
        print(number,"is a Prime number \n")
# If the number is less than 1 it can't be Prime    
 else:
    print(number,"is not a Prime number \n")

'''
try:
 (ValueError)

 except
  print("Strings Not Allowed!!! ")
'''  
  