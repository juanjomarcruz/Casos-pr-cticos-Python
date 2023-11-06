def suma(x,y):
  return x+y
def resta(x,y):
  return x-y
def multiplicacion(x,y):
  return x*y
def division(x,y):
  if y!=0:
    return x/y
  else:
    return 'Math Error'
def raiz_cuadrada(x):
  if x>=0:
    return x**0.5
  else:
    return 'Math Error'
def potencia(x,y):
  return x**y

def calculadora():
  print('¡Bienvenido a tu calculadora!')
  while True:
    eleccion = int(input('Selecciona la operación a realizar: Sumar(1) / Restar(2) / Multiplicar(3) / Dividir(4) / Elevar un número por otro(5) / Raiz cuadrada(6) / Exit(7): '))
    if eleccion == 7:
      break
    elif eleccion in [1,2,3,4,5]:
      x = int(input('Introduce el primer número: '))
      y = int(input('Introduce el segundo número: '))
      if eleccion == 1:
        result = suma(x,y)
      elif eleccion == 2:
        result = resta(x,y)
      elif eleccion == 3:
        result = multiplicacion(x,y)
      elif eleccion == 4:
        result = division(x,y)
      elif eleccion == 5:
        result = potencia(x,y)
    elif eleccion == 6:
      x = int(input('Introduce el número: '))
      result = raiz_cuadrada(x)
    else:
      print('Opción no válida')
      return False
    print(result)

if __name__== "__main__":
  calculadora()

