import json

# Cargar los datos desde el archivo JSON
with open('data.json', 'r') as file:
    data = json.load(file)

# Filtrar los clientes cuya ciudad sea "Sevilla"
clientes_sevilla = [cliente for cliente in data['ventas']['clientes'] if cliente['ciudad'] == 'Sevilla']

# Ordenar los clientes filtrados por apellidos y nombre
clientes_sevilla_ordenados = sorted(clientes_sevilla, key=lambda x: (x['apellido1'], x['nombre']))

# Imprimir el identificador, nombre y primer apellido de los clientes filtrados y ordenados
for cliente in clientes_sevilla_ordenados:
    print(f"{cliente['id']}: {cliente['apellido1']}, {cliente['nombre']}")