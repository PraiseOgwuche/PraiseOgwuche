from module1 import pymunk, App, GRAY
from pymunk.vec2d import Vec2d
from pymunk.space_debug_draw_options import SpaceDebugColor
import pygame
pygame.init()


A = App()

class StaticRectangle:
	def __init__(self,pos=(int(A.size[0]/2), int(A.size[1]/2)), dimensions=(100,50)):
		self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
		self.body.position = pos
		brick = pymunk.Poly.create_box(self.body, dimensions)
		self.shape = brick
		self.position = pos
		self.size = dimensions
		self.velocity = Vec2d(0,0)
		self.shape.friction = 0.9
		self.shape.elasticity = 0.4
	def __repr__(self):
		return f"StaticRectangle{self.position}"

class DynamicObject:
	def increase_velocity(self,v):
		self.body.velocity += v

class DynamicCircle(DynamicObject):
	def __init__(self,pos=(int(A.size[0]/2), int(A.size[1]/2)), radius=30):
		self.body = pymunk.Body(mass=1, moment=10)
		self.body.position = pos
		circle = pymunk.Circle(self.body, radius)
		self.shape = circle
		circle.elasticity = 0.9
		self.radius = radius
		self.position = pos
		self.velocity = Vec2d(0,0)
		self.shape.friction = 0.9
	def __repr__(self):
		return f"DynamicCircle{self.position}"
	


class DynamicSquare(DynamicObject):
	def __init__(self,pos=(int(A.size[0]/2), int(A.size[1]/2)), length=40):
		self.body = pymunk.Body(mass=1, moment=10)
		self.body.position = pos
		square = pymunk.Poly.create_box(self.body, (length, length))
		self.shape = square
		square.elasticity = 0.95
		self.length = length
		self.position = pos
		self.velocity = Vec2d(0,0)
		self.shape.friction = 0.1
	def __repr__(self):
		return f"DynamicSquare{self.position}"
	

if __name__ == '__main__':
	pass


