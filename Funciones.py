import json

def menu():
 while True:
  print("\nMENU")
  print("1. Iniciar sesión")
  print("2. Registrarse")
  print("3. Buscar usuario")
  print("4. Salir")
  try:
    opcion = int(input("Elegir una opción: "))
    if 1 <= opcion <= 4: #Que el usuario solo pueda elegir una opción válida
      return opcion
    else:
      print("(!) Elija una opcion válida.\n")
  except ValueError: #Por si ingresa un string
    print("(!) Por favor ingresá un número. \n")

def contiene_numero(contrasenia):
  for char in contrasenia:
    if char.isdigit():
      return True
  else:
    return False

def iniciar_sesion(): #opcion 1
  print("\n INICIAR SESIÓN - ingrese 0 para retornar \n")
  with open('base_clientes.json', 'r') as archivo:
    base_de_datos = json.load(archivo)
  archivo.close()
  # ingresar usuario
  while True:
    usuario=input("Usuario: ")
    if usuario=="0":
      print("Retornando... \n")
      return
    elif usuario not in base_de_datos:
      print("(!) El usuario no existe.\n")
    else:
      break
  # ingresar contraseña
  while True:
    contrasenia=input("Contraseña: ")
    if contrasenia=="0":
      print("Retornando...")
      print(" ")
      return
    elif not(base_de_datos[usuario] == contrasenia):
      print("(!) Contraseña incorrecta.\n")
      print("Usuario: " + usuario)
    else:
      break
  print("\n HA INICIADO SESIÓN :) \n")

def registrar_usuario():
  print("\n REGISTRAR USUARIO - ingrese 0 para retornar \n")
  with open('base_clientes.json', 'r') as archivo:
    base_de_datos = json.load(archivo) 
  # Nuevo usuario
  while True:
    nuevo_usuario=input("Nuevo usuario: ")
    if nuevo_usuario=="0":
      print("Retornando... \n")
      return
    elif nuevo_usuario in base_de_datos:
      print("(!) El usuario ya existe. \n")
      continue
    elif len(nuevo_usuario)<5:
      print("(!) El usuario debe tener más de 5 caracteres. \n")
      continue
    else:
      break
  # Nueva contraseña
  while True:
    nueva_contrasenia=input("Ingrese una contraseña: ")
    if len(nueva_contrasenia)<5:
      print("(!) La contraseña debe tener más de 5 caracteres.\n")
      print("Usuario: " + nuevo_usuario)
      continue
    elif " " in nueva_contrasenia:
      print("(!) La contraseña no puede contener espacios. \n")
      print("Usuario: " + nuevo_usuario)
      continue
    elif not contiene_numero(nueva_contrasenia):
      print("(!) La contraseña debe contener al menos un número.\n")
      print("Usuario: " + nuevo_usuario)
      continue
    else:
      break
  base_de_datos[nuevo_usuario] = nueva_contrasenia
  with open('base_clientes.json', 'w') as archivo:
    json.dump(base_de_datos, archivo)
  print("Usuario "+ nuevo_usuario +" registrado exitosamente! \n")

def buscar_usuario():
  with open('base_clientes.json', 'r') as archivo:
    base_de_datos = json.load(archivo)  
  while True:
    print("\nBÚSQUEDA DE USUARIO")
    print("1. Buscar un usuario en la base de datos")
    print("2. Salir")
    try:
      opcion = int(input("Elegir una opción: "))
      if opcion > 2 or opcion < 1: #Que el usuario solo pueda elegir una opción válida
        print("(!) Elija una opcion válida.\n")
    except ValueError: #Por si ingresa un string
     print("(!) Por favor ingresá un número. \n")
    if opcion==1:
      usuario=input("\nUsuario: ")
      if usuario not in base_de_datos:
        print("El usuario no está registrado en la base de datos.")
        continue
      elif usuario in base_de_datos:
        print("La contraseña de " +usuario+" es: " + base_de_datos[usuario])
        input("Presione cualquier tecla para continuar...")
        continue
    if opcion==2:
      return
    