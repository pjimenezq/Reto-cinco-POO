import paquete.shape as shape

class Rectangle(shape.Shape):#Subclase
    def __init__(self, is_regular:bool, vertices:list=[shape.point.Point], edges:list=[shape.line.Line]):
        super().__init__(is_regular, vertices, edges)#Llamando atributos y métodos de la clase base

    def compute_area(self):#Polimorfismo
        #Se obtienen las coordenadas del último punto de la primera línea dada
        vertice_x = self.get_edges()[0].get_end_point().get_x()
        vertice_y = self.get_edges()[0].get_end_point().get_y()
        x = 0
        while x<len(self.get_edges()):
            #Se busca la línea que tiene como primer punto las mismas coordenadas que el último punto de la primera linea dada
            #Lo anterior se hace para asegurarse de que se multipliquen la base y la altura del rectángulo y no los lados paralelos
            if self.get_edges()[x].get_start_point().get_x()==vertice_x and self.get_edges()[x].get_start_point().get_y()==vertice_y:
                area = self.get_edges()[0].get_length()*self.get_edges()[x].get_length() #Se multiplican la base y la altura del rectángulo
                return area
            else:
                x+=1

    def compute_perimeter(self):#Polimorfismo
        x = 0
        sum = 0#suma de la longitud de todos los lados del triángulo
        while x<len(self.get_edges()):
            sum+=self.get_edges()[x].get_length()
            x+=1
        return sum
    
    def compute_inner_angles(self):#Polimorfismo
        return [90, 90, 90, 90]#Todos los ángulos de un rectángulo miden 90 grados
    

