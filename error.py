class ValueTooHighError(Exception):
      pass
   
def test_value(x):
    x = int(input("Enter value: "))
    if x > 100:
     raise ValueTooHighError('value is too high')
   
try:
    test_value(200)     
except ValueTooHighError as e:
    print(e)

'''x = -5

if x < 0:
 raise Exceptionerror('x is not positive')
#assert(x >= 0),'x is not positive'
'''