import json

# Cargar el archivo JSON
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Filtrar y ordenar los clientes
clientes_filtrados = sorted([cliente['nombre'] for cliente in data['ventas']['clientes'] if cliente['nombre'][0] == 'A'], key=str.lower)

# Imprimir el listado
for cliente in clientes_filtrados:
    print(cliente)