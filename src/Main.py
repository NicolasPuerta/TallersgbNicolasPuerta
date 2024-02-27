from Biblioteca import Biblioteca
from Usuarios import Usuario

biblioteca = Biblioteca()
Usuarios = {1:Usuario('Juan','Lopez', 20), 2:Usuario('Nicolas', 'Puerta', '19')}

while(True):
    print(f'Bienvenido')
    opc = int(input('1.Elegir usuario\n2.mostrar catalogo\nelija una de estas dos opciones:'))
    if(opc == 1):
        for i,j in Usuarios.items():
            print(f'Id {i}. {j.MostrarUsuario()}')
        try:
            usuarioID = int(input('Digite el numero de resgistro del usuario: '))
            usuario = Usuarios[usuarioID]
        except Exception as e:
            print('usuario no existente')
        opc2 = int(input('1.Prestar Libro\n2.Devolver Libro\nelija una de estas dos opciones:'))
        if(opc2 == 1):
            biblioteca.MostrarCatalogo()
            titulo = input('Digite el titulo del libro a prestar: ')
            usuario.PrestarLibros(Titulo=titulo)
        elif(opc2 == 2):
            usuario.MostrarLibros()
            titulo = input('Digite el titulo del libro a devolver: ')
            usuario.DevolverLibro(Titulo=titulo)
    else: 
        biblioteca.MostrarCatalogo()


