class Producto:
    def __init__(self, nombre_prducto, precio):
        self.__nombre_producto = nombre_prducto
        self.__precio = precio


    def CambiarPrecio(self, cambiar_precio):
        if cambiar_precio > 0:
            self.__precio = cambiar_precio
        else:
           raise ValueError("El precio debe ser positivo")

    def ConsultarPrecio(self):
        return self.__precio
    
    def ConsultarNombre(self):
        return self.__nombre_producto

    def Descuento(self, porcentaje_descuento):
        if 0 <= porcentaje_descuento <=100:
            descuento = self.__precio * (porcentaje_descuento /100)
            self.__precio -= descuento
        else:
            raise ValueError ("El descuento debe estar entre 0 y 100")

producto = Producto("laptop", 1500)

print(f"nombre: {producto.ConsultarNombre()}")
print(f"Precio: {producto.ConsultarPrecio()}")

producto.CambiarPrecio(1200)
print(f"Precio: {producto.ConsultarPrecio()}")

producto.Descuento(20)
print(f"Descuento: {producto.ConsultarPrecio()}")

