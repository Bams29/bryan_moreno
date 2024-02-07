import json
from datetime import datetime

# Cargar los datos desde el archivo JSON
with open('data.json', 'r') as file:
    data = json.load(file)

# Obtener los pedidos
pedidos = data['ventas']['pedidos']

# Filtrar los pedidos realizados durante el año 2017 y con una cantidad total superior a 500€
pedidos_filtrados = [pedido for pedido in pedidos if datetime.strptime(pedido['fecha'], '%Y-%m-%d').year == 2017 and pedido['total'] > 500]

# Imprimir los pedidos filtrados
for pedido in pedidos_filtrados:
    print(pedido)