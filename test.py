from endoscope import Endoscope
from ursina import *
from settings import test_model_path


window.title = "hole visualizer"    
app = Ursina(borderless=False)

# Настройки окна
window.size = (800,600)
window.exit_button.enable = True
window.cog_button.enable = False
window.fps_counter.enable = False
window.fullscreen = False

# Класс эндоскопа
endoscope = Endoscope()


# Модель stl
block = Entity(model=test_model_path, color = color.hsv(0, 0, 1, .5))

#Entity(model=Cylinder(6), color=color.orange)

#камера
EditorCamera()

app.run()