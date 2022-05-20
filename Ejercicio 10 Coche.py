# if __name__ == '__main__':

class Vehículo:
    color = "verde"
    doors = 4
    wheels = 4


class Coche(Vehículo):
    velocidad = 120
    cilindrada = 8

    def imprimir_elementos(self):
        print("Propiedades vehículo: ", "color:", self.color,
              ", puertas: ", self.doors, ", llantas: ", self.wheels)
        print("Propiedades de Coche: ", "velocidad: ", self.velocidad,
              ", cilindrada:", self.cilindrada)


coche = Coche()
coche.imprimir_elementos()
