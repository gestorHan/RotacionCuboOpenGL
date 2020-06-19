import glfw
from OpenGL.GL import *
from .polygon import Polygon
import numpy as np
import time


class Window:
    def __init__(self):
        self._list_of_polygons = []
        self._win = self.init_GLFW()
        self.camera_angle = -30
        self.is_rotating = False

    def init_GLFW (self):
        if not glfw.init():
            raise Exception('Glfw can not be initialized!')
        # Creating the window
        my_win = glfw.create_window(800, 800,"Rotación cubo", None, None)
        # Check if window was created
        if not my_win:
            glfw.terminate()
            raise Exception('Glfw window could not be created!')
        # Set window position
        glfw.set_window_pos(my_win, 30, 30)
        # Make the context current
        glfw.make_context_current(my_win)
        glClearColor(0.05 ,0.05, 0.05, 1)  # 222222
        return my_win
    # Main application loop
    def main_loop(self):
        # rotcion inical de camara para cambiar perspectiva
        glRotate(45, 1, 0, 0)
        glRotate(self.camera_angle, 0, 1, 0)
        glEnable(GL_CULL_FACE)
        glCullFace(GL_FRONT)
        
        initial_position = True
        add = 2
        while not glfw.window_should_close(self._win):
            glfw.poll_events()
            time.sleep(1/30)
            self.input_events()
            glClear(GL_COLOR_BUFFER_BIT)
            
            for polygon in self._list_of_polygons:
                self._draw_polygon(polygon)

            if self.is_rotating:              
                if initial_position:
                    add  = 2 
                else:
                    add = -2   
                for polygon in self._list_of_polygons:
                    polygon.rotate_around_corner(add)
                if polygon.get_angle() >= 30:
                    self.is_rotating = False
                    initial_position = False
                    print("Efectuada rotacion de 0° -> 30°")
                if polygon.get_angle() <= 0:
                    self.is_rotating = False
                    initial_position = True
                    print("Efectuada rotacion de 30° -> 0°")
            self.draw_axis()

#            if self.camera_rotation:

            glfw.swap_buffers(self._win)

        # Terminate glfw, free up allocated resources
        glfw.terminate()

    def input_events(self):
        if glfw.get_mouse_button(self._win, 0):
            glRotate(-2, 0, 1, 0)
        if glfw.get_mouse_button(self._win, 1):
            glRotate(2, 0, 1, 0)
        if glfw.get_key(self._win , 32 ): #TeclaS
            if not self.is_rotating :
                self.is_rotating = True
        if glfw.get_key(self._win , 68 ): #TeclaS
            for polygon in self._list_of_polygons:
                polygon.rotate_around_corner(-2)

    def add_polygon(self, polygon: Polygon):
        self._list_of_polygons.append(polygon)

    def draw_axis(self):
        glEnableClientState(GL_VERTEX_ARRAY)
        glVertexPointer(3, GL_FLOAT, 0, np.array([0, 0, 0,1, 0, 0, 
                                                  0, 0, 0,0, 1, 0, 
                                                  0, 0, 0,0, 0, 1, 
                                                   0, 0, 0,-1, 0, 0,
                                                   0, 0, 0,0, -1, 0,
                                                   0, 0, 0,0, 0, -1,
                                                  ]))
        glEnableClientState(GL_COLOR_ARRAY)
        # x: Red  y:green z: blue
        glColorPointer(3, GL_FLOAT, 0,  np.array([1, 0, 0, 1, 1, 1,
                                                  0, 1, 0, 1, 1, 1,
                                                  0, 0, 1, 1, 1, 1,
                                                  1, 0, 0, 0, 0, 0,
                                                  0, 1, 0, 0, 0, 0,
                                                  0, 0, 1, 0, 0, 0,
                                                  ]))
        glDrawArrays(GL_LINES, 0, 12)

    def _draw_polygon(self, polygon: Polygon):
        # Setup for the vertices
        glEnableClientState(GL_VERTEX_ARRAY)
        glVertexPointer(3, GL_FLOAT, 0, polygon.get_vertices().flatten())
        # Setup for the colors
        glEnableClientState(GL_COLOR_ARRAY)
        glColorPointer(3, GL_FLOAT, 0, polygon.get_colors())
        glDrawArrays(GL_TRIANGLE_FAN, 0, polygon.get_sides())
