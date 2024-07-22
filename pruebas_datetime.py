from datetime import datetime, timedelta

# Obtener la fecha y hora actual
fecha_actual = datetime.now()

# Mostrar la fecha y hora actual
print("Fecha y hora actual:", fecha_actual)

# Calcular la fecha y hora exactamente 7 días después
fecha_despues = fecha_actual + timedelta(days=7)

# Mostrar la fecha y hora después de 7 días
print("Fecha y hora después de 7 días:", fecha_despues)
