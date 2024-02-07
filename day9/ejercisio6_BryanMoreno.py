import json

# Cargar los datos desde el archivo JSON
with open('data.json', 'r') as file:
    data = json.load(file)

# Obtener las comisiones de los comerciales
comisiones = [comercial['comisión'] for comercial in data['ventas']['comerciales']]

# Obtener el valor máximo de las comisiones
comision_maxima = max(comisiones)

# Imprimir el valor máximo de las comisiones
print(comision_maxima)