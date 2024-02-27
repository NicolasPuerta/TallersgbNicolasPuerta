from Biblioteca import Biblioteca
class Usuario():
    def __init__(self,nombre: str,apellido: str,edad : int) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.listaLibros = []
        self.catalogo = Biblioteca()

    def PrestarLibros(self,Titulo:str) -> None:
        libro = {}
        for j in self.catalogo.catalogo_libros.values():
            if j.titulo == Titulo:
                j.disponibilidad = False
                libro = j
        
        self.listaLibros = libro if libro else {'titulo': 'No existe'}
    
    def DevolverLibro(self,Titulo:str) :
        for j in self.catalogo.catalogo_libros.values():
            if j.titulo == Titulo:
                j.disponibilidad = True
        for i in self.listaLibros:
            for j in self.listaLibros[i].titulo:
                if j == Titulo:
                    del self.listaLibros[i]