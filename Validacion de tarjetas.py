class TarjetaCredito:
    def __init__(self, numero):
        # Almacena el número de tarjeta
        self.numero = numero

    @staticmethod
    def validar_tarjeta(numero):
        # Implementación del algoritmo de Luhn
        numero = str(numero)
        suma = 0
        longitud = len(numero)
        es_par = False

        # Recorremos los números de derecha a izquierda
        for i in range(longitud - 1, -1, -1):
            digito = int(numero[i])
            
            if es_par:
                digito *= 2
                if digito > 9:
                    digito -= 9
            suma += digito
            es_par = not es_par

        # El número es válido si la suma es múltiplo de 10
        return suma % 10 == 0

# Ejemplo de uso
tarjeta1 = TarjetaCredito("4532015112830366")
tarjeta2 = TarjetaCredito("1234567812345670")

print("¿Tarjeta 1 válida?", TarjetaCredito.validar_tarjeta(tarjeta1.numero))  # Debería ser True
print("¿Tarjeta 2 válida?", TarjetaCredito.validar_tarjeta(tarjeta2.numero))  # Debería ser False

        