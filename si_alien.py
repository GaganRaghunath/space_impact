import pygame
from pygame.locals import *
from pygame.sprite import Sprite

class Alien1(Sprite):

	def __init__(self,DISPLAYSURF,mi_setting):
		super(Alien1, self).__init__()

		self.DISPLAYSURF=DISPLAYSURF
		self.mi_setting=mi_setting
		self.alien_img=pygame.image.load('./images/alien14.png')
		self.rect=self.alien_img.get_rect()

		self.rect.x = self.rect.x
		self.rect.y = self.rect.y

	def draw_alien(self):
		self.DISPLAYSURF.blit(self.alien_img,(self.rect.x,self.rect.y))

	def alien_update(self):
		self.rect.x-=10

class Alien2(Sprite):

	def __init__(self,DISPLAYSURF,mi_setting):
		super(Alien2,self).__init__()

		self.DISPLAYSURF=DISPLAYSURF
		self.mi_setting=mi_setting
		self.alien2_img=pygame.image.load('./images/alien7.png')
		self.rect=self.alien2_img.get_rect()

		self.rect.x = self.rect.x
		self.rect.y = self.rect.y

		self.A_life=25

	def draw_alien(self):
		self.DISPLAYSURF.blit(self.alien2_img,(self.rect.x,self.rect.y))

	def alien_update(self):
		if self.rect.y >= 600:
			self.rect.y-=10
		elif self.rect.y <= 600:
			self.rect.y+=10