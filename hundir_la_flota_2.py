import random

TAMAÑO=10
BARCO='B'
AGUA='∼'
TOCADO= 'X'
FALLO= 'O'
tamaño_barcos=[2,3,3,4,5]

def crear_tablero(TAMAÑO):
  tablero=[[AGUA for i in range(TAMAÑO)] for i in range(TAMAÑO)]
  return tablero

def imprimir_tablero(tablero,ocultar_barcos=True):
  print('  '+ ' '.join(str(i) for i in range(TAMAÑO)))
  fila=[]
  for i in range(TAMAÑO):
    fila=[str(i)]
    for j in range(TAMAÑO):
      if ocultar_barcos and tablero[i][j]==BARCO:
        fila.append(AGUA)
      else:
        fila.append(tablero[i][j])
    print(' '.join(fila))

def colocar_barcos(tablero):
  for tam in tamaño_barcos:
    while True:
      fila=random.randint(0,TAMAÑO-1)
      columna=random.randint(0,TAMAÑO-1)
      dirección=random.choice(['horizontal','vertical'])
      if es_posición_válida(tablero,fila,columna,dirección,tam):
        coloca_barco(tablero,fila,columna,dirección,tam)
        break

def es_posición_válida(tablero,fila,columna,dirección,tam):
  if dirección=='horizontal':
    if tam+columna > TAMAÑO:
      return False
    return all(tablero[fila][columna+i]==AGUA for i in range(tam))
  elif dirección=='vertical':
    if tam+fila > TAMAÑO:
      return False
    return all(tablero[fila+i][columna]==AGUA for i in range(tam))

def coloca_barco(tablero,fila,columna,dirección,tam):
    if dirección=='horizontal':
      for i in range(tam):
        tablero[fila][columna+i]=BARCO
    elif dirección=='vertical':
      for i in range(tam):
        tablero[fila+i][columna]=BARCO

def disparar(tablero,fila,columna):
  if tablero[fila][columna]==BARCO:
    tablero[fila][columna]=TOCADO
    return True
  elif tablero[fila][columna]==AGUA:
    tablero[fila][columna]=FALLO
    return False

def hundir_la_flota():
  tablero=crear_tablero(TAMAÑO)
  colocar_barcos(tablero)
  print('Bienvenido al juego de Hundir la Flota.')
  while True:
    imprimir_tablero(tablero,ocultar_barcos=True)
    try:
      fila=int(input('Introduce la fila para disparar: '))
      columna=int(input('Introduce la columna para disparar: '))
      if fila<0 or fila>=TAMAÑO or columna<0 or columna>=TAMAÑO:
        print('La posición introducida no es válida o está fuera del rango del tablero.')
      if disparar(tablero,fila,columna):
          print('¡Tocado! Buen disparo, sigue así.')
      else:
          print('¡Has fallado! Inténtalo de nuevo.')
      if all(all(tablero[i][j]!=BARCO for i in range(TAMAÑO)) for j in range(TAMAÑO)):
        print('¡Felicidades, has derribado todos los barcos!')
        imprimir_tablero(tablero,ocultar_barcos=False)
        break
    except ValueError:
      print('Entrada no válida. Introduzca un número válido.')

if __name__=='__main__':
  hundir_la_flota()