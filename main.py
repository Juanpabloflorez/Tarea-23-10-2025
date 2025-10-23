#Autor: Juan Pablo Florez Rubio

class Animal:

    def __init__(self, especie, edad):

        self.especie = especie
        self.edad = edad

        def hablar(self):
            pass

        def moverse(self):
            pass

        def describeme(self):
            pass

class BiomasaPanspermica(Animal):

    def hablar(self):
        print("*Se comunica con cambios en su temperatura corporal*")

    def moverse(self):
        print("Usa ventosas para jalar el suelo")

    def describeme(self):
        print("Hola, salí de un meteoro para reproducir mi especie en este planeta para preservar mi especie")

    def reproducir(self):
        print("Expulsa esporas que crecen rapidamente con la luz proporcionada por una estrella amarilla")

class EstrellaDeMar(Animal):
    def hablar(self):
        print("Expulsa burbujas")

    def moverse(self):
        print("usa cambios de presion en el agua")

    def describeme(self):
        print("Hola, soy una estrella de mar, tengo simetria pentalateral y consumo crustaceos pequenos")

    def comer(self):
        print("Disuelvo organismos pequenos con enzimas en mi superficie")

class Blob(Animal):
    def hablar(self):
        print("Hace sonidos de ultra baja frecuencia")

    def moverse(self):
        print("Usa sus aletas gigantes para desplazarse")

    def describeme(self):
        print("Hola, soy una especie marina gigante, soy conocido unicamente por los sonidos extremadamente fuertes que emito")

    def AccionTerrorifica(self):
        print("Soy capaz de hundir cualquier embarcacion y mi capacidad mental me permite competir con el hombre intelectualmente")

def main():
    especieDesconocida = BiomasaPanspermica("Desconocido", 1539)
    especieDesconocida.describeme()

if __name__ == "__main__":
    main()
