import pygame,sys,time,random
from pygame.locals import *
from si_setting import Si_Setting
from si_ship import Si_Ship
import si_control as mi_control
from si_alien import Alien1
from pygame.sprite import Group

def Main_Impact():

	pygame.init()
	mi_setting=Si_Setting()
	mi_ship=Si_Ship()
	mi_bulletGroup=Group()
	mi_alienGroup=Group()
	BG_group=Group()

	FPS=20

	fpsclock=pygame.time.Clock()

	DISPLAYSURF = pygame.display.set_mode((mi_setting.Disp_Width,mi_setting.Disp_Height))
	pygame.display.set_caption('Space Impact')
	

	St=startgame(DISPLAYSURF,mi_setting,mi_ship)

	DISPLAYSURF.fill(mi_setting.BLACK)
	DISPLAYSURF.blit(mi_ship.ship_img,(5,50))
	mi_alien1=Alien1(DISPLAYSURF,mi_setting)
	mi_setting.alien_delay=random.randint(1,5)
	mi_setting.alien_count=random.randint(1,5)

	while True:
		mi_control.check_keypress(DISPLAYSURF,mi_setting,mi_ship,mi_bulletGroup,mi_alienGroup,BG_group)
		pygame.display.update()
		fpsclock.tick(FPS)

def startgame(DISPLAYSURF,mi_setting,mi_ship):
	
	basicFont=pygame.font.SysFont(None,48)
	text=basicFont.render("CLICK SPACE TO START !!!",True,mi_setting.GREEN,mi_setting.AQUA)
	textrect=text.get_rect()
	textrect.centerx=DISPLAYSURF.get_rect().centerx
	textrect.centery=DISPLAYSURF.get_rect().centery
	DISPLAYSURF.fill(mi_setting.AQUA)
	DISPLAYSURF.blit(text,textrect)
	pygame.display.update()
	while True:
		for i in pygame.event.get():
			if i.type==QUIT:
				pygame.quit(b)
				sys.exit()
			elif i.type == pygame.KEYDOWN:
				if i.key == pygame.K_SPACE:
					return 0

Main_Impact()