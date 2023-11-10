def crear_tablero():
  tablero=[[' ' for i in range(3)] for i in range(3)]
  return tablero
def imprimir_tablero(tablero):
  print('------')
  for fila in tablero:
    print('|'.join(fila))
    print('------')
def is_tablero_full(tablero):
  return all(all(casilla!=' ' for casilla in fila) for fila in tablero)
def comprobar_ganador(tablero, jugador):
  for i in range(3):
    if all(tablero[i][j]==jugador for j in range(3)) or all(tablero[j][i]==jugador for j in range(3)):
      return True
  if all(tablero[i][i]==jugador for i in range(3)) or all(tablero[i][2-i]==jugador for i in range(3)):
      return True
  return False
def tres_en_raya():
  tablero=crear_tablero()
  jugador_actual='X'
  print('Bienvenido al Tres en Raya')
  while True:
    imprimir_tablero(tablero)
    print(f'Turno del jugador {jugador_actual}')
    fila=int(input('Introduzca la fila (0/1/2): '))
    columna=int(input('Introduzca la columna (0/1/2): '))
    if tablero[fila][columna]==' ':
      tablero[fila][columna]=jugador_actual
      if is_tablero_full(tablero)==True:
        print('El tablero está lleno: EMPATE')
        break
      elif comprobar_ganador(tablero,jugador_actual)==True:
        print(f'El jugador {jugador_actual} ha ganado.')
        imprimir_tablero(tablero)
        break
      if jugador_actual=='X':
        jugador_actual='O'
      else:
        jugador_actual='X'
    else:
      print('La casilla está ocupada, seleccione otra.')

if __name__=='__main__':
  tres_en_raya()