class Rectangulo:
    def __init__(self, largo, ancho):
        self.__largo = largo
        self.__ancho = ancho

    def CambiarDimensiones(self, nlargo, nancho):
        if nlargo  > 0 < nancho:
            self.__largo = nlargo
            self.__ancho = nancho
        else:
            raise ValueError("El largo y ancho deben ser positivos")
        
        #Calculamos el perimetro del rectangulo
    def CalcularAreayPerimetro(self):
        Area = self.__ancho * self.__largo
        perimetro = 2 * (self.__largo + self.__ancho)

        print(f"Area: {Area}")
        print(f"Perimetro {perimetro}")

    
    def ConsutarDimensiones(self):
        return f"Ancho: {self.__ancho}", f"Largo: {self.__largo}"
    
#creamos el objeto
figura = Rectangulo(20, 37)

#consultamos las dimensiones actuales y el perimetro
print(figura.ConsutarDimensiones())
print(figura.CalcularAreayPerimetro())

#Cambiamos las dimensiones
figura.CambiarDimensiones(18, 50)
#Consultamos las dimensiones y el perimetro despues de cambiar las dimensiones
print(figura.ConsutarDimensiones())
print(figura.CalcularAreayPerimetro())
