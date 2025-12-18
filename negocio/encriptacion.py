import hashlib

class Encriptador:
    @staticmethod
    def encriptar(contrasena):
        return hashlib.sha256(contrasena.encode()).hexdigest()

    @staticmethod
    def verificar(contrasena_plana, contrasena_encriptada):
        return Encriptador.encriptar(contrasena_plana) == contrasena_encriptada