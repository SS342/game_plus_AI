import numpy as np
# класс настоек, создан для быстрой сены условий среды
class SETTINGS:
    def __init__(self):
        # ширина окна
        self.WIDTH = 1600
        # высота окна
        self.HEIGHT = 1000
        # стартовая точка агента
        self.Start_agent_x = 800
        # стартовая точка агента
        self.Start_agent_y = 500
        # цвета
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 107, 82)
        self.BLUE = (0, 0, 255)
        # цвета
        # частота обновления экрана
        self.FPS = 70
        self.Gamma = 0.4
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

