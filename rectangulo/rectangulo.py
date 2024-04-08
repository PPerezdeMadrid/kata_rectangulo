""" CLASE rectangulo"""

class Rectangulo():
    def __init__(self, xmin, xmax, ymin, ymax):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax

def obtener_x_y(xmin, xmax, ymin, ymax):
    # xmin = -7  xmax = -4 --> 7-4 = 3
    # xmin = -2 xmax = 4 --> 4 - (-2)
    x = xmax-xmin
    y = ymax-ymin
    return abs(x), abs(y)

def calcular_area(x,y):
    return x*y