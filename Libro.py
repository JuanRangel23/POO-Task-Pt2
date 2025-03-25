class libro:
    def __init__(self, titulo, autor, total_paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__totalpaginas = total_paginas
        self.__paginaactual = 1
    
    def AdelantarPagina(self, adelantar):
        if self.__paginaactual + adelantar > self.__totalpaginas:
            raise ValueError("Supero el numero total de paginas")
       
        self.__paginaactual += adelantar
        
    def RetrocederPagina(self, retroceder):
        if self.__paginaactual - retroceder < 1:
            raise ValueError("No puede retroceder mas alla de la pagina #1")
        self.__paginaactual -= retroceder
        
    def ConsultarPagina(self):
        return self.__paginaactual
    
    def InfoLibro(self):
        return self.__titulo, self.__autor, self.__totalpaginas, self.__paginaactual

libro1 = libro("Historias de un naufrago", "Gabriel Garcia Marquez", 100)

print(libro1.InfoLibro())
print(f"Pagina Actual: {libro1.ConsultarPagina()}")

libro1.AdelantarPagina(80)
print(f"Adelanto: {libro1.ConsultarPagina()}")

libro1.RetrocederPagina(50)
print(f"Retrocedio: {libro1.ConsultarPagina()}")


libro1.AdelantarPagina(90)
print(libro1.ConsultarPagina())


