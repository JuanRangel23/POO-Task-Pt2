class Empleado:
    # Variable de clase que llevará el conteo de empleados creados
    contador_empleados = 0

    def __init__(self, nombre, salario):
        # Inicializamos el nombre y salario del empleado
        self.nombre = nombre
        self.salario = salario
        # Incrementamos el contador de empleados cada vez que se crea uno nuevo
        Empleado.contador_empleados += 1

    @classmethod
    def cantidad_empleados(cls):
        # Método de clase para obtener el total de empleados creados
        return cls.contador_empleados

# Ejemplo de uso
empleado1 = Empleado("Juan", 1500)
empleado2 = Empleado("Ana", 1800)
empleado3 = Empleado("Carlos", 2000)

# Imprimir la cantidad de empleados creados
print("Cantidad de empleados:", Empleado.cantidad_empleados())
