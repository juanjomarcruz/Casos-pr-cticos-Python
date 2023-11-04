'''Define una función que tome dos números y retorne su suma.'''
def suma(a,b):
  print(a+b)
suma(8,9)
'''Define una función que tome un número y retorne su factorial.'''
def factorial(a):
  result=1
  for i in range(1,a+1):
    result*=i
  return result
print(factorial(9))
'''Define una función que tome un número y determine si es primo.'''
def es_primo(x):
  if x<=1:
    return False
  for i in range(2,x):
      if x%i==0:
        return False
  return True
print(es_primo(2))
'''Define una función que reciba una lista de números y retorne la suma
de ellos.'''
def suma(lista):
  total=0
  for numero in lista:
    total+=numero
  return total
print(suma([1,2,2,1]))
'''Define una función que reciba una cadena de texto y retorne la
cadena en reversa.'''
def reverse(string):
  return string[::-1]
print (reverse('Hola'))
