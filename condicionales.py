'''Dado un número, imprime si es positivo o negativo.'''
a = -1
if a >= 0:
  print('El número es positivo')
else:
  print('El número es negativo')
'''Dado un número, imprime si es par o impar.'''
b = 3
if b%2==0:
  print('El número es par')
else:
  print('El número es impar')
'''Dado tres números, encuentra y muestra el mayor de ellos.'''
numeros =[1,5,2]
maximo = numeros[0]
for numero in numeros:
  if numero > maximo:
    maximo = numero
print(maximo)