class Persona:
    def __init__ (self, apellido, nombre):
        self.apellido = apellido
        self.nombre = nombre
    
    def get_nombre_completo(self):
        return f"{self.apellido}, {self.nombre}"

class Autor(Persona):
    def __init__ (self, apellido, nombre, nacionalidad):
        super().__init__(nombre,apellido)
        self.nacionalidad = nacionalidad
    
class Libro:
    def __init__(self, titulo, autor, isbn, paginas, edicion, editorial, ciudad, pais, fecha_edicion):
        self.titulo = titulo
        self.autor = autor  # Instancia de la clase Persona
        self.isbn = isbn
        self.paginas = paginas
        self.edicion = edicion
        self.editorial = editorial
        self.ciudad = ciudad
        self.pais = pais
        self.fecha_edicion = fecha_edicion
    
    def get_titulo(self): 
        return self.titulo
    
    def set_titulo(self, titulo): 
        self.titulo = titulo

    def get_autor(self): 
        return self.autor
    
    def set_autor(self, autor): 
        self.autor = autor

    def get_isbn(self): 
        return self.isbn
    
    def set_isbn(self, isbn): 
        self.isbn = isbn

    def get_paginas(self): 
        return self.paginas
    
    def set_paginas(self, paginas): 
        self.paginas = paginas

    def get_edicion(self): 
        return self.edicion
    
    def set_edicion(self, edicion): 
        self.edicion = edicion

    def get_editorial(self): 
        return self.editorial
    
    def set_editorial(self, editorial): 
        self.editorial = editorial

    def get_ciudad(self): 
        return self.ciudad
    
    def set_ciudad(self, ciudad): 
        self.ciudad = ciudad

    def get_pais(self): 
        return self.pais

    def set_pais(self, pais): 
        self.pais = pais

    def get_fecha_edicion(self): 
        return self.fecha_edicion

    def set_fecha_edicion(self, fecha): 
        self.fecha_edicion = fecha

    def leer_informacion(self):
        print("\n--- Carga de datos del Libro ---")
        self.titulo = input("Título: ")
        nom = input("Nombre del autor: ")
        ape = input("Apellido del autor: ")
        self.autor = Persona(nom, ape)
        self.isbn = input("ISBN: ")
        self.paginas = int(input("Cantidad de páginas: "))
        self.edicion = input("Edición (ej. 3a.): ")
        self.editorial = input("Editorial: ")
        self.ciudad = input("Ciudad: ")
        self.pais = input("País: ")
        self.fecha_edicion = input("Fecha de edición (texto): ")

    def mostrar_informacion(self):
        print(f"\nTítulo: {self.titulo} {self.edicion} edición")
        if self.autor:
            print(f"Autor: {self.autor.get_nombre_completo()}")
        else:
            print("Autor: No especificado")
        print(f"ISBN: {self.isbn}")
        print(f"{self.editorial}, {self.ciudad} ({self.pais})")
        print(f"{self.fecha_edicion}")
        print(f"{self.paginas} páginas")

# --- Prueba del programa ---

autor_ejemplo = Autor("Y. Daniel", "Liang","Estadounidense")

libro_ejemplo = Libro(
    titulo="Introduction to Java Programming",
    autor=autor_ejemplo,
    isbn="0-13-031997-X",
    paginas=784,
    edicion="3a.",
    editorial="Prentice-Hall",
    ciudad="New Jersey",
    pais="USA",
    fecha_edicion="viernes 16 de noviembre de 2001"
)

libro_ejemplo.mostrar_informacion()