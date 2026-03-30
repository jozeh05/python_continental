class Coche:
    color="rojo"
    marca="Nisaan"
    modelo="AD"
    velocidad=300
    caballaje=500
    plazas=2

    def setcolor(self,color):
        self.color=color

    def getcolor(self):
        return self.color

    def setmodelo(self,modelo):
        self.modelo=modelo

    def getmodelo(self):
        return self.modelo

    def acelerar(self):
        self.velocidad+=1

    def frenar(self):
        self.velocidad-=1

    def getvelocidad(self):
        return self.velocidad

    #Crear los objetos e instancarlos
coche=Coche()

coche.setcolor("Amarillo")
coche.setmodelo("Murcielago")

print(coche.marca,coche.getmodelo(),coche.getcolor())
print("Vehiculo actual :",coche.getvelocidad())

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()


coche.frenar()
coche.frenar()

print("Velocidad nueva:",coche.getvelocidad())