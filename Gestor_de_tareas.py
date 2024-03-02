lista_tareas=[]
class tarea:
  def __init__(self):
    self.id=None
    self.descripcion=None
    self.fecha_vencimiento=None
    self.estado='Pendiente'
  def user_input(self, count_tareas):
    self.id=count_tareas
    self.descripcion=input("Ingresa una breve descripción de la tarea (p.e. Hacer maleta): ")
    self.fecha_vencimiento=input("Ingresa una fecha de vencimiento (DD/MM/AAAA): ")

def agregar_tarea(tarea, lista_tareas, count_tareas):
  tarea_x=tarea()
  tarea_x.user_input(count_tareas)
  lista_tareas.append(tarea_x)
  return lista_tareas

def completar_tarea(lista_tareas):
  i=int(input('Introduzca el ID de la tarea que desea marcar como Finalizada: '))
  lista_tareas[i-1].estado='Finalizada'

def listar_tareas(lista_tareas):
  print('ID' + ' ' + 'Descripción' + ' ' + 'Vencimiento' + ' ' + 'Estado' )
  for tarea in lista_tareas:
    print(str(tarea.id) + ' ' + tarea.descripcion + ' '+ tarea.fecha_vencimiento + ' ' + tarea.estado)

def filtrar_tareas(lista_tareas):
    num=int(input('Para filtrar por tareas pendientes, pulse 1. Para filtrar por tareas finalizadas pulse 2: '))
    if num==1:
      print('ID' + ' ' + 'Descripción' + ' ' + 'Vencimiento' + ' ' + 'Estado' )
      for tarea in lista_tareas:
        if tarea.estado=='Pendiente':
          print(str(tarea.id) + ' ' + tarea.descripcion + ' '+ tarea.fecha_vencimiento + ' ' + tarea.estado)
    elif num==2:
      print('ID' + ' ' + 'Descripción' + ' ' + 'Vencimiento' + ' ' + 'Estado' )
      for tarea in lista_tareas:
        if tarea.estado=='Finalizada':
          print(str(tarea.id) + ' ' + tarea.descripcion + ' '+ tarea.fecha_vencimiento + ' ' + tarea.estado)
    else:
      print('Entrada no válida. Pruebe de nuevo.')

def gestor_de_tareas(lista_tareas):
  print('¡Bienvenido a tu Gestor de Tareas!')
  count_tareas=0
  while True:
    eleccion = int(input('Selecciona la acción a realizar: Agregar Tarea (1) / Completar Tarea (2) / Listar Tareas (3) / Filtrar Tareas (4) / Salir (5): '))
    if eleccion==1:
        count_tareas+=1
        agregar_tarea(tarea,lista_tareas, count_tareas)
    elif eleccion==2:
        completar_tarea(lista_tareas)
    elif eleccion==3:
        listar_tareas(lista_tareas)
    elif eleccion==4:
        filtrar_tareas(lista_tareas)
    elif eleccion==5:
        break
    else:
        print('Entrada no válida. Pruebe de nuevo.')
        return False

if __name__=='__main__':
  gestor_de_tareas(lista_tareas)