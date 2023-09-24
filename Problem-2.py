# sum of the even-numbers bellow 4000000 in the Fibonacci Sequence.
a = 1
b = 1
c = a + b
soma = 0
soma += c 
while c <= 4000000:
    a = b
    b = c
    c = a + b
    if c % 2 == 0:
        soma += c

print(soma)

