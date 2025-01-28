from Clase_cliente import Cliente

Cliente1= Cliente("Caterina", "Galafassi", "Categalafassi", "categalafassi@gmail.com", "micontrasenia01")
Cliente2=Cliente("Maria", "Perez","MariPerez02", "Mariaperez@gmail.com","marimari3322")

Cliente1.actualizar_datos(nuevo_usuario="CaterinaGalafassi")
print("El nuevo usuario es " + Cliente1.usuario)

Cliente2.cambiar_contrasenia("nuevacontrasenia!23")
print("Datos de "+ Cliente2.nombre+" " +Cliente2.apellido+": "+Cliente2.obtener_datos())

