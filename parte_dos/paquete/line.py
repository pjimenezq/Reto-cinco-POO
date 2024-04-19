import paquete.point as point

class Line:
    def __init__(self, start_point:point.Point, end_point:point.Point): #Hay composición: una línea tiene dos puntos
        self.__start_point = start_point
        self.__end_point = end_point
        self.__length = start_point.compute_distance(end_point) #Length se cálcula con el método compute_distance de la clase Point

    # Setter start point
    def set_start_point(self, new_start_point):
        self.__start_point = new_start_point

    # Getter start point
    def get_start_point(self):
        return self.__start_point
    
    # Setter end point
    def set_end_point(self, new_end_point):
        self.__end_point = new_end_point

    # Getter end point
    def get_end_point(self):
        return self.__end_point
    
    # Setter length
    def set_length(self, new_length):
        self.__length = new_length

    # Getter length
    def get_length(self):
        return self.__length
