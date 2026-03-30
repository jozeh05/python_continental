class Casa:
    propietario = "Jairo Huaman"
    m2 = 500
    ubicacion = "2 de Agosto 390"
    precio = 250000
    coordenada = "-11.977084, -77.057950"
    partida = "73068175"
    departamento = "Lima"
    provincia = "Lima"
    distrito = "Independencia"

    def setpropietario(self, propietario):
        self.propietario = propietario

    def getpropietario(self):
        return self.propietario

    def setm2(self, m2):
        self.m2 = m2

    def getm2(self):
        return self.m2

    def setprecio(self, precio):
        self.precio = precio

    def getprecio(self):
        return self.precio

    def mostrarubicacion(self):
        return self.departamento + ", " + self.provincia + ", " + self.distrito

casa = Casa()

print("Propietario:", casa.getpropietario())
print("Metros cuadrados:", casa.getm2())
print("Precio:", casa.getprecio())
print("Ubicación:", casa.mostrarubicacion())

casa.setpropietario("Danjely Saavedra")
casa.setm2(250)
casa.setprecio(125000)

print("***** VENTA *****")
print("Nuevo propietario:", casa.getpropietario())
print("M2 del terreno actual:", casa.getm2())
print("Precio vendido:", casa.getprecio())