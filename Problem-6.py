# this program find the diference between the sum of the squares and the square of the sum
# of the first one hundred natural numbers  
import math

numeros = []
numeros_ao_quadrado = []
for n in range(1, 101):
    numeros.append(n)

for n in numeros:
    numeros_ao_quadrado.append(n**2)

a  = sum(numeros_ao_quadrado) 

b = sum(numeros)**2

print(abs(a - b))