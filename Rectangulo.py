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
        
    def CalcularAreayPerimetro(self):
        Area = self.__ancho * self.__largo
        perimetro = 2 * (self.__largo + self.__ancho)

        print(f"Area: {Area}")
        print(f"Perimetro {perimetro}")

    
    def ConsutarDimensiones(self):
        
        return f"Ancho: {self.__ancho}", f"Largo: {self.__largo}"

figura = Rectangulo(20, 37)

print(figura.ConsutarDimensiones())
print(figura.CalcularAreayPerimetro())

figura.CambiarDimensiones(18, 50)
print(figura.ConsutarDimensiones())
print(figura.CalcularAreayPerimetro())
