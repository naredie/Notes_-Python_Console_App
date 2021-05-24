"""
Proyecto de consola con python y MYSQL
- SQL estará alojado en un servidor de WAMP
- Se abre el asistente
- Permite Login o Registro
- Si elegimos registro, se creará un usuario en la base de datos
- Si elegimos login, se identifica al usuario
- Una vez logeado, se puede crear nota, mostrar notas, borrar nota (Tipico CRUD)

"""
from usuarios import acciones

acciones = acciones.Acciones()

print("""
    Acciones disponibles:
        * Registro
        * Login
""")

accion = input('¿Quieres registrarte o logearte?')

if accion == 'Registro' or accion == 'registro':
    acciones.registro()
elif accion == 'Login' or accion == 'login':
    acciones.login()
else:
    print("Opcion incorrecta")
