import pygame
import random
from HABITAT.Settings import SETTINGS
from AGENT.Agent import Agent as A
from AGENT.Agent import Vision as Vision


class Water:  # класс воды
    def __init__(self, x, y, img, window):
        self.window = window
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.x = x
        self.y = y

    # отображение воды
    def Show(self):
        self.window.blit(self.image, (self.x, self.y))
# класс еды
class Eat:
    def __init__(self, x, y, img, window, iter=1, state=1):
        self.window = window
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.x = x
        self.y = y
        self.iter = iter
        self.state = state

    # отображение еды
    def Show(self):

        self.window.blit(self.image, (self.x, self.y))


# главное окно среды

class HABITAT:
    def __init__(self):
        self._count = 1
        # инициализация класса настоек
        self.Set = SETTINGS()
        # создание окна
        self.screen = pygame.display.set_mode((self.Set.WIDTH, self.Set.HEIGHT))
        pygame.display.set_caption("AI")
        self.clock = pygame.time.Clock()
        self.AI_RUN = True
        self.Agent = A(
            self.Set.Start_agent_x,  # наш персонаж
            self.Set.Start_agent_y,  # наш персонаж
            r"C:\Users\alexe\OneDrive\Рабочий стол\II_2\HABITAT\Image\Agent.png",
            self.screen
        )
        self.All_Eat = []  # список с едой, которая отображается
        self.count = 1
        self.Eat_count = 0
        self.Eat_eat = []  # еда, которая была съедена и находится на перезарядке
        self.Vision = Vision(self.Agent, self.screen)


    # функция создания еды
    def create_Eat(self):

        self.E1 = Eat(random.randint(0, 1580), random.randint(120, 980), r"C:\Users\alexe\OneDrive\Рабочий стол\II_2\HABITAT\Image\Eat.png", self.screen)
        self.All_Eat.append(self.E1)
        self.Eat_count = 1
    # функция проверки столкновения игрока и еды
    def collide(self, Sprite1, Sprite2):
        if ((Sprite1.x <= Sprite2.x <= Sprite1.x + Sprite1.rect.width
             and Sprite1.y <= Sprite2.y <= Sprite1.y + Sprite1.rect.height)
                or (Sprite1.x <= Sprite2.x + Sprite2.rect.width <= Sprite1.x + Sprite1.rect.width
                    and Sprite1.y <= Sprite2.y + Sprite2.rect.height <= Sprite1.y + Sprite1.rect.height)
                or (Sprite2.x <= Sprite1.x + Sprite1.rect.width <= Sprite2.x + Sprite2.rect.width
                    and Sprite2.y <= Sprite1.y <= Sprite2.y + Sprite2.rect.height)
                or (Sprite2.x <= Sprite1.x <= Sprite2.x + Sprite2.rect.width
                    and Sprite2.y <= Sprite1.y + Sprite1.rect.height <= Sprite2.y + Sprite2.rect.height)):
            if self.Agent.hunger >= 80:
                self.Agent.hunger = 100
            else:
                self.Agent.hunger += 20
            return True
        else:
            return False
    # функция зпуска самой игры
    def RUN(self):
        self.Water = Water(0, 0, r"C:\Users\alexe\OneDrive\Рабочий стол\II_2\HABITAT\Image\water.png", self.screen)

        while self.AI_RUN:
            # функция создания еды
            if self._count < 11:
                if self.count < 36000 and self.count % 3 == 0 and len(self.All_Eat) < 11:
                    self.create_Eat()
                    self._count += 1
            # перезарядка еды
            if len(self.Eat_eat) > 0:
                for i in range(len(self.Eat_eat)):
                    if self.Eat_eat[i].state * 5 < self.Eat_eat[i].iter:
                        self.Eat_eat[i].iter = 1

                        self.Eat_eat[i].x = random.randint(0, 1580)
                        self.Eat_eat[i].y = random.randint(120, 980)
                        self.All_Eat.append(self.Eat_eat[i])
                        del self.Eat_eat[i]
                    else:
                        self.Eat_eat[i].iter += 1


            self.clock.tick(self.Set.FPS)
            self.screen.fill(self.Set.GREEN)
            self.Water.Show()
            self.Vision.show(self.All_Eat, self.Water)
            self.Agent.Show()
            pygame.display.flip()
            # отображение еды
            if self.Eat_count == 1:
                try:
                    for i in range(len(self.All_Eat)):
                        self.All_Eat[i].Show()
                        if self.collide(self.Agent, self.All_Eat[i]):
                            self.All_Eat[i].state += 1
                            self.Eat_eat.append(self.All_Eat[i])
                            del self.All_Eat[i]
                except:
                    print("exept")
                    for i in range(len(self.All_Eat)):
                        self.All_Eat[i].Show()
                        if self.collide(self.Agent, self.All_Eat[i]):
                            self.All_Eat[i].state += 1
                            self.Eat_eat.append(self.All_Eat[i])
                            del self.All_Eat[i]
            # проверка евенов игры
            for event in pygame.event.get():
                # проверить закрытие окна
                if event.type == pygame.QUIT:

                    self.AI_RUN = False

                elif event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RIGHT:  # кнопка перемещения вправо

                        self.Agent.move_right()

                    elif event.key == pygame.K_LEFT:  # кнопка перемещения влево

                        self.Agent.move_left()

                    elif event.key == pygame.K_UP:  # кнопка перемещения вверх

                        self.Agent.move_up()

                    elif event.key == pygame.K_DOWN:  # кнопка перемещения вниз

                        self.Agent.move_down()

                    elif event.key == pygame.K_q: # кнопка выхода

                        self.AI_RUN = False

            self.count += 1  # стадия игры

            pygame.display.update()
