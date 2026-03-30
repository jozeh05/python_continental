class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def describir(self):
        return f"Vehiculo de marca {self.marca}"

class Coche(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca)
        self.modelo = modelo
    def detalle(self):
        return f"{self.describir()} - Modelo: {self.modelo}"

mi_coche = Coche("Toyota","Corolla")
print(mi_coche.detalle())