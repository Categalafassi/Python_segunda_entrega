from Funciones import menu, iniciar_sesion, registrar_usuario, buscar_usuario 

while True:
  opcion=menu()
  if opcion==1:
    iniciar_sesion()
  if opcion==2:
    registrar_usuario()
  if opcion==3:
    buscar_usuario()
  if opcion==4: #Salir
    break