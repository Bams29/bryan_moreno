import json

# Cargar el archivo JSON
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Filtrar y eliminar los nombres repetidos
comerciales_filtrados = set([comercial['nombre'] for comercial in data['ventas']['comerciales'] if comercial['apellido1'] == 'Ruiz'])

# Imprimir el listado
for comercial in comerciales_filtrados:
    print(comercial)