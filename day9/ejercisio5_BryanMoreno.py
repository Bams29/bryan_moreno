import json

# Cargar los datos desde el archivo JSON
with open('data.json', 'r') as file:
    data = json.load(file)

# Obtener los comerciales
comerciales = data['ventas']['comerciales']

# Filtrar los comerciales con una comisión entre 0.05 y 0.11
comerciales_filtrados = [comercial for comercial in comerciales if comercial['comisión'] >= 0.05 and comercial['comisión'] <= 0.11]

# Imprimir el nombre y los apellidos de los comerciales filtrados
for comercial in comerciales_filtrados:
    print(f"{comercial['nombre']} {comercial['apellido1']} {comercial['apellido2'] if 'apellido2' in comercial else ''}")