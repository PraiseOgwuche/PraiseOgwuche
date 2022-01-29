import module2 as m2
import module1 as m1
from pymunk.vec2d import Vec2d
import os
import pygame
os.system("clear")


class AppWindow(m1.App):
    def __init__(self,size=(500,600)) -> None:
        super().__init__(size=size)

class DynamicMovement:
    def right_move(self):
        self.increase_velocity(Vec2d(100, 0))
    
    def left_move(self):
        self.increase_velocity(Vec2d(-100, 0))

    def upward_move(self):
        self.increase_velocity(Vec2d(0, -300))


class BaseRectangle(m2.StaticRectangle):
    def __init__(self, pos=(600, 800), dimensions= (1200, 200)):
        super().__init__(pos=pos, dimensions=dimensions)


class GameSquare(m2.DynamicSquare, DynamicMovement):
    def __init__(self, pos=(100, 100), length=55):
        super().__init__(pos=pos, length=length)
    
    def movesquare(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.right_move()  # move right
            if event.key == pygame.K_LEFT:
                self.left_move()
            if event.key == pygame.K_UP:
                self.upward_move() 

class GameCircle(m2.DynamicCircle, DynamicMovement):
    def __init__(self, pos=(75, 100), radius=50):
        super().__init__(pos=pos, radius=radius)

    def movecircle(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.right_move()
            if event.key == pygame.K_a:
                self.left_move()
            if event.key == pygame.K_w:
                self.upward_move()
            


app = AppWindow((1200,1000))
square = GameSquare()
square2 = GameSquare(pos = (150, 150))
circle = GameCircle(pos=(600,100))
circle2 = GameCircle(pos=(600,300),radius=20)
rect = BaseRectangle()
rect2 = BaseRectangle(pos = (0, 500), dimensions = (100, 1000))
rect3 = BaseRectangle(pos = (1200, 500), dimensions = (100, 1000))
app.add([square, circle, rect, rect2, rect3, square2, circle2])
app.mainloop(circle.movecircle, square.movesquare, circle2.movecircle)

