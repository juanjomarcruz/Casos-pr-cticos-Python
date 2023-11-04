'''Crea una función para verificar si un número es par o impar y devuelva “El
número es par” o “El número es impar” según corresponda.'''
def paroimpar(x):
  if x%2==0:
    print(f'El {x} es par')
  else:
    print(f'El {x} es impar')
paroimpar(9)
'''Crea una función a la que pases un número como argumento, calcule el factorial
de ese número y haga print del resultado.'''
def factorial(a):
  result=1
  for i in range(1,a+1):
    result*=i
  print(result)
factorial(4)
'''Crea una función a la que se le pase un número como argumento, calcule la
cantidad de dígitos y haga print de “La cantidad de dígitos es:” y el resultado
total de dígitos.'''
def cantidad_dígitos(numero):
  print(f'La cantidad de dígitos es: {len(str(numero))}')
cantidad_dígitos(576837)
'''Dada una lista de números, crea una función que devuelva el número máximo
de la lista.'''
def num_max(numeros):
  maximo=numeros[0]
  for numero in numeros:
    if numero > maximo:
     maximo=numero
  return maximo
print(num_max([1,-1,-47,50,2]))
'''Crea una función que, dado un número, sume los dígitos de ese número y
devuelva el resultado.'''
def suma_digitos():
  x = int(input("Ingresa un número: "))
  total=0
  for i in str(x):
    total+=int(i)
  return total
print("La suma de los dígitos es:", suma_digitos())
'''Dados dos números, crea una función para encontrar el mínimo común múltiplo
(MCM) de los dos números, que se les pasarán como argumento a la función, y
devuelva el MCM.'''
def mcm(x,y):
  if x == 0 or y == 0:
    return 0
  else:
    maximo = max(x,y)
    while True:
      if maximo % x == 0 and maximo % y == 0:
        return maximo
      maximo += 1
print(mcm(46,27))
'''Crea una función a la que, pasándole la base y la altura, calcule y devuelva el
área de un triángulo.'''
def area_triangulo():
  b = int(input("Ingrese la base del tríangulo: "))
  h = int(input("Ingrese la altura del triángulo: "))
  total=(b*h)/2
  print(f"El área del triángulo es igual a: {total}")
  return total
area_triangulo()
def signo_numero(x):
  if x==0:
    print("El número ingresado es cero")
  elif x>0:
    print("El número ingresado es positivo")
  else:
    print("El número ingresado es negativo")
signo_numero(-25)
'''Crea una función que, dada una palabra, cuente la cantidad de letras en una
palabra.'''
def num_palabras():
  palabra=input("Ingresa una palabra: ")
  contador=0
  for letra in palabra:
    contador+=1
  print(f"La palabra {palabra} tiene {contador} letras")
  return contador
num_palabras()
'''Crea una función que, dada una lista de números, convierta la lista de números
a su valor absoluto.'''
def absolut(numeros):
  i=0
  for numero in numeros:
    if numero<0:
      numeros[i]*=-1
    i+=1
  print(numeros)
  return numeros
absolut([2,-1,2,0])
'''Crea una función que, dado un número, verifique si un número es primo.'''
def es_primo(x):
  if x<=1:
    return False
  for i in range(2,x):
      if x%i==0:
        return False
  return True
print(es_primo(2))
'''Dados dos números, crea una función para encontrar el máximo común divisor
(MCD) de esos dos números.'''
def mcd(a,b):
  if a==0 or b==0:
    return 0
  else:
    minimo=min(a,b)
    while True:
      if a%minimo==0 and b%minimo==0:
        return minimo
      minimo-=1
print(mcd(250,300))
'''Define una función que utilice un bucle para imprimir los primeros n
números de la serie de Fibonacci.'''
def fibonacci(x):
  secuencia=[0,1]
  for i in range(2,x):
    siguiente=secuencia[i-2]+secuencia[i-1]
    secuencia.append(siguiente)
  print(secuencia)
  return secuencia
fibonacci(7)
'''Define una función que tome un número y retorne una lista de sus
divisores.'''
def divisores(x):
  lista_divisores=[]
  for i in range(1,x+1):
    if x%i==0:
      lista_divisores.append(i)
  print(lista_divisores)
divisores(10)
'''Define una función que tome una lista y retorne una nueva lista con
los elementos únicos de la lista original.'''
def elementos_unicos(lista):
  lista_unicos = []
  for elemento in lista:
    if elemento not in lista_unicos:
      lista_unicos.append(elemento)
  return lista_unicos
elementos_unicos([1,4,2,8,8,9,3,8,9])
'''Define una función que tome un número y retorne la suma de sus
dígitos.'''
def suma_digitos():
  x = int(input("Ingresa un número: "))
  total=0
  for i in str(x):
    total+=int(i)
  return total
print("La suma de los dígitos es:", suma_digitos())
'''Define una función que tome una cadena y cuente el número de
vocales en la cadena.'''
def num_vocales(string):
  vocales =['a','e','i','o','u']
  total=0
  for letter in string:
    for vocal in vocales:
      if letter==vocal:
       total+=1
  return total
print(num_vocales('Hola'))
'''Define una función que tome una lista y un número n, y retorne los
primeros n elementos de la lista.'''
def n_elementos(lista,x):
  for i in range(x):
    print(lista[i])
n_elementos([1,4,2,'o',6,3,6],4)
'''Define una función que tome una cadena y retorne la cantidad de
letras mayúsculas y minúsculas en la cadena.'''
def upper_lower(string):
  contador_minusculas=0
  contador_mayusculas=0
  for letter in string:
    if letter.islower()==True:
      contador_minusculas+=1
    else:
      contador_mayusculas+=1
  print(f"La palabra ingresada contiene {contador_minusculas} minúsculas y {contador_mayusculas} mayúsculas")
upper_lower('HoLa')
'''Define una función que tome un número y retorne True si es un
número perfecto, False en caso contrario. Un número perfecto es aquel que es
igual a la suma de sus divisores propios positivos. Por ejemplo, 6 es un número
perfecto porque sus divisores son 1, 2 y 3, y 6 = 1 + 2 + 3.'''
def es_perfecto(x):
  lista_divisores=[]
  for i in range(1,x):
    if x%i==0:
      lista_divisores.append(i)
  print(lista_divisores)
  total=0
  for i in lista_divisores:
    total+=i
  if total == x:
    return True
  else:
    return False
print(es_perfecto(8128))
'''Define una función que reciba un número y retorne su
representación en binario.'''
def binario(x):
  if x<0:
    print("No pueden transformarse números negativos en binarios")
  elif x==0:
    print("0")
  else:
    binario=''
    while x>0:
      resto=x%2
      binario= str(resto) + binario
      x//=2
    return binario
print(binario(25))
'''Define una función que reciba dos listas y retorne la intersección de
ambas (los elementos que están en las dos listas).'''
def interseccion(lista_1,lista_2):
  for i in lista_1:
    for j in lista_2:
      if i==j:
        print(i)
interseccion([9,2,5],[1,0,5])
'''Define una función que tome una cadena y determine si es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).'''
def es_palindromo(string):
  string=string.lower()
  if string==string[::-1]:
    return True
  return False
print(es_palindromo('Reconocer'))
'''Escribe un programa que imprima los números del 1 al 50, pero para
múltiplos de tres imprima “Fizz” en lugar del número y para los múltiplos de
cinco imprima “Buzz”. Para números que son múltiplos de tanto tres como cinco
imprima “FizzBuzz”.'''
def FizzBuzz():
 for i in range(1,51):
    if i%3==0 and i%5==0:
      print("FizzBuzz")
    elif i%3==0:
      print("Fizz")
    elif i%5==0:
      print("Buzz")
    else:
      print(i)
FizzBuzz()
'''Define una función que tome una lista y retorne la lista ordenada en
orden ascendente.'''
def ascendent(lista):
  lista_ascendente=[]
  while len(lista)>0:
    minimo=min(lista)
    lista_ascendente.append(minimo)
    lista.remove(minimo)
  return lista_ascendente
print(ascendent([5,2,4,6,4,6,7,8,8]))
'''Define una función que reciba una lista de palabras y un entero n, y
retorne la lista de palabras que son más largas que n.'''
def palabras_n(lista,n):
  lista_palabras=[]
  for palabra in lista:
    if len(palabra) > n:
      lista_palabras.append(palabra)
  print(lista_palabras)
  return lista_palabras
palabras_n(['Reptiliano', 'Oca','Nevera','Ordenador'], 8)
'''Define una función que tome un número y calcule su serie de
Fibonacci.'''
def fibonacci(x):
  serie=[0,1]
  for i in range(2,x):
    serie.append(serie[i-1]+serie[i-2])
  print(serie)
  return serie
fibonacci(36)
'''Define una función que tome una lista de números y retorne el
número más grande de la lista.'''
def maximo(lista):
  maximo=lista[0]
  for element in lista:
    if element > maximo:
      maximo = element
  return maximo
maximo([1,2,0,4,6,3])
'''Define una función que reciba un número y retorne la suma de sus
dígitos al cubo.'''
def cubo(x):
  suma=0
  for digito in str(x):
    suma+=int(digito)**3
  print(suma)
cubo(71)
'''Define una función que reciba una lista de números y retorne el
segundo número más grande de la lista.'''
def segundo_máximo(lista):
  maximo=lista[0]
  for numero in lista:
    if numero > maximo:
      maximo = numero
  lista.remove(maximo)
  maximo=lista[0]
  for numero in lista:
    if numero > maximo:
      maximo = numero
  return maximo
'''Define una función que tome dos listas y retorne True si tienen al
menos un miembro en común, de lo contrario, retorne False.'''
def tienen_comun(lista_1, lista_2):
  for i in lista_1:
    for j in lista_2:
      if i==j:
        return True
  return False
print(tienen_comun(['Fernando',0,6,9],[4,2,'Fernando',1]))
'''Define una función que tome una lista y retorne una nueva lista con
los elementos de la lista original en orden inverso.'''
def inverse(lista):
  lista_inversa=lista[::-1]
  return lista_inversa
print(inverse(['Juan','García', 'Ruiz']))
'''Define una función que reciba una cadena y cuente el número de
dígitos y letras que contiene.'''
def contador_letras_numeros(string):
  contador_numeros = 0
  contador_letras = 0
  for element in string:
    if element.isdigit():
      contador_numeros+=1
    else:
      contador_letras+=1
  print(f'La cadena tiene {contador_numeros} dígitos y {contador_letras} letras')
contador_letras_numeros('Hola4')
'''Define una función que reciba una lista de números y retorne la
suma acumulada de los números'''
def suma_acumulada(lista):
  lista_acumulada=[]
  total=0
  i=0
  while i<len(lista):
    total+=lista[i]
    lista_acumulada.append(total)
    i+=1
  print(lista_acumulada)
  return lista_acumulada
suma_acumulada([1,0,3,4,25])
'''Define una función que encuentre el elemento más común en una
lista.'''
def mas_comun(lista):
  diccionario={}
  for i in lista:
    if i in diccionario:
      diccionario[i]+=1
    else:
      diccionario[i]=1
  maxima_frecuencia=0
  for key,value in diccionario.items():
    if value > maxima_frecuencia:
      elemento_mas_frecuente=key
      maxima_frecuencia=value
  print(elemento_mas_frecuente)
  return elemento_mas_frecuente
mas_comun([1,4,2,7,9,9,9,4,5])
'''Define una función que tome un número y retorne un diccionario con
la tabla de multiplicar de ese número del 1 al 10.'''
def tabla_multiplicar(x):
  tabla={}
  for i in range(0,11):
    tabla[f'{x}*{i}']=x*i
  print(tabla)
tabla_multiplicar(7)
'''Define una función que tome una cadena y retorne un diccionario
con la cantidad de apariciones de cada caracter en la cadena.'''
def apariciones(string):
  diccionario={}
  for letter in string:
    if letter in diccionario:
      diccionario[letter]+=1
    else:
      diccionario[letter]=1
  print(diccionario)
  return diccionario
apariciones('HolalHp')
'''Define una función que tome dos listas y retorne la lista de
elementos que no están en ambas listas.'''
def unicos(lista_1,lista_2):
  lista_3=[]
  for i in lista_1:
    if i not in lista_2:
      lista_3.append(i)
  for i in lista_2:
    if i not in lista_1:
      lista_3.append(i)
  return lista_3
print(unicos([1,8,3,57,23], [43,8,67,3,2]))
'''Define una función que tome una lista y retorne la lista sin
duplicados.'''
def no_duplicates(lista):
  lista_unicos=[]
  for elemento in lista:
    if elemento not in lista_unicos:
      lista_unicos.append(elemento)
  print(lista_unicos)
  return lista_unicos
no_duplicates([1,4,2,7,8,9,3,8,9])
'''Define una función que reciba un número entero positivo y retorne la
suma de los cuadrados de todos los números pares menores o iguales a ese
número.'''
def suma_pares_cuadrados(x):
  total=0
  for i in range(2,x):
    if i%2==0:
      total+=i**2
  print(total)
  return total
suma_pares_cuadrados(8)
'''Define una función que reciba una lista de números y retorne el
promedio de los números en la lista.'''
def promedio(lista):
  suma=0
  for i in lista:
    suma+=i
  print(suma/(len(lista)))
  return suma/(len(lista))
promedio([1,5,6,27])
'''Define una función que reciba una lista de cadenas y retorne la
cadena más larga en la lista.'''
def cadena_mas_larga(lista):
  cadena_larga=lista[0]
  for cadena in lista:
    if len(cadena) > len(cadena_larga):
      cadena_larga=cadena
  print(cadena_larga)
  return cadena_larga
cadena_mas_larga(['Hola','Pájaro','Esternocleidomastoideo'])
'''Define una función que reciba un número entero n y retorne una lista
con los n primeros números primos.'''
def n_primos(n):
  lista_primos=[]
  contador=0
  i=0
  while contador<n:
    if es_primo(i)==True:
      lista_primos.append(i)
      contador+=1
    i+=1
  print(lista_primos)
  return lista_primos
n_primos(9)
'''Define una función que reciba una cadena y retorne la misma cadena
pero con las palabras en orden inverso.'''
def inverse(string):
  print(string[::-1])
  return string[::-1]
inverse('Hola')
'''Escribe una función que reciba una lista de tuplas y retorne una lista
ordenada basada en el último elemento de cada tupla.'''
'''Define una función que reciba una cadena y retorne la cantidad de
letras vocales en la cadena.'''
def num_vowels(string):
  vowels=['a','e','i','o','u']
  total=0
  for letter in string:
    if letter in vowels:
      total+=1
  print(total)
  return total
num_vowels('granja')
'''Define una función que reciba un número entero y retorne True si es
un número primo, de lo contrario retorne False.'''
def es_primo(x):
  if x<=1:
    return False
  for i in range(2,x):
      if x%i==0:
        return False
  return True
print(es_primo(2))