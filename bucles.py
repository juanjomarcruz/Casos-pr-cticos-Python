'''Imprime los números del 1 al 10 usando un bucle for '''
for i in range(10):
  print(i+1)
'''Imprime los números pares del 1 al 20 usando un bucle while .'''
numeros = range(21)
i = 1
while i < len(numeros):
  if numeros[i]%2==0:
    print(numeros[i])
  i+=1
'''Usa un bucle para calcular la suma de los números del 1 al 100.'''
total = 0
for i in range(101):
  total+=i
print(total)
