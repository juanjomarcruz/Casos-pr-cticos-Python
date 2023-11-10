def crear_tablero():
  tablero=[[" " for i in range(3)] for i in range(3)]
  return tablero
def imprimir_tablero(tablero):
  print('------')
  for fila in tablero:
      print('|'.join(fila))
      print('------')
def is_tablero_lleno(tablero):
   return all(all(casilla!=' ' for casilla in fila) for fila in tablero) #all devuelve True solo sí todas son True (las va acumulando en cada iteración)
def comprobar_ganador(tablero,jugador):
   for i in range(3):
        if all(tablero[i][j]==jugador for j in range(3)) or all(tablero[j][i]==jugador for j in range(3)):
            #con [i][j] comprobamos las filas y con [j][i] las columnas
            return True
   if all(tablero[i][i]==jugador for i in range(3)) or all(tablero[i][2-i]==jugador for i in range(3)):
            #comprobación de diagonales
            return True
   return False
def tres_en_raya():
   tablero=crear_tablero()
   jugador_actual='X'
   print('¡Bienvenido al Tres en Raya!')
   imprimir_tablero(tablero)
   while True:
      print(f'Turno del jugador {jugador_actual}')
      fila=int(input('Elige la fila (0, 1 o 2): '))
      columna=int(input('Elige la columna (0, 1, o 2): '))
      if tablero[fila][columna]==' ':
         tablero[fila][columna]=jugador_actual
         imprimir_tablero(tablero)
         if comprobar_ganador(tablero,jugador_actual)==True:
            print(f'El jugador {jugador_actual} ha ganado')
            break
         elif is_tablero_lleno(tablero)==True:
            print('El tablero está lleno, EMPATE')
            break
         if jugador_actual=='X':
            jugador_actual='O'
         else:
            jugador_actual='X'
      else:
         print(f'La casilla {fila}{columna} está ocupada, seleccione otra')

if __name__=='__main__':
   tres_en_raya()