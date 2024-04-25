lista_tareas=[] #cómo hacer que se guarde en un txt para que al salir del programa no se borre todo. --> libreria OS
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
  try:
    i=int(input('\n Introduzca el ID de la tarea que desea marcar como Finalizada: '))
    lista_tareas[i-1].estado='Finalizada'
    listar_tareas(lista_tareas)
  except IndexError:
    print('\n El ID introducido no está asociado a ninguna tarea.')
  except ValueError:
    print('\n Entrada no válida. Pruebe de nuevo.')

def listar_tareas(lista_tareas):
  print('LISTA DE TAREAS: \n')
  for tarea in lista_tareas:
    print('ID-'+str(tarea.id) + ' ' + 'Descripción-'+tarea.descripcion + ' '+'Vencimiento-'+tarea.fecha_vencimiento + ' ' +'Estado-'+tarea.estado)

def filtrar_tareas(lista_tareas):
  try:
    num=int(input('Para filtrar por tareas pendientes, pulse 1. Para filtrar por tareas finalizadas pulse 2: '))
    if num==1:
      print('LISTA DE TAREAS PENDIENTES: \n')
      for tarea in lista_tareas:
        if tarea.estado=='Pendiente':
          print('ID-'+str(tarea.id) + ' ' + 'Descripción-'+tarea.descripcion + ' '+'Vencimiento-'+tarea.fecha_vencimiento + ' ' +'Estado-'+tarea.estado)
    elif num==2:
      print('LISTA DE TAREAS FINALIZADAS: \n')
      for tarea in lista_tareas:
        if tarea.estado=='Finalizada':
          print('ID-'+str(tarea.id) + ' ' + 'Descripción-'+tarea.descripcion + ' '+'Vencimiento-'+tarea.fecha_vencimiento + ' ' +'Estado-'+tarea.estado)
    else:
      print('\n Entrada no válida. Pulse 1 o 2.')
  except ValueError:
      print('\n Entrada no válida. Pulse 1 o 2.')

def gestor_de_tareas(lista_tareas):
  count_tareas=0
  while True:
    print('\n¡Bienvenido a tu Gestor de Tareas!\n')
    try:
      eleccion = int(input('Selecciona la acción a realizar:  \n 1. Agregar Tarea \n 2. Completar Tarea \n 3. Listar Tareas \n 4. Filtrar Tareas \n 5. Salir \n Introduzca un entero del 1 al 5: '))
      print('\n')
      if eleccion==1:
        count_tareas+=1
        agregar_tarea(tarea,lista_tareas, count_tareas)
      elif eleccion==2:
        listar_tareas(lista_tareas)
        completar_tarea(lista_tareas)
      elif eleccion==3:
        listar_tareas(lista_tareas)
      elif eleccion==4:
        filtrar_tareas(lista_tareas)
      elif eleccion==5:
        print('Has salido del Gestor de Tareas.')
        break
    except ValueError:
        print('\n')
        print('Entrada no válida. Pruebe de nuevo.')

if __name__=='__main__':
  gestor_de_tareas(lista_tareas)