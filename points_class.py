import json
import numpy as np

from ursina import *

"""Класс для отображения точек"""
class Points():
    
    def __init__(self, json_path) -> None:
        self.json_path = json_path
        

    """Распаковщик json файлов"""
    def json_unpacking(self) -> dict:

        with open(self.json_path) as json_file:
            data = json.load(json_file)
            
        return data
    
    
    """Создание точки по координатам"""
    def create_point(self, coordinate_dict, color_point=color.red) -> Entity:
        
        coordinate = (float(coordinate_dict['X']), float(coordinate_dict['Y']), float(coordinate_dict['Z']))
        
        return Entity(model='sphere', position=Vec3(coordinate), color=color_point)
    

    """Создание структуры points = {start:[[start_coordinate_1],[start_coordinate_2]], end:[[end_coordinate_1],[end_coordinate_2]]}"""
    def get_points_from_json(self) -> dict:
        
        coordinate = self.json_unpacking()
        json_dict_keys = list(coordinate.keys())
        
        start_coordinates = []
        end_coordinates   = []
        
        #test_list = ""
        
        for json_dict_key in json_dict_keys:
            
            #index_point+=1
            
            #oint_namber = float(test_list.split("_")[1])
            
            point_name = "hole_" + str(json_dict_key.split("_")[1])
            
            start_coordinates.append(coordinate[point_name]['start'])
            end_coordinates.append(coordinate[point_name]['end'])
        
        point_dict = {'start':start_coordinates, 'end':end_coordinates}
        
        return point_dict


    '''Создание списка точек (на четный индекс стартов на нечет конечная)'''
    def create_points(self, color_start=color.rgb(.66, .170, .255), color_end=color.green) -> list:
        
        coordinate_list = self.get_points_from_json()
        
        object_list = []
        
        for index in range(len(coordinate_list['start'])):
            
            new_point = self.create_point(coordinate_list['start'][index], color_point=color_start)
            object_list.append(new_point)
            new_point = self.create_point(coordinate_list['end'][index], color_point=color_end)
            object_list.append(new_point)
        
        return object_list    
   
   
    '''Создание  метки'''
    def create_label(self, label_text='я метка', label_location={'x':0, 'Y':0, "Z":0}, text_color = color.white, prnt=0, label_size = 0.25, scale=100) -> Text:
        
        #print(f"{label_location=}")
        
        label = Text(label_text, x=float(label_location['x'])-10, y=float(label_location['Y'])+2.5, z=float(label_location['Z']), scale=100, color=color.red, parent=prnt, text_size=2)
        
        return label
    
    
    """Создание списка меток"""
    def create_labels(self, points:list) -> list:
           
        label_list = []
        
        for index_point in range(int(len(points)/2)):
            for index in range(len(points)):
                
                new_label = self.create_label(label_text=f"Точка №{index_point+1} (Начало)", prnt=points[index])
                label_list.append(new_label)
            
                new_label = self.create_label(label_text=f"Точка №{index_point+1} (Конец)", prnt=points[index+1])
                label_list.append(new_label)
                
                points.pop(index+1)
                points.pop(index)

                break
                
        return label_list
    
    
    '''Создание связи между точкой старта и конца'''
    def create_connection(self, start_coordinate, end_coordinate, color_connection) -> Entity:
        
        new_connection = Entity(model=Cylinder(6, direction=end_coordinate), position=start_coordinate, color=color_connection)
        
        return new_connection
    
    
    """Создание списка связей"""
    def create_connections(self, points:dict, color_connection=color.hsv(0, 1, 0.72, 0.72) ) -> list:
        
        connections_list = []
        
        for index in range(0, len(points), 2):
            
            start_point_coordinate = points[index].position 
            end_point_coordinate = points[index+1].position 
            
            #print("start_point_coordinatestart_point_coordinatestart_point_coordinatestart_point_coordinate", start_point_coordinate)
            #print("end_point_coordinateend_point_coordinate", end_point_coordinate)
            
            turn_coordinate =  np.subtract(end_point_coordinate, start_point_coordinate)
        
            new_connection = self.create_connection(start_coordinate=(start_point_coordinate[0], 
                                                                      start_point_coordinate[1],
                                                                      start_point_coordinate[2]), 
                                                    
                                                    end_coordinate = (turn_coordinate[0], 
                                                                      turn_coordinate[1], 
                                                                      turn_coordinate[2]), 
                                                    
                                                    color_connection=color_connection)
            
            connections_list.append(new_connection)
        
        
            #print(len(connections_list))
            
        return connections_list
    
    
    def connect_endoscope_to_detail(self, point_coordinate, endoscop_coordinate) -> list:
        
        connection_list = []
        
        for index_endoscop_point in range(len(endoscop_coordinate)):
            
            for index_point in range(len(point_coordinate)):
                
                #endoscop_coordinate[start] point_coordinate[end] 
            
                turn_coordinate =  np.subtract(np.array(point_coordinate[index_point+1].position), np.array(endoscop_coordinate[index_endoscop_point].position))
                
                #print(f"{endoscop_coordinate[index_endoscop_point]=}")
                #print(f"{point_coordinate[index_point+1]=}")
                connections = self.create_connection(start_coordinate=endoscop_coordinate[index_endoscop_point].position, 
                                                     end_coordinate=(turn_coordinate[0],turn_coordinate[1],turn_coordinate[2]), 
                                                     color_connection=color.hsv(0, 0.2, 0.5, .5))
                connection_list.append(connections)
                
                point_coordinate.pop(index_point+1)
                point_coordinate.pop(index_point)
                
                break
        
        
        """
        for index_endoscop_point in range(0, len(endoscop_coordinate), 2):
            
            for index_point in range(0, len(point_coordinate),2):
                
                #endoscop_coordinate[start] point_coordinate[end] 
            
                turn_coordinate =  np.subtract(np.array(point_coordinate[index_point+1].position), np.array(endoscop_coordinate[index_endoscop_point].position))
                
                #print(f"{endoscop_coordinate[index_endoscop_point]=}")
                #print(f"{point_coordinate[index_point+1]=}")
                connections = self.create_connection(start_coordinate=endoscop_coordinate[index_endoscop_point].position, 
                                                     end_coordinate=(turn_coordinate[0],turn_coordinate[1],turn_coordinate[2]), 
                                                     color_connection=color.hsv(0, 0.2, 0.5, .5))
                connection_list.append(connections)
                
                point_coordinate.pop(index_point+1)
                point_coordinate.pop(index_point)
                
                break
         """   
        return(connection_list)