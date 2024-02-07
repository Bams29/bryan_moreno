import json

# Cargar los datos desde el archivo JSON
with open('data.json', 'r') as file:
    data = json.load(file)

# Obtener los pedidos
pedidos = data['ventas']['pedidos']

# Obtener los identificadores únicos de los clientes que han realizado algún pedido
clientes_unicos = set(pedido['id_cliente'] for pedido in pedidos)

# Imprimir los identificadores únicos de los clientes que han realizado algún pedido
print(clientes_unicos)