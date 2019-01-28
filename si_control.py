import pygame,sys,random,time
from si_setting import Si_Setting
from pygame.locals import * 
from si_bullets import *
from si_alien import *
from backgrounds import *


def check_keypress(DISPLAYSURF,mi_setting,mi_ship,mi_bulletGroup,mi_alienGroup,BG_group):
	collisions = pygame.sprite.groupcollide(mi_bulletGroup,mi_alienGroup, True, True)
	if collisions:
		mi_setting.score+=1

	mi_setting.alien_delay=random.randint(1,10)
	mi_setting.alien_count=random.randint(1,50)

	if (mi_setting.alien_count-20) == mi_setting.alien_delay:
		new_bg=BG_Class(DISPLAYSURF,mi_setting)
		new_bg.rect.x=800
		new_bg.rect.y=random.randint(50,530)
		BG_group.add(new_bg)
 
	if pygame.sprite.spritecollideany(mi_ship,mi_alienGroup):
		DISPLAYSURF.blit(mi_ship.ship_blast,(mi_ship.rect.x-12,mi_ship.rect.y-3))
		pygame.display.update()
		pygame.time.wait(4000)
		game_over(DISPLAYSURF,mi_setting)

	for i in pygame.event.get():
		if i.type==QUIT:
			pygame.quit()
			sys.exit()
		elif i.type == pygame.KEYDOWN:
			if i.key == pygame.K_SPACE:
				if (len(mi_bulletGroup) <= 4):
					new_bullet=Bullets(DISPLAYSURF,mi_setting,mi_ship.rect.x,mi_ship.rect.y)
					mi_bulletGroup.add(new_bullet)

	if (mi_setting.alien_count) == mi_setting.alien_delay:
		new_alien=Alien1(DISPLAYSURF,mi_setting)
		if mi_setting.score == 5:
			new_alien2=Alien2(DISPLAYSURF,mi_setting)
			new_alien2.rect.x=700
			new_alien2.rect.y=50
			mi_alienGroup.add(new_alien2)
		new_alien.rect.x=800
		new_alien.rect.y=random.randint(50,530)
		mi_alienGroup.add(new_alien)

	DISPLAYSURF.fill(mi_setting.BLACK)

	for i in BG_group.sprites():
		i.draw_BG()

	DISPLAYSURF.blit(mi_ship.ship_img,(mi_ship.rect.x,mi_ship.rect.y))
	get_score(DISPLAYSURF,mi_setting)

	for i in mi_bulletGroup.sprites():
		i.draw_bullet()
		i.bullet_update()

	for i in mi_alienGroup.sprites():
		i.draw_alien()
		i.alien_update()

	for i in mi_bulletGroup.copy():
		if i.rect.x >= mi_setting.Disp_Width:
			mi_bulletGroup.remove(i)

	for i in mi_alienGroup.copy():
		if i.rect.y <= 0:
			mi_alienGroup.remove(i)

	for i in BG_group.copy():
		if i.rect.y <= 0:
			BG_group.remove(i)

	pressed_key=pygame.key.get_pressed()

	if pressed_key[pygame.K_LEFT] and mi_ship.rect.x>mi_ship.ship_xMIN:
		mi_ship.rect.x-=15
	elif pressed_key[pygame.K_RIGHT] and mi_ship.rect.x<mi_ship.ship_xMAX:
		mi_ship.rect.x+=15
	elif pressed_key[pygame.K_UP] and mi_ship.rect.y>mi_ship.ship_yMIN:
		mi_ship.rect.y-=15
	elif pressed_key[pygame.K_DOWN] and mi_ship.rect.y<mi_ship.ship_yMAX:
		mi_ship.rect.y+=15
	else:
		pass

def get_score(DISPLAYSURF,mi_setting):
	basicFont=pygame.font.SysFont(None,48)
	text=basicFont.render(str(mi_setting.score),True,mi_setting.AQUA,mi_setting.BLACK)
	textrect=text.get_rect()
	textrect.centerx=750
	textrect.centery=20
	DISPLAYSURF.blit(text,textrect)

def game_over(DISPLAYSURF,mi_setting):
	basicFont=pygame.font.SysFont(None,48)
	text=basicFont.render("YOUR SCORE : "+str(mi_setting.score),True,mi_setting.AQUA,mi_setting.BLACK)
	textrect=text.get_rect()
	textrect.centerx=DISPLAYSURF.get_rect().centerx
	textrect.centery=DISPLAYSURF.get_rect().centery
	DISPLAYSURF.fill(mi_setting.BLACK)
	DISPLAYSURF.blit(text,textrect)
	pygame.display.update()
	while True:
		for i in pygame.event.get():
			if i.type==QUIT:
				pygame.quit()
				sys.exit()