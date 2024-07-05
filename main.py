import pygame,sys
from config import *
from level import *
from player import *

pygame.init()

# değişkenler
ekran = pygame.display.set_mode((en, boy))
clock=pygame.time.Clock()
level=Level(level_map,ekran)
# elma
apple_img = pygame.image.load("f_g_i/apple.png").convert_alpha()
apple_img = pygame.transform.scale(apple_img, (16, 16))
# patates
patates_img = pygame.image.load("f_g_i/patates.png").convert_alpha()
patates_img = pygame.transform.scale(patates_img, (17, 12))
#soğan
soğan_img = pygame.image.load("f_g_i/soğan.png").convert_alpha()
soğan_img = pygame.transform.scale(soğan_img, (12, 16))
# yün
yün_img = pygame.image.load("f_g_i/yün.png").convert_alpha()
yün_img = pygame.transform.scale(yün_img, (18, 12))
#ekmek
ekmek_img = pygame.image.load("f_g_i/bread.png").convert_alpha()
ekmek_img = pygame.transform.scale(ekmek_img, (18, 9))
#iksir
iksir_img=pygame.image.load("f_g_i/can_iksiri.png").convert_alpha()
iksir_img=pygame.transform.scale(iksir_img, (12,19))
#energy_bar
energy_bar_img=pygame.image.load("f_g_i/energy_bar.png").convert_alpha()
energy_bar_img=pygame.transform.scale(energy_bar_img, (12,18))
sun=pygame.image.load("f_g_i/g_sun.png").convert_alpha()
sun=pygame.transform.scale(sun, (50,50))
moon=pygame.image.load("f_g_i/moon.png").convert_alpha()
moon=pygame.transform.scale(moon, (50,50))
para_yeri=pygame.image.load("f_g_i/para_yeri.png").convert_alpha()
para_yeri2=pygame.transform.scale(para_yeri, (100,35))
ekmek = pygame.sprite.Group()

ekmek_group = pygame.sprite.Group()
ekmek_sprite = pygame.sprite.Sprite()
ekmek_sprite.image = ekmek_img
ekmek_sprite.rect = ekmek_img.get_rect()
ekmek_group.add(ekmek_sprite) 
ekmek_sprite.image.set_colorkey((255, 255, 255))

iksir_group = pygame.sprite.Group()
iksir_sprite = pygame.sprite.Sprite()
iksir_sprite.image = iksir_img
iksir_sprite.rect = iksir_img.get_rect()
iksir_group.add(iksir_sprite) 

energy_bar_group = pygame.sprite.Group()
energy_bar_sprite = pygame.sprite.Sprite()
energy_bar_sprite.image = energy_bar_img
energy_bar_sprite.rect = energy_bar_img.get_rect()
energy_bar_group.add(energy_bar_sprite) 

apple_group = pygame.sprite.Group()
apple_sprite = pygame.sprite.Sprite()
apple_sprite.image = apple_img
apple_sprite.rect = apple_img.get_rect()
apple_group.add(apple_sprite) 
apple_sprite.image.set_colorkey((255, 255, 255))

patates_group = pygame.sprite.Group()
patates_sprite = pygame.sprite.Sprite()
patates_sprite.image = patates_img
patates_sprite.rect = patates_img.get_rect()
patates_group.add(patates_sprite) 

soğan_group = pygame.sprite.Group()
soğan_sprite = pygame.sprite.Sprite()
soğan_sprite.image = soğan_img
soğan_sprite.rect = soğan_img.get_rect()
soğan_group.add(soğan_sprite) 

yün_group = pygame.sprite.Group()
yün_sprite = pygame.sprite.Sprite()
yün_sprite.image = yün_img
yün_sprite.rect = yün_img.get_rect()
yün_group.add(yün_sprite) 

envanter = pygame.Rect(375, 496, 45, 45)
envanter2 = pygame.Rect(425, 496, 45, 45)
envanter_1_ekmek=0
envanter_1_iksir=0
envanter_1_energy_bar=0
envanter_2_ekmek=0
envanter_2_iksir=0
envanter_2_energy_bar=0

envanter3 = pygame.Rect(352, 563, 45, 45)
envanter4 = pygame.Rect(402, 563, 45, 45)
envanter5 = pygame.Rect(452, 563, 45, 45)

ekmek_yeri=0
iksir_yeri=0
energy_bar_yeri=0

while True:
  if level.day==15 and level.saat==6 and level.dakika>15:
    level.end_açıldı=0

  if level.butona_basıldı==0:
    level.story()
#------------Eşya satın alma---------------
  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and level.player_died_flag:
                level.player_died_flag = False
                level.reset_game()
#------------------------1_TUŞU--------------------
            elif event.key == pygame.K_1:  
              # --------ekmek--------
              if ekmek_yeri==1 and level.ekmek_sayısı>0:
                level.ekmek_sayısı-=1
                if level.ekmek_sayısı<=0:
                  level.ekmek=0
                level.hunger+=18
                if level.hunger>=150:
                  level.hunger=150  
              # ------iksir--------
              if iksir_yeri==1 and level.iksir_sayısı>0:
                level.iksir_sayısı-=1
                if level.iksir_sayısı<=0:
                  level.iksir=0
                level.health+=15

              # ------energy_bar---------
              if energy_bar_yeri==1 and level.energy_bar>0:
                level.energy_bar_sayısı-=1
                if level.energy_bar_sayısı<=0:
                  level.energy_bar=0
                level.strength+=13
                      
#------------------------2_TUŞU--------------------
            elif event.key == pygame.K_2:  
              # -----ekmek-----
              if ekmek_yeri==2 and level.ekmek_sayısı>0:
                level.ekmek_sayısı-=1
                if level.ekmek_sayısı<=0:
                  level.ekmek=0
                level.hunger+=18
              # ------iksir----
              if iksir_yeri==2 and level.iksir_sayısı>0:
                level.iksir_sayısı-=1
                if level.iksir_sayısı<=0:
                  level.iksir=0
                level.health+=15
              # ------energy_bar-----
              if energy_bar_yeri==2 and level.energy_bar_sayısı>0:
                level.energy_bar_sayısı-=1
                if level.energy_bar_sayısı<=0:
                  level.energy_bar=0
                level.strength+=13
                  
#------------------------3_TUŞU---------------------
            elif event.key == pygame.K_3:  
              # ------ekmek----
              if ekmek_yeri==3 and level.ekmek_sayısı>0:
                level.ekmek_sayısı-=1
                if level.ekmek_sayısı<=0:
                  level.ekmek=0
                level.hunger+=18
              # -----iksir-----
              if iksir_yeri==3 and level.iksir_sayısı>0:
                level.iksir_sayısı-=1
                if level.iksir_sayısı<=0:
                  level.iksir=0
                level.health+=15
              # -----energy_bar----
              if energy_bar_yeri==3 and level.energy_bar_sayısı>0:
                level.energy_bar_sayısı-=1
                if level.energy_bar_sayısı<=0:
                  level.energy_bar=0
                level.strength+=13

        elif event.type == pygame.MOUSEBUTTONDOWN:
          if event.button == 1:  # Left mouse button
            if level.story_açıldı==1:
              if level.draw_button7_rect.collidepoint(event.pos):
                level.butona_basıldı=1
                level.story_açıldı=0
          
            if level.ödeme_açıldı==1 and level.day==15:
              if level.draw_button8_rect.collidepoint(event.pos):
                level.money-=1500
                level.ödendi=1

            player = level.player.sprite
            if level.store_açıldı==1:

              if level.money>=18:
                if level.draw_button1_rect.collidepoint(event.pos) and level.money>=12:
                  level.ekmek=1
                  level.ekmek_sayısı+=1
                  level.money-=18
                  print("1")
             
              if level.money>=15:
                if level.draw_button2_rect.collidepoint(event.pos) and level.money>=15:
                  level.iksir=1
                  level.iksir_sayısı+=1
                  level.money-=15
                  print("2")

              if level.money>=15:
                if level.draw_button3_rect.collidepoint(event.pos) and level.money>=13:
                  level.energy_bar=1
                  level.energy_bar_sayısı+=1 
                  level.money-=15
                  print("3")

            # -------------SATIŞ-------------
            if level.sales_açıldı==1:
                # ------elma_sat----------
                if level.draw_button4_rect.collidepoint(event.pos) and level.apple_sayısı>0:
                  level.apple_sayısı-=1
                  level.money+=12
                  print("4")
                # ------patates_sat----------  
                if level.draw_button5_rect.collidepoint(event.pos) and level.patates_sayısı>0:
                  level.patates_sayısı-=1
                  level.money+=13
                  print("5")
                # ------soğan_sat----------
                if level.draw_button6_rect.collidepoint(event.pos) and level.soğan_sayısı>0:
                  level.soğan_sayısı-=1 
                  level.money+=13
                  print("6")
                # ------yün_sat----------
                if level.draw_button9_rect.collidepoint(event.pos) and level.yün_sayısı>0:
                  level.yün_sayısı-=1 
                  level.money+=15
                  print("9")
                  
  if level.yün_sayısı<=0:
    level.yün=0

  if level.butona_basıldı==1 and level.game_over==0:
    if level.hunger>=150:
      level.hunger=150
    if level.strength>=150:
      level.strength=150
    if level.health>=150:
      level.health=150

    ekran.fill((103, 145,23))
    level.run()
    font = pygame.font.Font(None, 16)
    font2 = pygame.font.Font("f_g_i/SHPinscher-Regular.otf", 30)
    font3 = pygame.font.Font("f_g_i/SHPinscher-Regular.otf", 16)
    pygame.draw.rect(ekran, (255, 255, 255), (27, 15, 156, 21))
    pygame.draw.rect(ekran, (255, 255, 255), (27, 40, 156, 21))
    pygame.draw.rect(ekran, (255, 255, 255), (27, 64, 156, 21))  
    pygame.draw.rect(ekran, (255, 255, 255), (228, 465, 452, 14))
    pygame.draw.rect(ekran, (4, 117, 4), (230, 467, 448, 10))
    level.draw_health_bar(ekran)
    text = font2.render(f"Level:{level.level}", True, (0, 0, 0))
    ekran.blit(text, (410, 430))
    text_money = font2.render(f"{level.money}", True, (0, 0, 0))
    ekran.blit(para_yeri, (29, 90))  
    ekran.blit(text_money, (80, 89))
    text_day = font2.render(f"Day:{level.day}", True, (0, 0, 0))
    ekran.blit(text_day, (826, 50))
    if level.saat<10 and level.dakika<10:
      text = font2.render(f"0{level.saat}:0{level.dakika}", True, (0,0,0))
      text_rect = text.get_rect(center=(852, 100)) 
      ekran.blit(text, text_rect)
      
    if level.saat>=10 and level.dakika<10:
      text = font2.render(f"{level.saat}:0{level.dakika}", True, (0,0,0))
      text_rect = text.get_rect(center=(852, 100))
      ekran.blit(text, text_rect)

    if level.saat<10 and level.dakika>=10:
      text = font2.render(f"0{level.saat}:{level.dakika}", True, (0,0,0))
      text_rect = text.get_rect(center=(852, 100))
      ekran.blit(text, text_rect)
      
    if level.saat>=10 and level.dakika>=10:
      text = font2.render(f"{level.saat}:{level.dakika}", True, (0,0,0))
      text_rect = text.get_rect(center=(852, 100))
      ekran.blit(text, text_rect)

    if level.saat>=6 and level.saat<18:
      ekran.blit(sun, (826, 5))

    if level.saat>=18 or level.saat<6:
      ekran.blit(moon, (826, 5))

    pygame.draw.rect(ekran, (148,107,41), (369, 490, 157, 57))
    pygame.draw.rect(ekran, "gray", envanter)
    pygame.draw.rect(ekran, "gray", envanter2)
    pygame.draw.rect(ekran, "gray", (475, 496, 45, 45))

    pygame.draw.rect(ekran, (148,107,41), (346, 557, 206, 57))
    pygame.draw.rect(ekran, "gray", envanter3)
    pygame.draw.rect(ekran, "gray", envanter4)
    pygame.draw.rect(ekran, "gray", envanter5)
    pygame.draw.rect(ekran, "gray", (502, 563, 45, 45))

#---------------------ENVANTER_1_TEMASI-----------------------
    for ekmek_sprite in ekmek_group.sprites():
      if ekmek_sprite.rect.colliderect(envanter):
        envanter_1_ekmek=1

    for iksir_sprite in iksir_group.sprites():
      if iksir_sprite.rect.colliderect(envanter):
         envanter_1_iksir=1

    for energy_bar_sprite in energy_bar_group.sprites():
      if energy_bar_sprite.rect.colliderect(envanter):
         envanter_1_energy_bar=1
  
#---------------------ENVANTER_2_TEMASI-----------------------
    for ekmek_sprite in ekmek_group.sprites():
      if ekmek_sprite.rect.colliderect(envanter2):
        envanter_2_ekmek=1

    for iksir_sprite in iksir_group.sprites():
      if iksir_sprite.rect.colliderect(envanter2):
         envanter_2_iksir=1

    for energy_bar_sprite in energy_bar_group.sprites():
      if energy_bar_sprite.rect.colliderect(envanter2):
         envanter_2_energy_bar=1
  
#---------------------EKMEK-------------------------
    text = font3.render(f"{level.ekmek_sayısı}x", True, (0, 0, 0))
    if level.ekmek==1 and envanter_1_iksir==0 and envanter_1_energy_bar==0:
      ekmek_sprite.rect.topleft = (387, 510)  
      ekran.blit(ekmek_sprite.image, ekmek_sprite.rect.topleft)
      ekran.blit(text, (405, 524))
      ekmek_yeri=1
  
    if level.ekmek==1 and envanter_1_iksir==1 and envanter_2_energy_bar==0:
      ekmek_sprite.rect.topleft = (440, 510)  
      ekran.blit(ekmek_sprite.image, ekmek_sprite.rect.topleft)
      ekran.blit(text, (454, 524))
      ekmek_yeri=2
  
    if level.ekmek==1 and envanter_1_energy_bar==1 and envanter_2_iksir==0:
      ekmek_sprite.rect.topleft = (440, 510)  
      ekran.blit(ekmek_sprite.image, ekmek_sprite.rect.topleft)
      ekran.blit(text, (454, 524))
      ekmek_yeri=2
  
    if level.ekmek==1 and envanter_1_iksir==1 and envanter_2_energy_bar==1 or level.ekmek==1 and envanter_2_iksir==1 and envanter_1_energy_bar==1:
      ekmek_sprite.rect.topleft = (490, 510)  
      ekran.blit(ekmek_sprite.image, ekmek_sprite.rect.topleft)
      ekran.blit(text, (504, 524))
      ekmek_yeri=3
      
#---------------------İKSİR-------------------------
    text2 = font3.render(f"{level.iksir_sayısı}x", True, (0, 0, 0))
    if level.iksir==1 and envanter_1_ekmek==0 and envanter_1_energy_bar==0:
      iksir_sprite.rect.topleft = (389, 510)  
      ekran.blit(iksir_sprite.image, iksir_sprite.rect.topleft)
      ekran.blit(text2, (405, 524))
      iksir_yeri=1
  
    if level.iksir==1 and envanter_1_ekmek==1 and envanter_2_energy_bar==0:
      iksir_sprite.rect.topleft = (442, 510)  
      ekran.blit(iksir_sprite.image, iksir_sprite.rect.topleft)
      ekran.blit(text2, (454, 524))
      iksir_yeri=2
  
    if level.iksir==1 and envanter_1_energy_bar==1 and envanter_2_ekmek==0:
      iksir_sprite.rect.topleft = (442, 510)  
      ekran.blit(iksir_sprite.image, iksir_sprite.rect.topleft)
      ekran.blit(text2, (454, 524))
      iksir_yeri=2
  
    if level.iksir==1 and envanter_1_ekmek==1 and envanter_2_energy_bar==1 or level.iksir==1 and envanter_2_ekmek==1 and envanter_1_energy_bar==1:
      iksir_sprite.rect.topleft = (492, 510)  
      ekran.blit(iksir_sprite.image, iksir_sprite.rect.topleft)
      ekran.blit(text2, (504, 524))
      iksir_yeri=3
      
#-----------------------ENERGY_BAR-------------------
    text3 = font3.render(f"{level.energy_bar_sayısı}x", True, (0, 0, 0))
    if level.energy_bar==1 and envanter_1_iksir==0 and envanter_1_ekmek==0:
      energy_bar_sprite.rect.topleft = (389, 508)  
      ekran.blit(energy_bar_sprite.image, energy_bar_sprite.rect.topleft)
      ekran.blit(text3, (405, 524))
      energy_bar_yeri=1
  
    if level.energy_bar==1 and envanter_1_iksir==1 and envanter_2_ekmek==0:
      energy_bar_sprite.rect.topleft = (442, 508)  
      ekran.blit(energy_bar_sprite.image, energy_bar_sprite.rect.topleft)
      ekran.blit(text3, (454, 524))
      energy_bar_yeri=2
  
    if level.energy_bar==1 and envanter_1_ekmek==1 and envanter_2_iksir==0:
      energy_bar_sprite.rect.topleft = (442, 508)  
      ekran.blit(energy_bar_sprite.image, energy_bar_sprite.rect.topleft)
      ekran.blit(text3, (454, 524))
      energy_bar_yeri=2
  
    if level.energy_bar==1 and envanter_1_ekmek==1 and envanter_2_iksir==1 or level.energy_bar==1 and envanter_2_ekmek==1 and envanter_1_iksir==1:
      energy_bar_sprite.rect.topleft = (492, 508)  
      ekran.blit(energy_bar_sprite.image, energy_bar_sprite.rect.topleft)
      ekran.blit(text3, (504, 524))
      energy_bar_yeri=3
  
   # ----ELMA--------
    texte = font3.render(f"{level.apple_sayısı}x", True, (0, 0, 0))
    if level.apple==1:
      apple_sprite.rect.topleft = (364, 576)  
      ekran.blit(apple_sprite.image, apple_sprite.rect.topleft)
      ekran.blit(texte, (382, 588))
      if level.apple_sayısı<=0:
        level.apple=0
    # ------PATATES-------
    textp = font3.render(f"{level.patates_sayısı}x", True, (0, 0, 0))
    if level.patates==1:
      patates_sprite.rect.topleft = (418, 576)  
      ekran.blit(patates_sprite.image, patates_sprite.rect.topleft)
      ekran.blit(textp, (432, 588))
    # -------SOĞAN-----
    texts = font3.render(f"{level.soğan_sayısı}x", True, (0, 0, 0))
    if level.soğan==1:
      soğan_sprite.rect.topleft = (469, 576)  
      ekran.blit(soğan_sprite.image, soğan_sprite.rect.topleft)
      ekran.blit(texts, (481, 588))
    # ------YÜN-------
    texty = font3.render(f"{level.yün_sayısı}x", True, (0, 0, 0))
    if level.yün==1:
      yün_sprite.rect.topleft = (516, 578)  
      ekran.blit(yün_sprite.image, yün_sprite.rect.topleft)
      ekran.blit(texty, (532, 588))

    if level.npc_hit2 and level.day==14:
      level.stalin_walk()
  
    if level.ödendi==1:
      level.end_süre+=1
      if level.money>=0 and level.end_süre<=100:
         level.end()
      if level.money<0:
         level.end2()

    if level.died_end_açıldı==1:
      level.died_end()

    if level.health<=0:
      level.health=0
      level.died_end2()

    if level.sheep_süre_artışı==1:
      level.sheep_süre+=1

    pygame.display.update()
    clock.tick(90)