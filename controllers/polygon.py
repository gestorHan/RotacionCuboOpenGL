import numpy as np

class Polygon:
    def __init__(self,
                 polygon_vertices: list,
                 ):
        polygon_colors = np.array([
                                    [0.5, 0.5, 0.5], 
                                    np.random.rand(3), 
                                    np.random.rand(3), 
                                    [0, 0, 0]
                                    ]).flatten()
        self.original_vertices = np.array(polygon_vertices, dtype=np.float32)/2
        self.actual_vertices = np.copy(self.original_vertices)
        self.rotation_angle = 0 
        self.colors = np.array(polygon_colors, dtype=np.float32)
        self.sides = len(polygon_vertices)
        self.TA ,self.TB = self.pre_calc()


    def get_vertices(self):
        return self.actual_vertices
    def get_colors(self):
        return self.colors
    def get_sides(self):
        return self.sides
    def get_angle(self):
        return self.rotation_angle

    def pre_calc(self):
        #matrices que calcule durante el examen v':
        T1 =[
            [np.sqrt(2)/2,0,np.sqrt(2)/2],
            [0,1,0],
            [-np.sqrt(2)/2,0,np.sqrt(2)/2],
        ]
        T2 =[
            [np.sqrt(6)/3,np.sqrt(3)/3,0],
            [-np.sqrt(3)/3,np.sqrt(6)/3,0],
            [0,0,1],
        ]
        T4 =[
            [np.sqrt(6)/3,-np.sqrt(3)/3,0],
            [np.sqrt(3)/3,np.sqrt(6)/3,0],
            [0,0,1],
        ]
        T5 =[
            [np.sqrt(2)/2,0,-np.sqrt(2)/2],
            [0,1,0],
            [np.sqrt(2)/2,0,np.sqrt(2)/2],  
        ]
        return np.dot(T2,T1),np.dot(T5,T4)  

    def rotate_around_corner(self , aditional):
        self.rotation_angle = (self.rotation_angle+aditional)%360
        alpha = ((self.rotation_angle)*np.pi)/180
        T3 =[
            [1,0,0],
            [0,np.cos(alpha),-np.sin(alpha)],
            [0,np.sin(alpha),np.cos(alpha)],
        ]
        # M = T5xT4xT3xT2xT1
        # M = TBxT3xTA
        M = np.dot(self.TB,np.dot(T3,self.TA))
        def rotate_vertex (vertex):
            return np.dot(M,vertex)

        self.actual_vertices = np.array(list(map(rotate_vertex, self.original_vertices)))
        #self.actual_vertices = np.dot(M,self.original_vertices)