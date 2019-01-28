import pygame
from pygame.locals import *

class Si_Ship():

	def __init__(self):
		
		self.ship_img=pygame.image.load('./images/icons8-space-shuttle-64.png')
		self.ship_blast=pygame.image.load('./images/icons8-rock-80(1).png')
		self.rect= self.ship_img.get_rect()
		self.rect.y=50

		self.ship_yMIN=50
		self.ship_yMAX=527
		self.ship_xMAX=700
		self.ship_xMIN=5
