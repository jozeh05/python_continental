#clase padre
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    def hablar(self):
        pass

#clase hija
class Perro(Animal):
    def hablar(self):
        return "Guau"

mi_perro = Perro("Osa")
print(mi_perro.nombre)
print(mi_perro.hablar())