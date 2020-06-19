from controllers.window import Window
from controllers.polygon import Polygon
import numpy as np

if __name__ == '__main__':

    win = Window()
    #puntos que conforman el cubo
    p = [
        [0, 0, 0], 
        [1, 0, 0], 
        [0, 1, 0], 
        [0, 0, 1], 
        [1, 1, 0], 
        [1, 0, 1], 
        [0, 1, 1], 
        [1, 1, 1],]
    cube = [
    #La clase polygon almacena un conjunto de punto y los muestra como un poligono
        Polygon([p[0], p[1], p[4], p[2], ]),
        Polygon([p[0], p[3], p[5], p[1], ]),
        Polygon([p[0], p[2], p[6], p[3], ]),
        Polygon([p[7], p[4], p[1], p[5], ]),
        Polygon([p[7], p[6], p[2], p[4], ]),
        Polygon([p[7], p[5], p[3], p[6], ]),
    ]

    #Añadimos cada una de las caras a la lista de cosas a mostrar
    for face in cube:
        win.add_polygon(face)

    win.main_loop()
