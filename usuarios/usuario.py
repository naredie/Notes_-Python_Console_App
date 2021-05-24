
from datetime import date
import hashlib
import usuarios.conexion as conexion

connect = conexion.conectar()
database= connect[0]
cursor = connect[1]

class Usuario:
    #constructor
    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    #registro
    def registrar(self):
        sql = "insert into usuarios values(null, %s,%s,%s,%s,%s)"
        
        fecha = date.today()

        #cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        usuario = (self.nombre, self.apellidos,self.email, cifrado.hexdigest(), fecha)

        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]
        
        return result

    #login
    def identificar(self):

        sql = "select * from usuarios where email = %s and password = %s"

        #cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        usuario = (self.email, cifrado.hexdigest())

        cursor.execute(sql, usuario)
        result = cursor.fetchone()

        return result
  