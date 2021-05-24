import usuarios.conexion as conexion 

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Nota:
    #constructor
    def __init__(self, usuarioID, titulo , descripcion):
        self.usuario_id = usuarioID
        self.titulo = titulo
        self.descripcion = descripcion

    def crear_nota(self):
        sql = "insert into notas values(null, %s,%s, %s, NOW())"

        nota = (self.usuario_id, self.titulo, self.descripcion)

        cursor.execute(sql, nota)
        database.commit()

        return[cursor.rowcount, self]

    def mostrar_nota(self):

        sql = f"select * from notas where usuario_id = {self.usuario_id}"

        cursor.execute(sql)
        result = cursor.fetchall()

        return result



    def elimina_nota(self):
        sql = f"delete from notas where usuario_id = {self.usuario_id} and titulo like '%{self.titulo}%'"

        cursor.execute(sql)
        database.commit()

        return [cursor.rowcount, self]


    