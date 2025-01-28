import json

base_prueba={
    "Caterina01":"contraseña02", 
    "usuario123": "contra234", 
}

with open('base_clientes.json', 'w') as archivo:
    json.dump(base_prueba, archivo)
    