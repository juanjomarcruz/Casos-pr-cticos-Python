import random
tamaño=10
BARCO='B'
AGUA ='∼'
TOCADO= 'X'
FALLO = 'O'
Barco_tamaños=[2,3,3,4,5]
def crear_tablero(tamaño):
  tablero=[['∼' for i in range(tamaño)] for i in range(tamaño)]
  return tablero
def imprimir_tablero(tablero, ocultar_barcos=True):
  print('  '+' '.join(str(i) for i in range(len(tablero)))) #se imprime la primera fila con un separador concatenado con una lista de números del 1 al 9(tamaño del tablero - 1) generada mediante un bucle for. La lista de números que se genera pasa de tipo entero a texto para que pueda ser impresa con el .join. Dicha función consigue concatenar los elementos de la lista mediante el nexo separador ' '. 
  for i in range(10):
    fila = [str(i)] #aquí se genera la lista de números (tipo texto) denominada fila, mediante un bucle for, iterando del 1 al 9. En la primera iteración, la lista contiene el número 0 tipo texto. En cada iteración, la lista fila SE RENUEVA. Esto es importante. 
    for j in range(10): #se itera por cada una de las casillas dentro de cada fila del tablero.
      if ocultar_barcos and tablero[i][j] == BARCO: #si la variable ocultar_barcos es True y el contenido de la casilla [i][j] es igual a 'B', entonces añadimos a la lista fila AGUA, para que al imprimirse después muestre agua en esta casilla.
        fila.append(AGUA)
      else: #si la variable ocultar_barcos es False o el contenido del tablero en la casilla [i][j] no es igual a 'B', entonces añadimos a la lista fila el contenido de la casilla para que este se muestre por pantalla.
        fila.append(tablero[i][j])
def colocar_barcos(tablero):
  for tam in Barco_tamaños: #en la primera iteración, tam sería igual a 2 (colocamos el barco de longitud 2 casillas)
    while True:
      fila= random.randint(0,tamaño-1) #gracias a la función random junto con el sufijo randint somos capaces de generar coordenadas aleatorias de filas y columnas. De esta manera, en cada partida los barcos se posicionaran de manera distinta dentro del tablero. En este aso, si el tamaño del tablero fuera de 10, las coordenadas de filas y columnas podríanir desde (0,0) hasta (9,9).
      columna=random.randint(0,tamaño-1)
      direccion=random.choice(['horizontal','vertical']) #con el sufijo choice, el programa elige aleatoriamente donde colocaremos el barco.
      if es_posicion_valida(tablero,fila,columna,tam,direccion):
        colocar_barco(tablero,fila,columna,tam,direccion)
        break
def es_posicion_valida(tablero,fila,columna,tam,direccion):
  if direccion=='horizontal':
    if columna + tam > tamaño-1:
      return False
    return all(tablero[fila][columna+i]==AGUA for i in range(tam))
  elif direccion=='vertical':
    if fila + tam > tamaño-1:
      return False
    return all(tablero[fila+i][columna] == AGUA for i in range(tam))
def colocar_barco(tablero,fila,columna,tam,direccion):
    if direccion=='horizontal':
      for i in range(tam):
        tablero[fila][columna+i]==BARCO
    elif direccion=='vertical':
      for i in range(tam):
        tablero[fila+i][columna]==BARCO
def disparar(tablero,fila,columna):
  if tablero[fila][columna]==BARCO:
    tablero[fila][columna]==TOCADO
    return True
  elif tablero[fila][columna]==AGUA:
    tablero[fila][columna]==FALLO
    return False

def hundir_la_flota():
  tablero = crear_tablero(tamaño)
  colocar_barcos(tablero)
  print('Bienvenido a Hundir la Flota')
  while True:
    imprimir_tablero(tablero)
    try:
      fila=int(input('Introduce la fila para disparar: '))
      columna=int(input('Introduce la columna para disparar: '))
      if fila >= tamaño or fila<0 or columna>=tamaño or columna<0:
        print('Posición fuera del tablero. Inténtelo de nuevo.')
      if disparar(tablero,fila,columna):
        print('Barco golpeado!')
      else:
        print('Disparo al agua')
      if all(all(casilla!=BARCO for casilla in fila) for fila in tablero):
        print('Felicidades, has hundido la flota!')
        break
    except ValueError:
      print('Entrada inválida. Ingresa un número válido.')

if __name__=='__main__':
  hundir_la_flota()


