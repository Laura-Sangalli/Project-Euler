# find the biggest prime factor of 600851475143 
x = 600851475143
i=2

while i < x:
    if x % i == 0:
        x = x / i
        i = 2 
    i += 1   
print(x)