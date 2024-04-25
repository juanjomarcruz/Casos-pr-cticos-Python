cadena='Hoy es lunes y martes también'
def frecuencia_letras(cadena):
  conteo_letras={}
  for letra in cadena.lower():
    if letra!=' ':
      if letra in conteo_letras:
        conteo_letras[letra]+=1
      else:
        conteo_letras[letra]=1

  return print(conteo_letras)

frecuencia_letras(cadena)

def buscar_palabra(lista_palabras,palabra_objetivo):
  palabras_encontradas=[]
  for palabra in lista_palabras:
    if palabra_objetivo in palabra:
      palabras_encontradas.append(palabra)
  return palabras_encontradas

def calcular_promedio(lista_notas,nota_aprobado=5):
  suma = 0
  for nota in lista_notas:
    suma+= nota
  nota_media = round(suma / len(lista_notas),2)
  estado = 'Aprobado'
  if nota_media < nota_aprobado:
    estado = 'Suspenso'
  return nota_media,estado

notas_1=[1,6,8,3,6,2,6,5,4]
final_curso=calcular_promedio(notas_1)
print(final_curso)

notas_2=[10,60,80,30]
final_curso_2=calcular_promedio(notas_2,50)
print(final_curso_2)

def factorial(n):
 if n==0:
   return 1
 else:
   return n*factorial(n-1)

#numero=4
#factorial_numero=factorial(numero)
#print(factorial)

#*args desempaqueta una lista o una tupla, mientras que **kwargs sirve para desempaquetar diccionarios, es decir, funciona con claves/valor.

def combinar_listas(*args):
  diccionario={}
  for indice,elemento in enumerate(list(zip(*args))):
    diccionario[indice]=elemento
  return diccionario

lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
lista3 = [True, False, True]

mi_diccionario=combinar_listas(lista1,lista2,lista3)
print(mi_diccionario)

def area_figura(**kwargs):
  if 'base' in kwargs and 'altura' in kwargs:
    base=kwargs['base']
    altura=kwargs['altura']
    area=(base*altura)
  elif 'radio' in kwargs:
    radio=kwargs['radio']
    area=3.14*radio**2
  elif 'lado' in kwargs:
    lado=kwargs['lado']
    area=lado**2
  else:
    raise ValueError('No se pudo determinar el tipo de figura geométrica')
  return area

area_triangulo = area_figura(base=3, altura=4)
print(area_triangulo)
area_circulo = area_figura(radio=2)
print(area_circulo)
area_cuadrado = area_figura(lado=5)
print(area_cuadrado)
