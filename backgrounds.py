import pygame
from pygame.locals import *
from pygame.sprite import Sprite

class BG_Class(Sprite):

	def __init__(self,DISPLAYSURF,mi_setting):
		super(BG_Class, self).__init__()

		self.DISPLAYSURF=DISPLAYSURF
		self.mi_setting=mi_setting
		self.bg_img=pygame.image.load("./images/icons8-cloud-80(1).png")
		self.rect=self.bg_img.get_rect()

		self.rect.x = self.rect.x
		self.rect.y = self.rect.y

	def draw_BG(self):
		self.DISPLAYSURF.blit(self.bg_img,(self.rect.x,self.rect.y))
		self.rect.x-=12