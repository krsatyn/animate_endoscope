import numpy as np

from ursina import *

class Endoscope(Entity):
    
    # Параметры эндоскопа
    def __init__(self, diametr = 10, radius = 50, resolution=6, len_endoscope=300, start_coordinate=[0,0,0], color_connection = color.orange, ) -> None:
        
        radius = diametr / 2
        
        # Установка начальных координат
        self.start_coordinate = start_coordinate
        
        #Длина эндоскопа
        self.len_endoscope = len_endoscope
        
        # Установка конечной коорлинаты 
        self.end_coordinate = [start_coordinate[0] , start_coordinate[1], start_coordinate[2] ]
        
        # Расчет наклона эндоскопа 
        vector_endoscope =  start_coordinate
        vector_endoscope[2] = vector_endoscope[2] - len_endoscope
        self.vector_endoscope = (vector_endoscope[0], vector_endoscope[1], vector_endoscope[2])
        
        # Создание Эндоскопа 
        self.endoscope = Entity(model=Cylinder(resolution=resolution, direction=self.vector_endoscope, radius=radius), position=self.start_coordinate, color=color_connection)


    # Перемещение на стартовую координату
    def get_start(self, ) -> None:
        pass
    
    
    # Создание оповещения о фиксации эндоскопа
    def markup_cylindre_position(self, ) -> None:
        pass
    
    # Метод анимации эндоскопа
    def update(self,) -> None:
        pass
    
    
    # Метод удаления обьекта
    def delete_endoscop(self,)->None:
        pass
