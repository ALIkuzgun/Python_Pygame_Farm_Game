import pygame, random
from animals import *
from config import *
from enemy import *
from npc import *
from player import *
from tiles import *

level_width = 900 
level_height = 640 

class Level(pygame.sprite.Sprite):
  def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)
        # değişkenler
        self.player_died_flag = False
        self.butona_basıldı=0
        self.kararma_derecesi=2
        self.died_end_açıldı=0
        self.sheep_teması=0
        self.askerle_konuşuldu=0
        self.level=0
        self.sd, self.pd=0,0
        self.story_açıldı=0
        self.x=0
        self.temas=0
        self.ekran_kaydır=1
        self.enemy_temas=0
        self.tree_png_timer = pygame.time.get_ticks()  
        self.tree_png_delay = 100000
        self.apple, self.apple_sayısı=1,2
        self.patates, self.patates_sayısı=1,5
        self.soğan, self.soğan_sayısı=1,5
        self.yün, self.yün_sayısı=1,1
        self.ekmek, self.ekmek_sayısı=0,0
        self.iksir, self.iksir_sayısı=0,0
        self.energy_bar, self.energy_bar_sayısı= 0,0
        self.tree_apple=0
        self.npc_hit=0
        self.npc_hit2=0
        self.money=100
        self.topla_apple=0
        self.store_açıldı,self.sales_açıldı,self.end_açıldı=0,0,0
        self.çapalanmış=1
        self.world_shift = 0
        self.süre=0
        self.end_süre=0
        self.game_over=0
        self.geçiş_temas=0
        self.stalin_süre=0
        self.staline_temas_edildi=0
        self.stalin_died=0
        self.sheep_süre=0
        self.sheep_süre_artışı=0
        self.ödeme_açıldı=0
        self.ödendi=0

        # butonlar
        self.draw_button1_rect = pygame.Rect(253, 189, 20, 18) # ekmek
        self.draw_button2_rect = pygame.Rect(253, 237, 20, 18) # iksir
        self.draw_button3_rect = pygame.Rect(253, 284, 20, 18) # energy_bar
        self.draw_button4_rect = pygame.Rect(209, 190, 20, 18) # elma
        self.draw_button5_rect = pygame.Rect(209, 226, 20, 18) # patates
        self.draw_button6_rect = pygame.Rect(209, 268, 20, 18) # soğan
        self.draw_button9_rect = pygame.Rect(209, 306, 20, 18) # syün
        self.draw_button7_rect = pygame.Rect(820, 590, 30, 22) # skip
        self.draw_button8_rect = pygame.Rect(178, 175, 30, 22) # ödeme

        # barlar
        self.health = 150
        self.max_health = 150  
        self.health_bar_width = 150
        self.health_bar_height = 15
        self.health_bar_color = (0, 255, 0)

        self.strength = 150
        self.max_strength = 150  
        self.strength_bar_width = 150
        self.strength_bar_height = 15
        self.strength_bar_color = (0, 0, 255)

        self.hunger = 150
        self.max_hunger = 150  
        self.hunger_bar_width = 150
        self.hunger_bar_height = 15
        self.hunger_bar_color = (255, 0, 0)

        self.level = 1
        self.level_xp = 0
        self.max_level = 150  
        self.level_bar_width = 450
        self.level_bar_height = 10
        self.level_bar_color = (255, 255, 0)

        self.strength_decrease_timer = pygame.time.get_ticks()  
        self.hunger_decrease_timer = pygame.time.get_ticks()  
        self.strength_decrease_delay = 10000
        self.hunger_decrease_delay = 10000

        # zaman değişkenleri
        self.day=1
        self.saat=6
        self.dakika=0
        self.last_minute_check = pygame.time.get_ticks() 
        self.minute_duration = 10

        # ekran kararması değişkenleri
        self.full_surf=pygame.Surface((level_width,level_height))
        self.start_color=[255,255,255]
        self.end_color=(38,101,189)
# ekran kararması
  def display(self,dt):
    if self.saat == 8:  
        self.start_color = [255, 255, 255]  
    else:
        for index, value in enumerate(self.end_color):
            if self.start_color[index] > value:
                self.start_color[index] -= self.kararma_derecesi * dt
    self.full_surf.fill(self.start_color)
    self.display_surface.blit(self.full_surf, (0, 0), special_flags=pygame.BLEND_RGB_MULT)
# barlar
  def draw_health_bar(self, surface):
        health_bar_rect = pygame.Rect(30, 18, self.health_bar_width, self.health_bar_height)
        pygame.draw.rect(surface, (255, 0, 0), health_bar_rect)
    
        strength_bar_rect = pygame.Rect(30 , 43, self.strength_bar_width, self.strength_bar_height)
        pygame.draw.rect(surface, (219, 211, 44), strength_bar_rect)

        hunger_bar_rect = pygame.Rect(30 , 67, self.hunger_bar_width, self.hunger_bar_height)
        pygame.draw.rect(surface, (141, 85, 36), hunger_bar_rect)

        level_bar_rect = pygame.Rect(230 , 467, self.level_bar_width, self.level_bar_height)
        pygame.draw.rect(surface, (10, 204, 10), level_bar_rect)
  
  def update_health_bar(self):
        strength_percentage = max(0, self.health) / self.max_health
        self.health_bar_width = int(strength_percentage * 150)

  def update_strength_bar(self):
        strength_percentage = max(0, self.strength) / self.max_strength
        self.strength_bar_width = int(strength_percentage * 150)

  def update_hunger_bar(self):
        hunger_percentage = max(0, self.hunger) / self.max_hunger
        self.hunger_bar_width = int(hunger_percentage * 150)

  def update_level_bar(self):
        hunger_percentage = max(0, self.level_xp) / self.max_level
        self.level_bar_width = int(hunger_percentage * 450)
# konum tanımlama 
  def setup_level(self,layout):
        player_created = False
        self.tiles = pygame.sprite.Group()
        self.tiles2 = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.slime = pygame.sprite.Group()
        self.map = pygame.sprite.Group()
        self.sheeps = pygame.sprite.Group()
        self.goblin = pygame.sprite.Group()
        self.lama = pygame.sprite.Group()
        self.xp = pygame.sprite.Group()
        self.geçiş = pygame.sprite.Group()
        self.sınır = pygame.sprite.Group()
        self.tree = pygame.sprite.Group()
        self.çit1 = pygame.sprite.Group()
        self.çit2 = pygame.sprite.Group()
        self.çit3 = pygame.sprite.Group()
        self.çit4 = pygame.sprite.Group()
        self.npc = pygame.sprite.Group()
        self.npc2 = pygame.sprite.Group()
        self.npc_asker = pygame.sprite.Group()
        self.npc_cüce = pygame.sprite.Group()
        self.farm = pygame.sprite.Group()
        self.bed = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites2 = pygame.sprite.Group()
        self.duvar = pygame.sprite.Group()
        self.water = pygame.sprite.Group()
        self.animals = pygame.sprite.Group()
        self.wall_tree = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == "X":
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                    self.all_sprites2.add(tile) 
                    self.duvar.add(tile) 
                elif cell == "W":
                    water = Water((x, y), tile_size)
                    self.water.add(water)
                    self.all_sprites2.add(water)
                elif cell == "x":
                    tile2 = Tile2((x, y+16), tile_size)
                    self.tiles2.add(tile2)
                    self.all_sprites2.add(tile2) 
                elif cell == "G":
                    geçiş = Geçiş((x, y), tile_size)
                    self.geçiş.add(geçiş)
                    self.all_sprites2.add(geçiş)
                elif cell == "S":     
                    sheep = Sheep((x, y), tile_size)
                    self.sheeps.add(sheep)
                    self.all_sprites.add(sheep) 
                    self.animals.add(sheep) 
                elif cell == "L":     
                    lama = Lama((x, y), tile_size)
                    self.lama.add(lama)
                    self.all_sprites.add(lama)
                    self.animals.add(lama)  
                elif cell == "F":     
                    farm = Farm((x, y), tile_size)
                    self.farm.add(farm)
                    self.all_sprites.add(farm) 
                elif cell == "1":
                    map = Map((x, y), tile_size)
                    self.map.add(map)
                    self.all_sprites.add(map) 
                elif cell == "E":  
                    slime = Slime((x, y), tile_size)
                    self.slime.add(slime) 
                    self.all_sprites.add(slime) 
                    self.enemies.add(slime)
                elif cell == "Ğ":  
                    goblin = Goblin((x, y), tile_size)
                    self.goblin.add(goblin) 
                    self.all_sprites.add(goblin) 
                    self.enemies.add(goblin)
                elif cell == "T":
                    tree = Tree((x, y), tile_size)
                    self.tree.add(tree)
                    self.all_sprites.add(tree)                 
                elif cell == "@":
                    sınır = Sınır((x, y), tile_size)
                    self.sınır.add(sınır)
                    self.all_sprites2.add(sınır) 
                elif cell == "Ç":
                    çit1 = Çit1((x, y), tile_size+16)
                    self.çit1.add(çit1)
                    self.all_sprites2.add(çit1) 
                    self.duvar.add(çit1) 
                elif cell == "ç":
                    çit2 = Çit1((x+16, y), tile_size)
                    self.çit1.add(çit2)
                    self.all_sprites2.add(çit2) 
                    self.duvar.add(çit2) 
                elif cell == "C":
                    çit3 = Çit2((x, y), tile_size)
                    self.çit3.add(çit3)
                    self.all_sprites2.add(çit3) 
                    self.duvar.add(çit3) 
                elif cell == "c":
                    çit4 = Çit2((x, y+16), tile_size)
                    self.çit4.add(çit4)
                    self.all_sprites2.add(çit4)
                    self.duvar.add(çit4) 
                elif cell == "N":
                    npc = Npc((x, y), tile_size)
                    self.npc.add(npc)
                    self.all_sprites.add(npc) 
                elif cell == "n":
                    npc2 = Npc_satış((x, y), tile_size)
                    self.npc2.add(npc2)
                    self.all_sprites.add(npc2) 
                elif cell == "A":
                    npc_asker = Npc_asker((x, y), tile_size)
                    self.npc_asker.add(npc_asker)
                    self.all_sprites.add(npc_asker) 
                elif cell == "B":
                    bed = Bed((x, y), tile_size)
                    self.bed.add(bed)
                    self.all_sprites2.add(bed) 
                elif cell == "P" and not player_created:  
                  player_sprite = Player((x, y))
                  self.player.add(player_sprite)
                  self.all_sprites.add(player_sprite) 
                  player_created = True                   
# temaslar
  def collision(self):
    player=self.player.sprite
    player.rect.x+=player.direction.x*player.speed

    if self.hunger>=150:
        self.hunger=150

    if self.hunger<=0:
        self.hunger=0
    if self.strength<=0:
        self.strength=0
    if self.health<=0:
        self.health=0
        self.died_end2()

    hitss = pygame.sprite.spritecollide(player, self.sınır, False)
    if hitss:
       self.died_end()
       self.died_end_açıldı=1

    hitst = pygame.sprite.spritecollide(player, self.duvar, False)
    hitst2 = pygame.sprite.spritecollide(player, self.geçiş, False)
    if hitst:
        self.temas=1
        print("1")
    else:
         self.temas=0

    if self.day!=15:
      if hitst2:
        self.geçiş_temas=1
        print("11")
      else:
         self.geçiş_temas=0
         
    for enemy in self.enemies.sprites():
        hitst_enemy = pygame.sprite.spritecollide(enemy, self.duvar, False)
        hitst_enemy2 = pygame.sprite.spritecollide(enemy, self.tiles2, False)
        if hitst_enemy or hitst_enemy2:
          if enemy.move_direction=="left":
            enemy.move_direction="right"
                    
          elif enemy.move_direction=="right":  
            enemy.move_direction="left"

          elif enemy.move_direction=="up":
            enemy.move_direction="down"

          elif enemy.move_direction=="down":
            enemy.move_direction="up"

    for lama in self.lama.sprites():
        hitst_lama = pygame.sprite.spritecollide(lama, self.duvar, False)
        if hitst_lama:
          if lama.yön=="left":
            lama.yön="right"
                    
          elif lama.yön=="right":  
            lama.yön="left"

          elif lama.yön=="up":
            lama.yön="down"

          elif lama.yön=="down":
            lama.yön="up"

    for sheep in self.sheeps.sprites():
        hitst_sheep = pygame.sprite.spritecollide(sheep, self.duvar, False)
        hitst_sheep2 = pygame.sprite.spritecollide(sheep, self.tiles2, False)
        if hitst_sheep or hitst_sheep2:
          if sheep.yön=="left":
            sheep.yön="right"
                    
          elif sheep.yön=="right":  
            sheep.yön="left"

          elif sheep.yön=="up":
            sheep.yön="down"

          elif sheep.yön=="down":
            sheep.yön="up"

    for waters in self.water.sprites():
      if player.rect.colliderect(waters.rect):
            if player.right==1:
              player.image = pygame.image.load("f_g_i/cs.png").convert_alpha()
              player.image = pygame.transform.scale(player.image, (22,30)) 
 
            if player.left==1:
              player.image = pygame.image.load("f_g_i/cs2.png").convert_alpha()
              player.image = pygame.transform.scale(player.image, (22,30)) 

    for sprite in self.duvar.sprites():
      if sprite.rect.colliderect(player.rect):
          if player.direction.x>0:
            player.rect.right=sprite.rect.left
          elif player.direction.x<0:
            player.rect.left=sprite.rect.right

    if self.day!=15 and self.askerle_konuşuldu==0:
      for sprite in self.geçiş.sprites():
        if sprite.rect.colliderect(player.rect):
          if player.direction.x>0:
            player.rect.right=sprite.rect.left
          elif player.direction.x<0:
            player.rect.left=sprite.rect.right

    hitse = pygame.sprite.spritecollide(player, self.slime, False)
    if hitse:
      self.health-=0.4
      if player.attack==1:
        for slime in hitse:
          slime.health -= 1
          if slime.health <= 0:
            slime.kill() 
            self.level_xp+=55

    hitsg = pygame.sprite.spritecollide(player, self.goblin, False)
    if hitsg:
      self.enemy_temas=1
      for goblin in hitsg:
          self.health-=0.6
          if player.attack==1:
            goblin.health -= 1.5
            if goblin.health <= 0:
              goblin.kill() 
              self.level_xp+=75
    else:
       self.enemy_temas=0

    hits5 = pygame.sprite.spritecollide(player, self.npc, False)
    if hits5:
      for npc in hits5:
        self.store()
        self.store_açıldı=1
        self.npc_hit=1

    else:
      self.npc_hit=0
      self.store_açıldı=0

    hitsnpc2 = pygame.sprite.spritecollide(player, self.npc2, False)
    if hitsnpc2:
      for npc2 in hitsnpc2:
        self.sales()
        self.sales_açıldı=1
        self.npc_hit2=1
        if self.day==14:
           self.stalin_walk()
           self.staline_temas_edildi=1
    else:
      self.npc_hit2=0
      self.sales_açıldı=0

    for npc2 in self.npc2:
           if self.stalin_died==1:
              npc2.kill()

    if self.staline_temas_edildi==1:
       self.stalin_süre+=1
       if self.stalin_süre>=10000:
          self.stalin_died=1

    hitsa = pygame.sprite.spritecollide(player, self.npc_asker, False)
    for npc_asker in hitsa:
      if hitsa:
       self.ödeme_açıldı=1
       self.ödeme()
       self.askerle_konuşuldu=1
       if self.ödendi==1:
          npc_asker.kill()

    hitst_sheep3 = pygame.sprite.spritecollide(player, self.sheeps, False)
    if hitst_sheep3 and player.x == 1:
        for sheep in hitst_sheep3:
            if sheep.type == "normal":
                self.yün_sayısı += random.choice([4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1])
                sheep.image = pygame.image.load("f_g_i/sheep3.png").convert_alpha()
                sheep.image = pygame.transform.scale(sheep.image, (24, 20))
                sheep.type = "kırkıldı"
                self.sheep_süre_artışı = 1

    if self.sheep_süre_artışı:
        self.sheep_süre += 1
        if self.sheep_süre >= 550:
            for sheep in self.sheeps:
                if sheep.type == "kırkıldı":
                    sheep.type = "normal"
                    sheep.image = pygame.image.load("f_g_i/sheep.png").convert_alpha()
                    sheep.image = pygame.transform.scale(sheep.image, (32, 32))
            self.sheep_süre = 0
            self.sheep_süre_artışı = 0

    hits8 = pygame.sprite.spritecollide(player, self.animals, False)
    if hits8 and player.attack==1 and player.kılıç==1:
      for sheep in hits8:
        sheep.health -= 1
        if sheep.health <= 0:
            self.level_xp+=30
            sheep.kill() 

    hitsf = pygame.sprite.spritecollide(player, self.farm, False)
    if hitsf:
      for farm in hitsf:
        if player.çapa==1 and farm.type!="g_farm_onion5" and farm.type!="g_farm_patates" and farm.soğan_type!="1" and farm.patates_type!="1":
            farm.image = pygame.image.load("f_g_i/g_farm.png").convert_alpha()
            farm.image = pygame.transform.scale(farm.image, (32,32)) 
            farm.çapalanmış=1
            farm.type="g_farm"
        if farm.çapalanmış == 1 and farm.type=="g_farm":
          if self.soğan == 1 and player.o == 1 and farm.state != "patates" and self.soğan_sayısı>=1:  
            self.soğan_sayısı-=1
            farm.image = pygame.image.load("f_g_i/g_farm_onion3.png").convert_alpha()
            farm.image = pygame.transform.scale(farm.image, (32,32)) 
            farm.state = "soğan"  
            farm.type = "g_farm_onion3"
            farm.soğan_type = "1" 
            self.sd=1
          elif self.patates == 1 and player.p == 1 and farm.state != "soğan" and self.patates_sayısı>=1:  
            self.patates_sayısı-=1
            farm.image = pygame.image.load("f_g_i/g_farm_patatesb.png").convert_alpha()
            farm.image = pygame.transform.scale(farm.image, (32,32)) 
            farm.state = "patates"
            farm.type="g_farm_patatesb"
            farm.patates_type="1"
            self.pd=1
        if farm.type=="g_farm_patates" and farm.type!="g_farm" and player.topla==1:
          farm.image = pygame.image.load("f_g_i/g_farm.png").convert_alpha()
          farm.image = pygame.transform.scale(farm.image, (32,32)) 
          self.patates_sayısı+=random.choice([2,1,1,2,3,1,1,1,4,1,2,1,2,1,2,3,1,1,1,1,1])
          farm.type="g_farm"
        if farm.type=="g_farm":
             farm.state=None
        if farm.type=="g_farm_onion5" and farm.type!="g_farm" and player.topla==1:
          farm.image = pygame.image.load("f_g_i/g_farm.png").convert_alpha()
          farm.image = pygame.transform.scale(farm.image, (32,32)) 
          self.soğan_sayısı+=random.choice([2,1,1,3,1,1,1,1,1,1,1,4,1,1,1,3,2,2,1,1])
          farm.type="g_farm"
    
    for farm in self.farm:
      if farm.çapalanmış == 1 and farm.type=="g_farm_onion3":
        if farm.state != "patates" and self.sd==1:  
          if self.saat==1:
            farm.image = pygame.image.load("f_g_i/g_farm_onion5.png").convert_alpha()
            farm.image = pygame.transform.scale(farm.image, (32,32)) 
            farm.type="g_farm_onion5"
            farm.soğan_type = "2"
      if farm.çapalanmış == 1 and farm.type=="g_farm_patatesb":
        if farm.state != "soğan" and self.pd==1:  
          if self.saat==1:
            farm.image = pygame.image.load("f_g_i/g_farm_patates.png").convert_alpha()
            farm.image = pygame.transform.scale(farm.image, (32,32)) 
            farm.type="g_farm_patates"
            farm.patates_zaman = 0
            farm.patates_type = "2"

    if self.soğan_sayısı==0:
      self.soğan=0
    if self.patates_sayısı==0:
       self.patates=0
    if self.patates_sayısı>0:
       self.patates=1
    if self.soğan_sayısı>0:
      self.soğan=1

    hits3 = pygame.sprite.spritecollide(player, self.tree, False)
    if hits3:
      self.topla_apple=1
      if player.c==1:
        for tree in self.tree:
          if tree.type == "ağaç":
            self.tree_apple = 1
          elif tree.type == "ağaç2":
             self.tree_apple = 0
          if self.tree_apple == 1:
            self.apple = 1
            self.apple_sayısı += random.choice([1, 3, 2, 4, 1, 1, 1, 1, 1, 1])
            tree.image = pygame.image.load("f_g_i/ağaç2.png").convert_alpha()
            tree.image = pygame.transform.scale(tree.image, (65, 70))
            tree.type = "ağaç2"
    else:
      self.topla=0
            
    for tree in self.tree:
      current_time2 = pygame.time.get_ticks()
      if current_time2 - self.tree_png_timer >= self.tree_png_delay:
        tree.type = "ağaç"
        tree.image = pygame.image.load("f_g_i/ağaç.png").convert_alpha()
        tree.image = pygame.transform.scale(tree.image, (65,70)) 
        self.tree_png_timer = current_time2

    hitsb = pygame.sprite.spritecollide(player, self.bed, False)
    if hitsb:
      for bed in hitsb:
        if self.saat==22 or self.saat==23 or self.saat==1 or self.saat==2 or self.saat==3 or self.saat==4 or self.saat==0 or self.saat==5:
          self.süre += 50 
          self.player.sprite.rect.x = bed.rect.x+20
          self.player.sprite.rect.y = bed.rect.y+14
          self.player.sprite.can_move = False
          self.strength=150
          self.ekran_kaydır=1
          
        if self.saat==6:
          self.süre+=0.5
          self.player.sprite.can_move = True
          self.ekran_kaydır=0
    else:
      self.süre += 0.5
      self.ekran_kaydır=0
    
    if self.ödendi==1:
      self.end_süre+=1
      if self.money>=0 and self.end_süre<=100:
         self.end()
      if self.money<0:
         self.end2()

  def collision_y(self):
    player=self.player.sprite
    player.rect.y += player.direction.y * player.speed
    
    for duvars in self.duvar.sprites():
      if player.rect.colliderect(duvars.rect):
        if player.direction.y > 0:
            player.is_jumping = False
            player.rect.bottom = duvars.rect.top
            player.direction.y = 0
        elif player.direction.y < 0:
            player.rect.top = duvars.rect.bottom
            player.direction.y = 0

    if self.day!=15 and self.askerle_konuşuldu==0:
      for geçiş in self.geçiş.sprites():
        if player.rect.colliderect(geçiş.rect):
          if player.direction.y > 0:
            player.is_jumping = False
            player.rect.bottom = geçiş.rect.top
            player.direction.y = 0
          elif player.direction.y < 0:
            player.rect.top = geçiş.rect.bottom
            player.direction.y = 0

    current_time = pygame.time.get_ticks()
    if current_time - self.strength_decrease_timer >= self.strength_decrease_delay:
            self.strength -= 4
            self.hunger -= 5
            self.strength_decrease_timer = current_time
# alım_satım
  def sales(self):
    s=pygame.image.load("f_g_i/sales.png").convert_alpha()
    s=pygame.transform.scale(s, (160,200))
    s_rect = s.get_rect(center=(200, 240))
    self.display_surface.blit(s, s_rect)
    
    button_rect = pygame.Rect(209, 266, 30, 22) #soğan
    pygame.draw.rect(self.display_surface, (0, 0, 0), button_rect) 
    font = pygame.font.Font("f_g_i/SHPinscher-Regular.otf", 24)
    text_surface = font.render("Sell", True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=button_rect.center)
    self.display_surface.blit(text_surface, text_rect)

    button_rect2 = pygame.Rect(209, 226, 30, 22) #patates
    pygame.draw.rect(self.display_surface, (0, 0, 0), button_rect2) 
    text_surface2 = font.render("Sell", True, (255, 255, 255))
    text_rect2 = text_surface2.get_rect(center=button_rect2.center)
    self.display_surface.blit(text_surface2, text_rect2)
  
    button_rect3 = pygame.Rect(209, 190, 30, 20) #elma
    pygame.draw.rect(self.display_surface, (0, 0, 0), button_rect3) 
    text_surface3 = font.render("Sell", True, (255, 255, 255))
    text_rect3 = text_surface3.get_rect(center=button_rect3.center)
    self.display_surface.blit(text_surface3, text_rect3)

    button_rect4 = pygame.Rect(209, 306, 30, 20) #elma
    pygame.draw.rect(self.display_surface, (0, 0, 0), button_rect4) 
    text_surface4 = font.render("Sell", True, (255, 255, 255))
    text_rect4 = text_surface4.get_rect(center=button_rect4.center)
    self.display_surface.blit(text_surface4, text_rect4)
# mağaza 
  def store(self):
    s=pygame.image.load("f_g_i/store.png").convert_alpha()
    s=pygame.transform.scale(s, (160,200))
    s_rect = s.get_rect(center=(200, 240))
    self.display_surface.blit(s, s_rect)
  
    font = pygame.font.Font("f_g_i/SHPinscher-Regular.otf", 28)
    button_rect1 = pygame.Rect(253, 193, 20, 18) #ekmek
    pygame.draw.rect(self.display_surface, (0, 0, 0), button_rect1) 
    text_surface1 = font.render("X", True, (255, 255, 255))
    text_rect1 = text_surface1.get_rect(center=button_rect1.center)
    self.display_surface.blit(text_surface1,text_rect1)

    button_rect2 = pygame.Rect(253, 237, 20, 18) #iksir
    pygame.draw.rect(self.display_surface, (0, 0, 0), button_rect2) 
    text_surface2 = font.render("X", True, (255, 255, 255))
    text_rect2 = text_surface2.get_rect(center=button_rect2.center)
    self.display_surface.blit(text_surface2, text_rect2)

    button_rect3 = pygame.Rect(253, 282, 20, 18) #energy bar
    pygame.draw.rect(self.display_surface, (0, 0, 0), button_rect3) 
    text_surface3 = font.render("X", True, (255, 255, 255))
    text_rect3 = text_surface3.get_rect(center=button_rect3.center)
    self.display_surface.blit(text_surface3, text_rect3)
# hikaye
  def story(self):
    self.story_açıldı=1
    font = pygame.font.Font("f_g_i/SHPinscher-Regular.otf", 38)
    text = font.render("""You are a person living under mandate and protection.""", True, (255, 0, 0))
    text_rect  = text.get_rect(center=(420, 140))
    text2 = font.render("""You must pay $1000 to the government by the 15th of the month.""", True, (255, 0, 0))
    text_rect2 = text.get_rect(center=(375, 190))
    self.display_surface.blit(text, text_rect)    
    self.display_surface.blit(text2, text_rect2)
    button_rect = pygame.Rect(820, 590, 30, 22) 
    pygame.draw.rect(self.display_surface, (0, 0, 0), button_rect) 
    font = pygame.font.Font("f_g_i/SHPinscher-Regular.otf", 30)
    text_surface3 = font.render("Skip", True, (255, 255, 255))
    text_rect3 = text_surface3.get_rect(center=button_rect.center)
    self.display_surface.blit(text_surface3, text_rect3)
    pygame.display.flip()
# borç ödeme
  def ödeme(self):
    s=pygame.image.load("f_g_i/ödeme.png").convert_alpha()
    s=pygame.transform.scale(s, (160,200))
    s_rect = s.get_rect(center=(200, 240))
    self.display_surface.blit(s, s_rect)
    
    button_rect = pygame.Rect(178, 175, 30, 22) 
    pygame.draw.rect(self.display_surface, (0, 0, 0), button_rect) 
    font = pygame.font.Font("f_g_i/SHPinscher-Regular.otf", 24)
    text_surface = font.render("Pay", True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=button_rect.center)
    self.display_surface.blit(text_surface, text_rect)
# son
  def end(self):
    self.end_açıldı=1
    self.display_surface.fill((0,0,0))
    font = pygame.font.Font("f_g_i/SHPinscher-Regular.otf", 38)
    text = font.render("""You have successfully made your payment""", True, (255, 0, 0))
    text_rect  = text.get_rect(center=(420, 140))
    text2 = font.render("""to the government on the 15th of the month.""", True, (255, 0, 0))
    text_rect2 = text.get_rect(center=(390, 190))
    self.display_surface.blit(text, text_rect)    
    self.display_surface.blit(text2, text_rect2)
    button_rect = pygame.Rect(820, 590, 30, 22)  
    font = pygame.font.Font("f_g_i/SHPinscher-Regular.otf", 30)
# son2
  def end2(self):
    self.end_açıldı=1
    self.display_surface.fill((0,0,0))
    font = pygame.font.Font("f_g_i/SHPinscher-Regular.otf", 38)
    font2 = pygame.font.Font("f_g_i/SHPinscher-Regular.otf", 50)
    text = font.render("""You couldn't pay your debt to the state,""", True, (255, 0, 0))
    text_rect  = text.get_rect(center=(460, 140))
    text2 = font.render(""" the state confiscated your farm.""", True, (255, 0, 0))
    text_rect2 = text.get_rect(center=(480, 190))
    text3 = font2.render("""Game Over.""", True, (255, 0, 0))
    text_rect3 = text3.get_rect(center=(470, 290))
    self.display_surface.blit(text, text_rect)    
    self.display_surface.blit(text2, text_rect2)
    self.display_surface.blit(text3, text_rect3)
    font = pygame.font.Font("f_g_i/SHPinscher-Regular.otf", 30)
# ölüm
  def died_end(self):
    self.end_açıldı=1
    self.display_surface.fill((0,0,0))
    font = pygame.font.Font("f_g_i/SHPinscher-Regular.otf", 42)
    font2 = pygame.font.Font("f_g_i/SHPinscher-Regular.otf", 50)
    text = font.render("""The soldiers shot you...""", True, (255, 0, 0))
    text_rect  = text.get_rect(center=(430, 170))
    text2 = font2.render("""Game Over.""", True, (255, 0, 0))
    text_rect2 = text.get_rect(center=(490, 250))
    self.display_surface.blit(text, text_rect)    
    self.display_surface.blit(text2, text_rect2)
    button_rect = pygame.Rect(820, 590, 30, 22) 
    pygame.draw.rect(self.display_surface, (0, 0, 0), button_rect) 
    font = pygame.font.Font("f_g_i/SHPinscher-Regular.otf", 30)
    self.game_over=1
# ölüm2
  def died_end2(self):
    self.end_açıldı=1
    self.display_surface.fill((0,0,0))
    font = pygame.font.Font("f_g_i/SHPinscher-Regular.otf", 42)
    font2 = pygame.font.Font("f_g_i/SHPinscher-Regular.otf", 50)
    text = font.render("""Your health is over, you are dead.""", True, (255, 0, 0))
    text_rect  = text.get_rect(center=(430, 170))
    text2 = font2.render("""Game Over.""", True, (255, 0, 0))
    text_rect2 = text2.get_rect(center=(440, 250))
    self.display_surface.blit(text, text_rect)    
    self.display_surface.blit(text2, text_rect2)
    button_rect = pygame.Rect(820, 590, 30, 22) 
    pygame.draw.rect(self.display_surface, (0, 0, 0), button_rect) 
    font = pygame.font.Font("f_g_i/SHPinscher-Regular.otf", 30)
    self.game_over=1
# ekranı kaydırma
  def shift_world(self, shift_x, shift_y):

    for sprite in self.all_sprites:
            sprite.rect.x += shift_x
            sprite.rect.y += shift_y

    for sprite in self.all_sprites2:
            sprite.rect.x += shift_x
            sprite.rect.y += shift_y
# saati ayralama
  def check_minute_elapsed(self):
    if self.süre>=20: 
      self.dakika += 5
      self.süre=0
# stalin konuşması        
  def stalin_walk(self):
    font = pygame.font.Font("f_g_i/SHPinscher-Regular.otf", 26)
    font2 = pygame.font.Font("f_g_i/SHPinscher-Regular.otf", 50)
    pygame.draw.rect(self.display_surface, (255, 255, 255), (150, 430, 600, 100))  
    text = font.render("""One of the trees in the bottom right is fake.You can escape""", True, (0, 0, 0))
    text_rect  = text.get_rect(center=(460, 475))
    text3 = font.render("""from there tomorrow morning.""", True, (0, 0, 0))
    text_rect3  = text3.get_rect(center=(320, 500))
    text2 = font.render("""Stalin:""", True, (0, 0, 0))
    text_rect2 = text2.get_rect(center=(200, 450))
    self.display_surface.blit(text, text_rect)    
    self.display_surface.blit(text2, text_rect2)
    self.display_surface.blit(text3, text_rect3) 
# çizdirme
  def run(self):
    self.süre+=0.5
    if self.saat>=18:
       self.kararma_derecesi=4
    if self.saat>=6 and self.saat<18:
       self.kararma_derecesi=2
    self.all_sprites.draw(self.display_surface)
  #  self.all_sprites2.draw(self.display_surface)
    self.slime.draw(self.display_surface)
    self.player.draw(self.display_surface)
    self.tree.draw(self.display_surface)
    self.player.update()
    self.collision()
    self.collision_y()
    
    self.update_health_bar() 
    self.update_strength_bar()
    self.update_hunger_bar() 
    self.update_level_bar()
    
    for sheep in self.sheeps.sprites():
      sheep.draw_health_bar(self.display_surface)
      if self.sheep_teması==0:
        sheep.move()

    for lama in self.lama.sprites():
      lama.draw_health_bar(self.display_surface)
      lama.move()

    for slime in self.slime.sprites():
      slime.draw_health_bar(self.display_surface)
      slime.move()
    
    for goblin in self.goblin.sprites():
      goblin.draw_health_bar(self.display_surface)
      if self.enemy_temas==1:
         goblin.animation_frames = [pygame.image.load("f_g_i/goblin_a.png").convert_alpha(),
                                    pygame.image.load("f_g_i/goblin_a.png").convert_alpha()]
         goblin.current_frame_index = 0
         goblin.image = goblin.animation_frames[goblin.current_frame_index]
         goblin.image = pygame.transform.scale(goblin.image, (34, 28)) 
         goblin.goblin_temas=1
      if self.enemy_temas==0:
         goblin.animation_frames = [pygame.image.load("f_g_i/goblin.png").convert_alpha(),pygame.image.load("f_g_i/goblin.png").convert_alpha()]
         goblin.current_frame_index = 0
         goblin.image = goblin.animation_frames[goblin.current_frame_index]
         goblin.image = pygame.transform.scale(goblin.image, (30, 28)) 
         goblin.goblin_temas=0
      if self.enemy_temas==0:
        goblin.move()

    if self.ekran_kaydır==0 and self.temas==0 and self.geçiş_temas==0:
      self.shift_world(-self.player.sprite.direction.x * self.player.sprite.speed, -self.player.sprite.direction.y * self.player.sprite.speed)

    if self.hunger<=10:
      self.health-=0.04
    
    if self.dakika>=60:
      self.saat+=1
      self.dakika=0

    if self.saat==24:
      self.saat=0
      self.day+=1
    
    self.check_minute_elapsed() 
    
    clock = pygame.time.Clock()
    dt = clock.tick(60) / 4000
    self.display(dt)

    if self.level_xp>=150:
      self.level_xp=0
      self.level+=1

  def run2(self):
    self.all_sprites2.draw(self.display_surface)
    self.map.draw(self.display_surface)
    self.water.draw(self.display_surface)