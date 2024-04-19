import paquete.point as point
import paquete.line as line

class Shape: #Clase base
    def __init__(self, is_regular:bool, vertices:list=[point.Point], edges:list=[line.Line]):
        self.__is_regular = is_regular 
        self.__vertices = vertices
        self.__edges = edges

    # Setter is regular
    def set_is_regular(self, new_is_regular):
        self.__is_regular = new_is_regular

    # Getter is regular
    def get_is_regular(self):
        return self.__is_regular
    
    # Setter vertices
    def set_vertices(self, new_vertices):
        self.__vertices = new_vertices

    # Getter vertices
    def get_vertices(self):
        return self.__vertices
    
    # Setter edges
    def set_edges(self, new_edges):
        self.__edges = new_edges

    # Getter edges
    def get_edges(self):
        return self.__edges
    
    def compute_area(self): #Se define el método para calcular área
        pass

    def compute_perimeter(self): #Se define el método para calcular perímetro
        pass
    
    def compute_inner_angles(self): #Se define el método para calcular ángulos internos
        pass

