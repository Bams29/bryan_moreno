import json

# Cargar los datos del archivo json
with open('data.json', 'r') as file:
    data = json.load(file)

# Obtener los pedidos
pedidos = data['ventas']['pedidos']

# Ordenar los pedidos por el valor total en orden descendente
pedidos_ordenados = sorted(pedidos, key=lambda x: x['total'], reverse=True)

# Obtener los dos pedidos de mayor valor
pedidos_mayor_valor = pedidos_ordenados[:2]

# Imprimir los pedidos de mayor valor
for pedido in pedidos_mayor_valor:
    print(f"ID: {pedido['id']}, Total: {pedido['total']}, Fecha: {pedido['fecha']}, ID Cliente: {pedido['id_cliente']}, ID Comercial: {pedido['id_comercial']}")