import math #importando math 

ARCOCOSENO = math.acos #Declarando arcocoseno como una constante
GRADOS = math.degrees #Declarando la conversión de radianes a grados como una constante

import paquete.shape as shape

class Triangle(shape.Shape): #Subclase
    def __init__(self, is_regular:bool, vertices:list=[shape.point.Point], edges:list=[shape.line.Line]):
        super().__init__(is_regular, vertices, edges) #Llamando atributos y métodos de la clase base
    
    def compute_area(self):#Polimorfismo
        #Para calcular el área de los triangulos se usa la fórmula de Herón
        #Formula de Herón:(s(s-a)(s-b)(s-c))**0.5, donde s=(a+b+c)/2
        x = 0
        sum = 0 #suma de la longitud de todos los lados del triángulo
        while x<len(self.get_edges()):
            sum+=self.get_edges()[x].get_length()
            x+=1
        s = sum/2 #Se calcula s 
        area = (s*(s-self.get_edges()[0].get_length())*(s-self.get_edges()[1].get_length())*(s-self.get_edges()[2].get_length()))**0.5
        #Se usa la formula de Herón
        return area

    def compute_perimeter(self):#Polimorfismo
        x = 0
        sum = 0 #suma de la longitud de todos los lados del triángulo
        while x<len(self.get_edges()):
            sum+=self.get_edges()[x].get_length()
            x+=1
        return sum

    def compute_inner_angles(self):#Polimorfismo
        #Para calcular los ángulos se usa la ley del coseno
        #a,b y c corresponden a cada uno de los lados del triángulo
        a = self.get_edges()[0].get_length()
        b = self.get_edges()[1].get_length()
        c = self.get_edges()[2].get_length()
        #Se obtiene cada uno de los ángulos con teniendo en cuenta la fórmula: a^2=b^2+c^2-2bc*cosA
        angle_a = (GRADOS(ARCOCOSENO((a**2-b**2-c**2)/(-2*b*c))))
        angle_b = (GRADOS(ARCOCOSENO((b**2-a**2-c**2)/(-2*a*c))))
        angle_c = (GRADOS(ARCOCOSENO((c**2-b**2-a**2)/(-2*a*b))))
        return [angle_a, angle_b, angle_c]


