class Biblioteca():
    catalogo_libros = {
        1: {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "descripcion": "Familia Buendía en Macondo", "fecha_publicacion": 1967, "disponibilidad": True},
        2: {"titulo": "1984", "autor": "George Orwell", "descripcion": "Distopía totalitaria", "fecha_publicacion": 1949, "disponibilidad": True},
        3: {"titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes", "descripcion": "Locuras de un caballero", "fecha_publicacion": 1605, "disponibilidad": True},
        4: {"titulo": "El señor de los anillos", "autor": "J.R.R. Tolkien", "descripcion": "Épica fantástica", "fecha_publicacion": 1954, "disponibilidad": True},
        5: {"titulo": "Harry Potter y la piedra filosofal", "autor": "J.K. Rowling", "descripcion": "Magia en Hogwarts", "fecha_publicacion": 1997, "disponibilidad": True},
        6: {"titulo": "Orgullo y prejuicio", "autor": "Jane Austen", "descripcion": "Amor y clases sociales", "fecha_publicacion": 1813, "disponibilidad": True},
        7: {"titulo": "Crónica de una muerte anunciada", "autor": "Gabriel García Márquez", "descripcion": "Asesinato anunciado", "fecha_publicacion": 1981, "disponibilidad": True},
        8: {"titulo": "El perfume", "autor": "Patrick Süskind", "descripcion": "Busca del aroma perfecto", "fecha_publicacion": 1985, "disponibilidad": True},
        9: {"titulo": "Moby Dick", "autor": "Herman Melville", "descripcion": "Caza de ballena blanca", "fecha_publicacion": 1851, "disponibilidad": True},
        10: {"titulo": "La metamorfosis", "autor": "Franz Kafka", "descripcion": "Transformación en insecto", "fecha_publicacion": 1915, "disponibilidad": True},
        11: {"titulo": "El hobbit", "autor": "J.R.R. Tolkien", "descripcion": "Aventura de Bilbo", "fecha_publicacion": 1937, "disponibilidad": True},
        12: {"titulo": "Drácula", "autor": "Bram Stoker", "descripcion": "Vampiro en Transilvania", "fecha_publicacion": 1897, "disponibilidad": True},
        13: {"titulo": "Los miserables", "autor": "Victor Hugo", "descripcion": "Lucha por la redención", "fecha_publicacion": 1862, "disponibilidad": True},
        14: {"titulo": "La Odisea", "autor": "Homero", "descripcion": "Viaje de Ulises a Ítaca", "fecha_publicacion": -800, "disponibilidad": True},
        15: {"titulo": "Romeo y Julieta", "autor": "William Shakespeare", "descripcion": "Trágico amor", "fecha_publicacion": 1597, "disponibilidad": True},
        16: {"titulo": "Anna Karenina", "autor": "León Tolstói", "descripcion": "Amor prohibido en Rusia", "fecha_publicacion": 1877, "disponibilidad": True},
        17: {"titulo": "El retrato de Dorian Gray", "autor": "Oscar Wilde", "descripcion": "Retrato envejecimiento", "fecha_publicacion": 1890, "disponibilidad": True},
        18: {"titulo": "El principito", "autor": "Antoine de Saint-Exupéry", "descripcion": "Viaje a través de asteroides", "fecha_publicacion": 1943, "disponibilidad": True},
        19: {"titulo": "Crimen y castigo", "autor": "Fyodor Dostoevsky", "descripcion": "Conciencia y crimen", "fecha_publicacion": 1866, "disponibilidad": True},
        20: {"titulo": "La guerra y la paz", "autor": "León Tolstói", "descripcion": "Guerra Napoleónica en Rusia", "fecha_publicacion": 1869, "disponibilidad": True},
        # Puedes agregar más libros siguiendo el mismo patrón
    }

    def MostrarCatalogo(self):
        for i in self.catalogo_libros.keys():
            print(f'Libro {i}')
            for j,k in self.catalogo_libros[i].items():
                print(f' {j} : {k} ')
    
