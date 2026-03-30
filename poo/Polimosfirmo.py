
class Animal:
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        return "Guau"

class Gato(Animal):
    def hablar(self):
        return "Miau"

#funcion polimorfica
def hacer_hablar(Animal):
    print(f"El animal dice: {Animal.hablar()}")

perro=Perro()
gato=Gato()

hacer_hablar(perro)
hacer_hablar(gato)


