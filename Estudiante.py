class Estudiante:
    def __init__(self, nombre, edad):
        self.__nombre =  nombre
        self.__edad = edad
        self.__notas = []

    def AgregarNota(self, nota):
        if 0 <= nota <= 100:
            self.__notas.append(nota)
        else:
            raise ValueError("La nota debe ser un numero entre 0 y 100")
    
    def Cal_Promedio(self):
        if len(self.__notas) == 0:
            return 0
        else:
            return sum(self.__notas) / len(self.__notas)
        
    def ConsutarNombre(self):
        return self.__nombre
    
    def ConsultarEdad(self):
        return self.__edad
    
persona = Estudiante("juan", 25 )
print(f"Nombre: {persona.ConsutarNombre()}")
print(f"Edad: {persona.ConsultarEdad()}")

persona.AgregarNota(30)
persona.AgregarNota(60)
persona.AgregarNota(10)

print(f"Su promedio es de: {persona.Cal_Promedio()}")

        