class Point:
    def __init__(self, x:int, y:int):
        self.__x = x
        self.__y = y
    
    # Setter x
    def set_x(self, new_x):
        self.__x = new_x

    # Getter x
    def get_x(self):
        return self.__x

    # Setter y
    def set_y(self, new_y):
        self.__y = new_y

    # Getter y
    def get_y(self):
        return self.__y
    
    def compute_distance(self, Point):
        return ((self.__x-Point.__x)**2+(self.__y-Point.__y)**2)**0.5 #Formula para calcular distancia entre dos puntos
    
