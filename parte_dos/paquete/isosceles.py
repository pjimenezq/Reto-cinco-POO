import paquete.triangle as triangle

class Isosceles(triangle.Triangle):#Subclase
    def __init__(self, is_regular: bool, vertices: list = [triangle.shape.point.Point], edges: list = [triangle.shape.line.Line]):
        super().__init__(is_regular, vertices, edges)#Llamando atributos y métodos de la clase base

