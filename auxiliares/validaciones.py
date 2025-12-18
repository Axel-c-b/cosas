import re
from interfaces_usuario import ingresar_correo

def validar_correo(email):
    regex = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}'
    if re.fullmatch(regex, str(email)):
        return True