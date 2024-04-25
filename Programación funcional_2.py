def procesar_datos(operación,a,b,*args,**kwargs): #en lugar de meter a y b como argumentos podemos poner solo *args.
  if operación.lower()=='sumar':
    resultado=kwargs['valor_inicial']+a+b #también podemos hacer resutado=kwargs.get('valor_inicial',0)
    for arg in args:
        resultado+=arg
  elif operación.lower()=='restar':
    resultado=a-b #o bien, si no hemos especificado a y b: resultado=args[0]
    for arg in args: #o bien for arg in args[1:]:
      resultado-=arg
  elif operación.lower()=='multiplicar':
    resultado=a*b*kwargs['factor']  #o bien, resultado=kwargs.get('factor',1)
    for arg in args:  #o bien for arg in args:
      resultado*=arg  
  elif operación.lower()=='dividir': 
    resultado=a/b  #o bien, confirmacion=all(valor!=0 for valor in args[1:])
    for arg in args: #if confirmacion:
      resultado/=arg  #resultado=args[0] 
                      #for valor in args:
                      #resultado/=valor
                      #else:
                      #raise ZeroDivisionError
  else:
    raise ValueError("Operación no válida. Pruebe 'sumar', 'restar', 'multiplicar' o 'dividir'.") #raise sirve para manejar errores 
  return resultado

resultado_suma=procesar_datos('sumar',4,2,2,valor_inicial=10)
print(resultado_suma)
resultado_resta=procesar_datos('restar',4,2,2)
print(resultado_resta)
resultado_multiplicacion=procesar_datos('multiplicar',4,2,2,factor=2)
print(resultado_multiplicacion)
resultado_division=procesar_datos('dividir',4,2,2)
print(resultado_division)

strings = ["hello", "world", "python", "programming", "is", "fun"]
cadenas_ordenadas=sorted(strings,key=lambda x: len(x))
print(cadenas_ordenadas)

numbers = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
filtered_numbers=[num for num in numbers if num%3==0 and num>10]
print(filtered_numbers)

people = {"Alice": 30, "Bob": 25, "Charlie": 35, "David": 40}

ordenado=dict(sorted(people.items(),key= lambda tuple: tuple[1]) )#es necesario la función .items porque .items te da el diccionario en tuplas clave-valor, que son elementos iterables y recordemos que la función sorted requiere un iterable.
print(ordenado)

def ordenacion_dict(diccionario):
  ordenado=dict(sorted(diccionario.items(),key= lambda tuple: tuple[1]) )
  dict_ordenado=dict(ordenado)
  return dict_ordenado

print(ordenacion_dict(people))

numbers = [1, 2, 3, 4, 5]

num_cuadrado=list(map(lambda x:x**2,))