class CuentaAhorro:
    def __init__(self, titular, saldo_inicial, interes_anual):
        # Atributos privados
        self.__titular = titular
        self.__saldo = saldo_inicial
        self.__interes_anual = interes_anual

    # Método para depositar dinero
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
        else:
            raise ValueError("El monto a depositar debe ser positivo")
    
    # Método para retirar dinero
    def retirar(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
        else:
            raise ValueError("Fondos insuficientes o monto inválido")
        
    # Método para consultar el saldo actual
    def consultar_saldo(self):
        return self.__saldo

    # Método para consultar el titular
    def consultar_titular(self):
        return self.__titular
    
    # Método para aplicar el interés anual al saldo
    def aplicar_interes(self):
        self.__saldo += self.__saldo * (self.__interes_anual / 100)

    # Método para consultar el porcentaje de interés actual
    def consultar_interes(self):
        return self.__interes_anual

# Ejemplo de uso:
cuenta_ahorro = CuentaAhorro("Juan Perez", 1000, 5)

print(f"Titular: {cuenta_ahorro.consultar_titular()}")
print(f"Saldo Inicial: {cuenta_ahorro.consultar_saldo()}")
print(f"Interés Anual: {cuenta_ahorro.consultar_interes()}%")

# Depositar dinero
cuenta_ahorro.depositar(500)
print(f"Saldo después de depositar 500: {cuenta_ahorro.consultar_saldo()}")

# Aplicar interés anual
cuenta_ahorro.aplicar_interes()
print(f"Saldo después de aplicar interés: {cuenta_ahorro.consultar_saldo()}")

# Retirar dinero
cuenta_ahorro.retirar(200)
print(f"Saldo después de retirar 200: {cuenta_ahorro.consultar_saldo()}")
