import bcrypt
import getpass
from modelos import Usuario
from datos import insertar_objeto, obtener_usuario_nombre
from auxiliares import validar_correo


def registrar_usuario():
    valido = False
    while valido == False:
        mensaje = '\nErrores en la creación del Usuario: \n'
        ingreso_nombre = input('Ingrese Nombre Completo: ')
        if ingreso_nombre == '':
            mensaje = mensaje + 'Nombre Completo es OBLIGATORIO.\n'
            
        ingreso_nombre_usuario = input('Ingrese Nombre Usuario: ')
        if ingreso_nombre_usuario == '':
            mensaje = mensaje + 'Nombre Usuario es OBLIGATORIO.\n'
            
        ingreso_email = input('Ingrese Correo Electrónico: ')
        if ingreso_email == '':
            mensaje = mensaje + 'Correo electrónico es OBLIGATORIO.\n'
        elif validar_correo(ingreso_email) != True:
            mensaje = mensaje + 'Correo electrónico INVÁLIDO.\n'
            
        ingreso_contrasena = getpass.getpass('Ingrese Contraseña: ')
        if ingreso_contrasena == '':
            mensaje = mensaje + 'Contraseña es OBLIGATORIA.\n'

        if mensaje == '\nErrores en la creación del Usuario: \n':
            valido = True
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw(ingreso_contrasena.encode('utf-8'), salt)
            nuevo_usuario = Usuario(
                nombre=ingreso_nombre,
                usuario=ingreso_nombre_usuario,
                email=ingreso_email,
                contrasena_hash=hashed,
                contrasena_salt=salt)

            try:
                id_usuario = insertar_objeto(nuevo_usuario)
                return id_usuario
            except Exception as error:
                print(f'Error al guardar al usuario: {error}')
        else:
            print(mensaje)
            print('\nVuelva a ingresar los datos')
            mensaje = ''


def iniciar_sesion():
    while True:
        ingreso_nombre_usuario = input('Ingrese Nombre Usuario: ')
        ingreso_contrasena = getpass.getpass('Ingrese Contraseña: ')

        usuario = obtener_usuario_nombre(ingreso_nombre_usuario)
        if usuario:
            if bcrypt.checkpw(ingreso_contrasena.encode('utf-8'), usuario.contrasena_hash.encode('utf-8')):
                print('Acceso Concedido!')
                return True
            else:
                print('Contraseña Incorrecta, Intente nuevamente.')
                return False
        else:
            print('Usuario NO encontrado, regístrese para ingresar.')
