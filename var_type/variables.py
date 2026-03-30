texto = "clases de Python"

numero = 1

decimal = 6.7

nombre="Jose Luis"
apellido="Robles Osorio"
web="www.josl.com"


print(f"{texto}/{numero}/{decimal}")

#concateno con operador
print(nombre +" " +apellido + " " + web)

#concateno con tipo f
print(f"{nombre}{apellido} - {web}")

#utilizando format
print("Hola mi nombre es {} {} y mi portal web es {}".format(nombre,apellido,web))