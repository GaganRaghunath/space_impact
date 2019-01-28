import pygame
from pygame.sprite import Sprite

class Bullets(Sprite):
	"""This is the Bullets class"""
	def __init__(self,DISPLAYSURF,mi_setting,x,y):
		super(Bullets, self).__init__()
		self.x=x
		self.y=y
		self.DISPLAYSURF=DISPLAYSURF
		self.rect=pygame.Rect(x+65,y+30,mi_setting.Bullet_w,mi_setting.Bullet_h)
		self.b_color=mi_setting.Bullet_color

	def draw_bullet(self):
		pygame.draw.rect(self.DISPLAYSURF,self.b_color,self.rect)

	def bullet_update(self):
		self.rect.x+=15