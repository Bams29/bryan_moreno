import json

# Cargar el archivo JSON
with open('data.json') as f:
    data = json.load(f)

# Acceder a las llaves 'ventas' y 'pedidos'
pedidos = data['ventas']['pedidos']

# Crear una lista de tuplas que contenga las fechas y los ID de los pedidos
fechas = [(pedido['fecha'], pedido['id']) for pedido in pedidos]

# Ordenar la lista de tuplas usando la función sorted() y el argumento key
fechas.sort(key=lambda x: x[0], reverse=True)

# Imprimir las fechas ordenadas
for fecha, id_pedido in fechas:
    print(fecha)