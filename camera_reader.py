import time 

class Camera_Reader():
    
    def __init__(self, camera) -> None:
        self.camera = camera
    
    def print_rotate(self, ):
        for index in range(500):
            time.sleep(50)
            print(self.camera.position)