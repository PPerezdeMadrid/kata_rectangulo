""" CLASE rectangulo"""

class Rectangulo():
    def __init__(self, xmin, xmax, ymin, ymax):
        if xmax < xmin:
            raise ValueError("xmax no puede ser menor que xmin")
        if ymax < ymin:
            raise ValueError("ymax no puede ser menor que ymin")
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

def calcular_perimetro(x,y):
    return 2*x+2*y

def calcular_centro(xmin, xmax, ymin, ymax):
    x_centro = (float(xmax)-float(xmin))/2 + float(xmin)
    y_centro = (float(ymax)-float(ymin))/2 + float(ymin)
    return x_centro, y_centro

def obtener_diagonal(rectangulo):
    return rectangulo.xmin, rectangulo.ymax

def r1SeSuperponeAr2(r1, r2):
    # Si xmin está en r2
    if r1.xmin <= r2.xmin <= r1.xmax and r1.ymin <= r2.ymin <= r1.ymax:
        return True
    if r2.xmin <= r1.xmin <= r2.xmax and r2.ymin <= r1.ymin <= r2.ymax:
        return True
    if r1.xmin <= r2.xmax <= r1.xmax and r1.ymin <= r2.ymax <= r1.ymax:
        return True
    if r2.xmin <= r1.xmax <= r2.xmax and r2.ymin <= r1.ymax <= r2.ymax:
        return True
    else:
        return False