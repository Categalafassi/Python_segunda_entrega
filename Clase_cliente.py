"""Clase cliente"""

class Cliente:
    def __init__(self, nombre, apellido, usuario, mail, contrasenia):
        self.nombre = nombre
        self.apellido = apellido
        self.usuario = usuario
        self.mail = mail
        self.contrasenia = contrasenia
    def obtener_datos(self):
        datos={
            "Nombre": self.nombre,
            "Apellido": self.apellido,
            "Usuario": self.usuario,
            "Mail": self.mail,
            "Contrasenia":self.contrasenia
        }
        return datos
    def cambiar_contrasenia(self, nueva_contrasenia):
        self.contrasenia=nueva_contrasenia
    def actualizar_datos(self, nuevo_nombre=None, nuevo_apellido=None, nuevo_usuario=None, nuevo_mail=None,nueva_contrasenia=None):
        if nuevo_nombre:
            self.nombre = nuevo_nombre
        if nuevo_apellido:
            self.apellido = nuevo_apellido
        if nuevo_usuario:
            self.usuario = nuevo_usuario
        if nuevo_mail:
            self.mail = nuevo_mail
        if nueva_contrasenia:
            self.contrasenia = nueva_contrasenia
    