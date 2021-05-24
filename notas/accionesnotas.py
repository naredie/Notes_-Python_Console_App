import notas.nota as modeloNota
class AccionesNotas:
    def crearNota(self, usuarioID):
        titulo = input("Introduce un titulo para tu nota: ")
        descripcion = input("Introduce la descripcion de la nota: ")

        usuario_id = usuarioID

        nota = modeloNota.Nota(usuario_id, titulo, descripcion)

        guardar = nota.crear_nota()

        if guardar[0] >= 1:
            print(f"Nota { nota.titulo } guardada correctamente")
        else:
            print(f"No se ha guardado la nota")


    def listarNotas(self, usuarioID):
        print(f"\nMostrando notas del usuario actual")

        nota = modeloNota.Nota(usuarioID, "", "")

        notas = nota.mostrar_nota()

        for nota in notas:
            print(f"\n************************")
            print(nota[2])
            print(nota[3])

    def borrar_nota(self, usuarioID):
        print (f"\nEliminando nota")
        titulo = input("Introduce el titulo de la nota a borrar: ")

        nota = modeloNota.Nota(usuarioID, titulo, "")

        elimina_nota = nota.elimina_nota()

        if elimina_nota[0] >=1:
            print(f"Nota {nota.titulo} eliminada correctanemte")
        else:
            print(f"No se ha podido eliminar correctamente la nota")



