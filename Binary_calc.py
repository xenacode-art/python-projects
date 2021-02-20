def decimal(x):
 x = list(str(x))
 x=x[::-1]
 product = 0
 for b in range(len(x)):
  product += int(x[b]) * 2 ** b
 return product


def binary(x):
 bits = []
 bit = ""

 while x > 0:
     bits.append(x % 2)
     x = x// 2
 bits = bits[:: -1]
 for x in bits:
   bits += str(x)

 return bit      
 
print(decimal("1011011010"))
#print(binary(730))  