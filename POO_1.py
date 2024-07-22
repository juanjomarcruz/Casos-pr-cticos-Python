from datetime import datetime, timedelta

class libro:
  def __init__(self, titulo, autor, precio):
    self.titulo=titulo
    self.autor=autor
    self.precio=precio
    self.cantidad=0
  def establecer_cantidad(self):
    while True:
      try:
        cantidad=int(input(f'Ingrese la cantidad de libros disponibles de {self.titulo}: '))
        if cantidad < 0:
          print('La cantidad no puede ser negativa. Intente de nuevo.')
        else:
          self.cantidad=cantidad
          break
      except ValueError:
        print("Por favor, ingrese un número entero válido.")

  def info_libro(self):
    info='Título: '+ self.titulo + '\n' + 'Autor: ' + self.autor + '\n' + 'Precio: ' + str(self.precio) + '\n' + 'Cantidad disponible: ' + str(self.cantidad)
    return info

class librofisico(libro):
  def __init__(self,titulo, autor, precio,categoria, peso):
    super().__init__(titulo, autor, precio)
    self.categoria=categoria
    self.peso=peso
  def envio(self,dias_envio=5):
    hoy=datetime.now()
    fecha_estimada_entrega=hoy + timedelta(days=dias_envio)
    return fecha_estimada_entrega
  def info_libro(self):
    info_libro=super().info_libro() + '\n' + 'Categoría: ' + self.categoria + '\n' +  'Peso: ' + str(self.peso) + '\n' + 'Fecha estimada de entrega: ' + self.envio().strftime("%Y-%m-%d")
    return info_libro

class audiolibro(libro):
  def __init__(self,titulo, autor, precio,categoria, duracion):
    super().__init__(titulo, autor, precio)
    self.categoria=categoria
    self.duracion=duracion
  def obtener_duracion_HH_MM_SS(self):
     horas=self.duracion // 3600
     minutos=(self.duracion % 3600) // 60
     segundos= self.duracion % 60
     duracion_HH_MM_SS=str(horas).zfill(2)+':'+str(minutos).zfill(2)+':'+str(segundos).zfill(2)
     return duracion_HH_MM_SS
  def info_libro(self):
    info_libro= super().info_libro() + '\n' + 'Categoría: '+ self.categoria + '\n' + 'Duración (S): ' + str(self.duracion) + '\n' + 'Duración (HH:MM:SS): ' + self.obtener_duracion_HH_MM_SS()
    return info_libro
  
class ECommerce:
    def __init__(self):
      self.carrito=[]
      self.inventario={}
    def agregar_al_inventario(self, producto):
      self.inventario[producto.titulo.lower()]=producto
    def ver_producto(self,nombre_producto):
      nombre_producto=nombre_producto.strip().lower()
      if nombre_producto in self.inventario:
        producto=self.inventario[nombre_producto]
        print(producto.info_libro())
      else:
        print('El producto no se encuentra en el inventario.')
    def ver_inventario(self):
        for producto in self.inventario.values():
          print(producto.info_libro())
    def agregar_al_carrito(self,nombre_producto):
      nombre_producto=nombre_producto.strip().lower()
      if nombre_producto in self.inventario:
        producto=self.inventario[nombre_producto]
        if producto.cantidad > 0:
          self.carrito.append(producto)
          producto.cantidad-=1
          print(f'{nombre_producto} ha sido añadido al carrito. Precio: {producto.precio}')
        else:
          print(f'No hay existencias de {nombre_producto} en el inventario.')
      else:
        print('El producto no se encuentra en el inventario.')
    def calcular_precio_total(self):
        precio_total = 0
        for producto in self.carrito:
          precio_total+=producto.precio
        return precio_total
    def pagar(self):
        while True:
          monto=float(input('Ingresa el monto para pagar: '))
          try:
            if monto >= self.calcular_precio_total():
              cambio=monto-self.calcular_precio_total()
              print(f'Pagado con éxito. Tu cambio es de {cambio:.2f} euros.')
              self.carrito=[]
              break
            else:
              print('El monto ingresado no es suficiente para pagar el total de la compra.')
          except ValueError:
            print('Ingrese un monto válido.')
    def ver_carrito(self):
          if self.carrito:
            print('Productos en el carrito:')
            for producto in self.carrito:
              print(producto.titulo)
            print(f'Precio total: {self.calcular_precio_total():.2f}')
          else:
            print('No hay productos en el carrito.')

eccomerce=ECommerce()
libro_fisico_1=librofisico('La Comunidad del Anillo', 'J.R.R. Tolkien', 29.99, 'Fantasía', 0.500)
libro_fisico_2=librofisico('Las Dos Torres', 'J.R.R. Tolkien', 29.99, 'Fantasía', 0.520)
libro_fisico_3=librofisico('El Retorno del Rey', 'J.R.R. Tolkien', 19.99, 'Fantasía', 0.490)
libro_fisico_4=librofisico('Las Crónicas de Narnia', 'C.S. Lewis', 21.50, 'Fantasía', 0.600)
audiolibro_1=audiolibro('El Juez', 'John Grisham', 9.99, 'Suspense', 3623)
audiolibro_2=audiolibro('La Promesa', 'John Grisham', 15.99, 'Suspense', 5603)
audiolibro_3=audiolibro('Patria', 'Ana Zulategui', 5.99, 'Historia', 4638)
audiolibro_4=audiolibro('El Mal', 'P. Gabrielle Amorth', 4.99, 'Religión', 7823)

libro_fisico_1.establecer_cantidad()
eccomerce.agregar_al_inventario(libro_fisico_1)
libro_fisico_2.establecer_cantidad()
eccomerce.agregar_al_inventario(libro_fisico_2)
libro_fisico_3.establecer_cantidad()
eccomerce.agregar_al_inventario(libro_fisico_3)
libro_fisico_4.establecer_cantidad()
eccomerce.agregar_al_inventario(libro_fisico_4)
audiolibro_1.establecer_cantidad()
eccomerce.agregar_al_inventario(audiolibro_1)
audiolibro_2.establecer_cantidad()
eccomerce.agregar_al_inventario(audiolibro_2)
audiolibro_3.establecer_cantidad()
eccomerce.agregar_al_inventario(audiolibro_3)
audiolibro_4.establecer_cantidad()
eccomerce.agregar_al_inventario(audiolibro_4)

eccomerce.ver_inventario()

print("\n¡Bienvenido a nuestra tienda en línea!")
while True:
  try:
    eleccion=int(input("Marque 1 para agregar un producto al carrito / Marque 2 para finalizar la compra: "))
    if eleccion==2:
      eccomerce.ver_carrito()
      eccomerce.pagar()
      break
    elif eleccion==1:
      producto_elegido=input('Escriba el producto que desea añadir al carrito: ')
      eccomerce.agregar_al_carrito(producto_elegido)
  except ValueError:
    print('Valor no válido. Inténtelo de nuevo.')

eccomerce.ver_carrito()
eccomerce.ver_inventario()