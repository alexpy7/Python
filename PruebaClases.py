class Coche:
    def __init__(self,marca,modelo,potencia):
        self.marca = marca
        self.modelo = modelo
        self.potencia = potencia
        self.arrancado = False
        self.velocidad = 0

    def __str__(self):
        return "Es un {} {} con {} CV".format(self.marca,self.modelo,self.potencia)

    def arrancar(self):
        if not self.arrancado:
            print("Arrancando...... \nStatus: Arrancado")
            self.arrancado = True
        else:
            print("El coche ya esta arrancado")

    def apagar(self):
        if self.arrancado and self.velocidad == 0:
            print("Apagando..\nStatus: Apagado")
            self.arrancado = False
        elif self.arrancado and self.velocidad > 0:
            print("Antes de apagar debe parar")
        else:
            print("El coche ya esta apagado")


    def acelerar(self):
        if self.arrancado:
            self.velocidad += 50
            return "{} km/h".format (self.velocidad)
        else:
            print("El coche no esta arrancado")

    def fullgas(self):
        if self.arrancado:
            self.velocidad += 150
            return"{} km/h".format (self.velocidad)
        else:
            print("El coche no esta arrancado")

    def frenazo(self):
        if self.arrancado and self.velocidad >= 50:
            self.velocidad -= 100
            print("Frenando..", self.velocidad,"km/H")
        elif self.arrancado and self.velocidad < 50:
            self.velocidad = 0
            print("Frenando y parando velocidad:", self.velocidad)
        else:
            print("El coche ya esta parado")



    def frenar(self):
        if self.arrancado and self.velocidad >= 50:
            self.velocidad -= 50
            print("Frenando..",self.velocidad)
        elif self.arrancado and self.velocidad <50:
            self.velocidad = 0
            print("Frenando y parando velocidad:",self.velocidad)
        else:
            print("El coche ya esta parado")

    def parar(self):
        if self.arrancado and self.velocidad > 0:
            print("El coche acaba de parar")
            self.velocidad = 0
        else:
            print("El coche ya esta parado")

    def status(self):
        print("Es un {} {} con {} CV".format(self.marca,self.modelo,self.potencia))
        if self.arrancado:
            print("Estado: Arrancado")
        else:
            print("Estado: Apagado")
        print("La velodidad actual es de:",self.velocidad,"km/h")


coche = Coche("BMW","M4",560)
print(coche)
print("\nFunciones que se pueden utlizar:\nArrancar\nParar\nAcelerar\nFrenar\nFullgas\nFrenazo\n")
coche.parar()


