import math as m

value = 1
x = 1
while x <= 20:
    value *= x // m.gcd(x, value)
    x+=1

print(value)



        
    