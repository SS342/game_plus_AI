import pygame



class Detector:
    def __init__(self, x, y, img, window, state):
        self.window = window
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.x = x
        self.y = y
        self.state = state
        self.count = 0


    def collide(self,Sprite1, Sprite2):
        if ((Sprite1.x <= Sprite2.x <= Sprite1.x + Sprite1.rect.width
             and Sprite1.y <= Sprite2.y <= Sprite1.y + Sprite1.rect.height)
                or (Sprite1.x <= Sprite2.x + Sprite2.rect.width <= Sprite1.x + Sprite1.rect.width
                    and Sprite1.y <= Sprite2.y + Sprite2.rect.height <= Sprite1.y + Sprite1.rect.height)
                or (Sprite2.x <= Sprite1.x + Sprite1.rect.width <= Sprite2.x + Sprite2.rect.width
                    and Sprite2.y <= Sprite1.y <= Sprite2.y + Sprite2.rect.height)
                or (Sprite2.x <= Sprite1.x <= Sprite2.x + Sprite2.rect.width
                    and Sprite2.y <= Sprite1.y + Sprite1.rect.height <= Sprite2.y + Sprite2.rect.height)) or \
                Sprite1.rect.collidepoint((Sprite2.rect.center)):
            return True
        else:
            return False

    def Show_Up(self, s1, eat, water):

        if self.state == 1:
            self.window.blit(self.image, (self.x, self.y))
        if self.state == 2:
            self.window.blit(pygame.transform.rotate(self.image, 90), (self.x, self.y))
        if self.state == 3:
            self.window.blit(pygame.transform.rotate(self.image, 0), (self.x, self.y))
        for i in range(len(eat)):
            if self.collide(s1, eat[i]) or self.collide(s1, water):
                self.image = pygame.image.load(
                    r"C:\Users\alexe\OneDrive\Рабочий стол\II_2\AGENT\images\Vertical\Dec2.png")
                print("up collide")
            else:
                if self.count > 100:
                    self.image = pygame.image.load(
                        r"C:\Users\alexe\OneDrive\Рабочий стол\II_2\AGENT\images\Vertical\Dec1.png")
                    self.count = 0
                else:
                    self.count += 1

    def Show_down(self, s1, eat, water):
        if self.state == 1:
            self.window.blit(self.image, (self.x, self.y))
        for i in range(len(eat)):
            if self.collide(s1, eat[i]) or self.collide(s1, water):
                self.image = pygame.image.load(
                    r"C:\Users\alexe\OneDrive\Рабочий стол\II_2\AGENT\images\Vertical\Dec2.png")
                print("down collide")
            else:
                if self.count > 100:
                    self.image = pygame.image.load(
                        r"C:\Users\alexe\OneDrive\Рабочий стол\II_2\AGENT\images\Vertical\Dec1.png")
                    self.count = 0
                else:
                    self.count += 1



    def GOR_Show_left(self, s1, eat, water):
        if self.state == 1:
            self.window.blit(self.image, (self.x, self.y))
        if self.state == 2:
            self.window.blit(pygame.transform.rotate(self.image, 90), (self.x, self.y))
        if self.state == 3:
            self.window.blit(pygame.transform.rotate(self.image, 0), (self.x, self.y))
        for i in range(len(eat)):
            if self.collide(s1, eat[i]) or self.collide(s1, water):
                self.image = pygame.image.load(
                    r"C:\Users\alexe\OneDrive\Рабочий стол\II_2\AGENT\images\Gorizontal\Dec2_.png")
                print(" LEFT IS COLLIDE")
            else:
                if self.count > 100:
                    self.image = pygame.image.load(
                        r"C:\Users\alexe\OneDrive\Рабочий стол\II_2\AGENT\images\Gorizontal\Dec1_.png")
                    self.count = 0
                else:
                    self.count += 1

    def GOR_Show_right(self, s1, eat, water):
        if self.state == 1:
            self.window.blit(self.image, (self.x, self.y))

        for i in range(len(eat)):
            if self.collide(s1, eat[i]) or self.collide(s1, water):
                self.image = pygame.image.load(
                    r"C:\Users\alexe\OneDrive\Рабочий стол\II_2\AGENT\images\Gorizontal\Dec2_.png")
                print("Right_IS COLLIDE")
            else:
                if self.count > 100:
                    self.image = pygame.image.load(
                        r"C:\Users\alexe\OneDrive\Рабочий стол\II_2\AGENT\images\Gorizontal\Dec1_.png")
                    self.count = 0
                else:
                    self.count += 1


    def Show_dec(self, s1, eat, water):
        if self.state == self.state:
            self.window.blit(self.image, (self.x, self.y))

        for i in range(len(eat)):
            if self.collide(s1, eat[i]) or self.collide(s1, water):
                self.image = pygame.image.load(
                    r"C:\Users\alexe\OneDrive\Рабочий стол\II_2\AGENT\images\Dec2.png")
                if self.state == 1:
                    print("UP LEFT COLLIDE")
                if self.state == 2:
                    print("UP RIGHT COLLIDE")
                if self.state == 3:
                    print("DOWN LEFT COLLIDE")
                if self.state == 4:
                    print("DOWN RIGHT COLLIDE")
            else:
                if self.count > 100:
                    self.image = pygame.image.load(
                        r"C:\Users\alexe\OneDrive\Рабочий стол\II_2\AGENT\images\Dec1.png")
                    self.count = 0
                else:
                    self.count += 1




class Agent:  # класс игрока(агента)
    def __init__(self, x, y, img, window):
        self.window = window
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.x = x
        self.y = y
        self.hels = 100
        self.hunger = 100
        self.thirst = 100
        self.state = 1

    def Show(self):  # отображение игрока и его стат
        if self.state == 1:
            self.window.blit(self.image, (self.x, self.y))
        if self.state == 2:
            self.window.blit(pygame.transform.rotate(self.image, -90), (self.x, self.y))
        if self.state == 3:
            self.window.blit(pygame.transform.rotate(self.image, 180), (self.x, self.y))
        if self.state == 4:
            self.window.blit(pygame.transform.rotate(self.image, 90), (self.x, self.y))
        #print("H:", self.hunger, "W", self.thirst, "HP:", self.hels)
        self.hunger -= 0.01
        self.thirst -= 0.01
        if self.hunger <= 5 or self.thirst <= 5:
            self.hels -= 1
        if self.hels <= 0:
            print("dead")
        self.draw_hungret_bar(0, 0, self.hunger)
        self.draw_hels_bar(0, 44, self.hels)
        self.draw_thirst_bar(0, 22, self.thirst)
        if self.hels < 100 and self.thirst > 49 and self.hunger > 49:
            self.hels += 1
            self.hunger -= 0.02
            self.thirst -= 0.02
        if self.x <= 0:
            self.x += 6
        if self.y <= 0:
            self.y += 6
        if self.x > 1580:
            self.x -= 6
        if self.y > 980:
            self.y -= 6
        if (self.y) <= 100:
            if self.thirst >= 93:
                self.thirst = 100
            else:
                self.thirst += 7


    def move_right(self):  # функция перемещения вправо
        self.state = 2
        self.x += 5
        self.hunger -= 0.01
        self.thirst -= 0.01

    def move_left(self):  # функция перемещения влево
        self.state = 4
        self.x -= 5
        self.hunger -= 0.01
        self.thirst -= 0.01

    def move_up(self):  # функция перемещения вверх
        self.state = 1
        self.y -= 5
        self.hunger -= 0.01
        self.thirst -= 0.01

    def move_down(self):  # функция перемещения вниз
        self.state = 3
        self.y += 5
        self.hunger -= 0.01
        self.thirst -= 0.01

    def draw_hungret_bar(self, x, y, pct):  # функция отображения полоски голода
        if pct < 0:
            pct = 0
        BAR_LENGTH = 200
        BAR_HEIGHT = 20
        fill = (pct / 100) * BAR_LENGTH
        outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
        fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
        pygame.draw.rect(self.window, (222, 196, 118), fill_rect)
        pygame.draw.rect(self.window, (0, 0, 0), outline_rect, 2)

    def draw_hels_bar(self, x, y, pct):  # функция отображения полоски хп
        if pct < 0:
            pct = 0
        BAR_LENGTH = 200
        BAR_HEIGHT = 20
        fill = (pct / 100) * BAR_LENGTH
        outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
        fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
        pygame.draw.rect(self.window, (222, 0, 0), fill_rect)
        pygame.draw.rect(self.window, (0, 0, 0), outline_rect, 2)
    def draw_thirst_bar(self, x, y, pct):  # функция отображения полоски хп
        if pct < 0:
            pct = 0
        BAR_LENGTH = 200
        BAR_HEIGHT = 20
        fill = (pct / 100) * BAR_LENGTH
        outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
        fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
        pygame.draw.rect(self.window, (0, 0, 250), fill_rect)
        pygame.draw.rect(self.window, (0, 0, 0), outline_rect, 2)

class Vision:
    def __init__(self, agent, window):
        self.agent = agent
        self.window = window
        self.Detctor_list = []
        self.D1 = Detector(self.agent.x, self.agent.y,
                           r"C:\Users\alexe\OneDrive\Рабочий стол\II_2\AGENT\images\Vertical\Dec1.png",
                           self.window, 1)

        self.D4 = Detector(self.agent.x, self.agent.y,
                           r"C:\Users\alexe\OneDrive\Рабочий стол\II_2\AGENT\images\Vertical\Dec1.png",
                           self.window, 1)

        self.D7 = Detector(self.agent.x, self.agent.y,
                           r"C:\Users\alexe\OneDrive\Рабочий стол\II_2\AGENT\images\Gorizontal\Dec1_.png",
                           self.window, 1)

        self.D10 = Detector(self.agent.x, self.agent.y,
                           r"C:\Users\alexe\OneDrive\Рабочий стол\II_2\AGENT\images\Gorizontal\Dec1_.png",
                           self.window, 1)

        self.Up_left = Detector(self.agent.x, self.agent.y,
                           r"C:\Users\alexe\OneDrive\Рабочий стол\II_2\AGENT\images\Dec1.png",
                           self.window, 1)
        self.Up_Right = Detector(self.agent.x, self.agent.y,
                                r"C:\Users\alexe\OneDrive\Рабочий стол\II_2\AGENT\images\Dec1.png",
                                self.window, 2)
        self.Down_left = Detector(self.agent.x, self.agent.y,
                                r"C:\Users\alexe\OneDrive\Рабочий стол\II_2\AGENT\images\Dec1.png",
                                self.window, 3)
        self.Down_Right = Detector(self.agent.x, self.agent.y,
                                r"C:\Users\alexe\OneDrive\Рабочий стол\II_2\AGENT\images\Dec1.png",
                                self.window, 4)


    def show(self, eat, water):
        self.eat = eat
        self.D1.x = self.agent.x + 0
        self.D1.y = self.agent.y + 20
        self.D1.Show_down(self.D1, self.eat, water)

        self.D4.x = self.agent.x + 0
        self.D4.y = self.agent.y - 80
        self.D4.Show_Up(self.D4, self.eat, water)

        self.D7.x = self.agent.x + 20
        self.D7.y = self.agent.y + 0
        self.D7.GOR_Show_right(self.D7, self.eat, water)

        self.D10.x = self.agent.x - 80
        self.D10.y = self.agent.y + 0
        self.D10.GOR_Show_left(self.D10, self.eat, water)

        self.Up_left.x = self.agent.x - 70
        self.Up_left.y = self.agent.y - 70
        self.Up_left.Show_dec(self.Up_left, self.eat, water)

        self.Up_Right.x = self.agent.x + 30
        self.Up_Right.y = self.agent.y - 70
        self.Up_Right.Show_dec(self.Up_Right, self.eat, water)

        self.Down_left.x = self.agent.x - 70
        self.Down_left.y = self.agent.y + 30
        self.Down_left.Show_dec(self.Down_left, self.eat, water)

        self.Down_Right.x = self.agent.x + 30
        self.Down_Right.y = self.agent.y + 30
        self.Down_Right.Show_dec(self.Down_Right, self.eat, water)

