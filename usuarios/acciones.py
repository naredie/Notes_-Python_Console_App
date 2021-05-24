import usuarios.usuario as usermodel
import notas.accionesnotas as accionesnotas
class Acciones:
    def registro(self):
        print("Registrandote en el sistema")

        nombre = input('Introduce tu nombre: ')
        apellidos = input('Introduce tus apellidos: ')
        email = input('Introduce tu Email: ')
        password = input ('Introduce una contraseña: ')

        usuario = usermodel.Usuario(nombre, apellidos, email, password)

        registro = usuario.registrar()

        if registro[0] >= 1:
            print("Usuario " + registro[1].nombre + " con email " + registro[1].email+" registrado")
        else:
            print("El usuario no se ha registrado correctamente")


    def login(self):
        print("Logeandote en el sistema")
        try:
            email = input('Introduce tu Email: ')
            password = input ('Introduce una contraseña: ')

            usuario = usermodel.Usuario('','',email, password)

            login = usuario.identificar()

            if login and email == login[3]:
                print(f"Bienvenido {login[1]}, te has logeado en el sistema")
                self.proximasAcciones(login)
            else:
                print(f"Error en el login. Por favor intentalo de nuevo")
        except Exception as e:
            print(e)
            print(type(e))
            print(type(e).__name__)
            print(f"Error en el login. Por favor intentalo de nuevo")


    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles:
        - Crear nueva nota
        - Mostrar tus notas
        - Eliminar nota
        - Salir
        """)

        accion = input("¿Que accion quieres realizar? ")
        acciones_notas = accionesnotas.AccionesNotas()

        if accion =="crear":
            acciones_notas.crearNota(usuario[0])
            self.proximasAcciones(usuario)
        elif accion =="mostrar":
            acciones_notas.listarNotas(usuario[0])
            self.proximasAcciones(usuario)
        elif accion =="eliminar":
            acciones_notas.borrar_nota(usuario[0])
            self.proximasAcciones(usuario)
        elif accion =="salir":
            exit()