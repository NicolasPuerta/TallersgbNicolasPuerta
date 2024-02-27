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
        for i,j in self.catalogo.catalogo_libros.items():
            if j['titulo'] == Titulo and j['disponibilidad'] == True:
                j['disponibilidad'] = False
                print('libro prestado')
                libro = {i:j}
            elif j['titulo'] == Titulo and j['disponibilidad'] == False:
                print('Libro no disponible')
        self.listaLibros = libro if libro or j['disponibilidad'] == False else {'titulo': 'No existe o no disponible'}
    
    def DevolverLibro(self,Titulo:str):
        if len(self.listaLibros)==0:
            print("No hay libros por devolver")
        else:
            self.MostrarLibros()
            for i in self.listaLibros:
                for j in self.listaLibros[i].values():
                    if j == Titulo:
                        index = i
            del self.listaLibros[index]
            for j in self.catalogo.catalogo_libros.values():
                if j['titulo'] == Titulo:
                    print("libro devuelto")
                    j['disponibilidad'] = True

    def MostrarUsuario(self):
        return (f'{self.nombre} {self.apellido}')
    
    def MostrarLibros(self):
        print("#### Libros prestados ####")
        for i in self.listaLibros:
            for j,k in self.listaLibros[i].items():
                print(f' {j} : {k}')