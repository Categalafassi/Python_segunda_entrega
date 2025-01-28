from Clase_cliente import Cliente

Cliente1= Cliente("Caterina", "Galafassi", "Categalafassi", "categalafassi@gmail.com", "micontrasenia01")

Cliente1.actualizar_datos(nuevo_usuario="CaterinaGalafassi")
print("El nuevo usuario es " + Cliente1.usuario)
Cliente1.cambiar_contrasenia("nuevacontrasenia!23")
print("Datos de "+ Cliente1.nombre+" " +Cliente1.apellido+": "+Cliente1.obtener_datos())

