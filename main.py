import numpy as np

from ursina import *
from points_class import Points
from camera_reader import Camera_Reader
from settings import json_path, model_path, endoscope_json_path_UP, endoscope_json_path_DOWN


window.title = "hole visualizer"    
app = Ursina(borderless=False)

# Настройки окна
window.size = (800,600)
window.exit_button.enable = True
window.cog_button.enable = False
window.fps_counter.enable = False
window.fullscreen = False



# Окно ввода
#input_wnd = InputField()

#объекты 

# Инициализация класса для создания точек
point_class = Points(json_path)
endoscop_class = Points(json_path=endoscope_json_path_UP)


# Точки для верхних координат
endoscop_points = endoscop_class.create_points(color_start=color.yellow, color_end=color.pink)
endoscop_points_connections = endoscop_class.create_connections(points=endoscop_points, color_connection=color.pink)


# Точки для нижних координат
endoscop_class = Points(json_path=endoscope_json_path_DOWN)
endoscop_points = endoscop_class.create_points(color_start=color.yellow, color_end=color.pink)
endoscop_points_connections = endoscop_class.create_connections(points=endoscop_points, color_connection=color.red)


# Модель stl
block = Entity(model=model_path, color = color.hsv(0, 0, 1, .5))


# Точки заданные по координатам с json файла 
points = point_class.create_points()


point_class.connect_endoscope_to_detail(endoscop_coordinate=endoscop_points_connections, point_coordinate=points)


# Связи между точками
connections = point_class.create_connections(points=points)


#Метки к точкам
labels = point_class.create_labels(points=points)

'''
# тестовая точка и ее метка
pnt = point_class.create_point(coordinate_dict={'x':0, 'Y':0, 'Z':0})
lbl = point_class.create_label(label_text="Я центр мира!", prnt = pnt)


point_1_coordinate = [1,2,2]
point_2_coordinate = [10,2,1]

turn_coordinate =  np.subtract(point_2_coordinate, point_1_coordinate)


pnt_1 = point_class.create_point(coordinate_dict={'x':point_1_coordinate[0], 'Y':point_1_coordinate[1], 'Z':point_1_coordinate[2]}, color_point=color.green)
lbl_1 = point_class.create_label(label_text="Я  Первая!", prnt = pnt_1)

pnt_2 = point_class.create_point(coordinate_dict={'x':point_2_coordinate[0], 'Y':point_2_coordinate[1], 'Z':point_2_coordinate[2]}, color_point=color.green)
lbl_2 = point_class.create_label(label_text="Я Вторая!", prnt = pnt_2)

test_connect = point_class.create_connection(start_coordinate=(point_1_coordinate[0],point_1_coordinate[1], point_1_coordinate[2]), end_coordinate=(turn_coordinate[0], turn_coordinate[1], turn_coordinate[2]))
'''


#камера
EditorCamera()

app.run()