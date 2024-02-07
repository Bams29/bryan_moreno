import json

# Cargar el archivo json
with open('data.json', 'r') as f:
    data = json.load(f)

# Filtrar y ordenar los clientes que empiezan con 'A' en el nombre y terminan con 'n' en el apellido
clientes_filtrados_a = sorted([f"{cliente['nombre']} {cliente['apellido1']}" for cliente in data['ventas']['clientes'] if cliente['nombre'].startswith('A') and cliente['apellido1'].endswith('n')], key=str.lower)

# Filtrar y ordenar los clientes que empiezan con 'P' en el nombre
clientes_filtrados_p = sorted([f"{cliente['nombre']} {cliente['apellido1']}" for cliente in data['ventas']['clientes'] if cliente['nombre'].startswith('P')], key=str.lower)

# Combinar los dos listados
clientes_filtrados_a.extend(clientes_filtrados_p)

# Imprimir el listado
for cliente in clientes_filtrados_a:
    print(cliente)
