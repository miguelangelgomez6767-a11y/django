class cuenta:
    def __init__(self, numero, saldo):#contructor
        self.numero = numero
        self.__saldo = saldo

    def depositar(self, cantidad):#Metodos o comportamientos
        if cantidad > 0:
            self.__saldo += cantidad

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad


    def imprimir_saldo(self):
        return f"Su saldo actual es: {self.__saldo}"


#creacion del objeto 
cuenta1 = cuenta("1111", 1000)
cuenta1.depositar(11000)
cuenta1.retirar(11999)
print(cuenta1.numero)
print(cuenta1.imprimir_saldo())












