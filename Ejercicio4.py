class Cancion:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        
    def cancion(sefl, ):
        pass
    
    def get_titulo(self):
        return self.titulo
    
    def get_autor(self):
        return self.autor
    
    def set_titulo(self, titulo):
        self.titulo = titulo
    
    def set_autor(self, autor):
        self.autor = autor
        

mi_cancion = Cancion("Muchachos", "La Mosca")

print(f"Título: {mi_cancion.get_titulo()}")
print(f"Autor: {mi_cancion.get_autor()}")

# Modificando los atributos con los setters
mi_cancion.set_titulo("Rezo por vos")
mi_cancion.set_autor("Charly García")

print(f"Nueva canción: {mi_cancion.get_titulo()} de {mi_cancion.get_autor()}")
    
    