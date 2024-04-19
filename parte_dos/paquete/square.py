import paquete.rectangle as rectangle

class Square(rectangle.Rectangle):#Subclase
    def __init__(self, is_regular:bool, vertices:list=[rectangle.shape.point.Point], edges:list=[rectangle.shape.line.Line]):
        super().__init__(is_regular, vertices, edges)#Llamando atributos y métodos de la clase base

    def compute_area(self):#Polimorfismo
        if self.get_is_regular()==True:
            return self.get_edges()[0].get_length()**2#El área de un cuadrado es la longitud de cualquier elevado al cuadrado
        else:
            return "The square should be regular."
    
    def compute_perimeter(self):#Polimorfismo
        if self.get_is_regular()==True:
            return self.get_edges()[0].get_length()*4#El perimetro de un cuadrado es la longitud de cualquier lado multiplicado por 4
        else:
            return "The square should be regular."
