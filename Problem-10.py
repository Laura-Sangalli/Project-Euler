# find the sum of all the prime numbers bellow two million
import math
import numpy as np

def find_primes(conj):
  for num in range(2, len(conj)):
      # se o numero continuar sendo primo ate o  valor de sua raiz quadrada, incluindo ela, então
      # ele será obrigatoriamente primo
      limit = math.ceil(math.sqrt(num)) 
      for divisor in range(2, limit+1):
          if num / divisor == 0:
            conj[num] = 0
  return sum_primes(conj)

def sum_primes(conj):
  soma = 0
  for i in range(len(conj)):
    if conj[i] == 1:
      soma += i
  
  return soma



conj = np.ones(2000000)
conj[1] = conj[0] = 0
find_primes(conj)
    
