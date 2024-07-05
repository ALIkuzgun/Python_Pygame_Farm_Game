import pygame
from config import *

class Tile(pygame.sprite.Sprite):

  def __init__(self, pos, size):
    super().__init__()
    self.image = pygame.Surface((size, size))
    self.image.fill((147,142,35))
    self.image = pygame.transform.scale(self.image, (32, 32)) 
    self.rect = self.image.get_rect(topleft=pos) 

class Tile2(pygame.sprite.Sprite):

  def __init__(self, pos, size):
    super().__init__()
    self.image = pygame.Surface((size, size))
    self.image.fill((147,142,135))
    self.image = pygame.transform.scale(self.image, (32, 16)) 
    self.rect = self.image.get_rect(topleft=pos) 

class Farm(pygame.sprite.Sprite):

  def __init__(self, pos, size):
    super().__init__()
    self.image = pygame.Surface((size, size))
    self.image = pygame.image.load("f_g_i/g_farm2.png").convert_alpha()
    self.image = pygame.transform.scale(self.image, (32,32)) 
    self.rect = self.image.get_rect(topleft=pos) 
    self.state = None 
    self.type = "g_farm2" 
    self.soğan_type=""
    self.patates_type=""
    self.çapalanmış=0 

class Geçiş(pygame.sprite.Sprite):

  def __init__(self, pos, size):
    super().__init__()
    self.image = pygame.Surface((size, size))
    self.image.fill((230,30,35))
    self.image = pygame.transform.scale(self.image, (32,32)) 
    self.rect = self.image.get_rect(topleft=pos)

class Sınır(pygame.sprite.Sprite):

  def __init__(self, pos, size):
    super().__init__()
    self.image = pygame.Surface((size, size))
    self.image.fill((21,210,235))
    self.image = pygame.transform.scale(self.image, (32,32)) 
    self.rect = self.image.get_rect(topleft=pos)

class Çit1(pygame.sprite.Sprite):

  def __init__(self, pos, size):
    super().__init__()
    self.image = pygame.Surface((size, size))
    self.image.fill((0,142,35))
    self.image = pygame.transform.scale(self.image, (16, 32)) 
    self.rect = self.image.get_rect(topleft=pos) 

class Çit2(pygame.sprite.Sprite):

  def __init__(self, pos, size):
    super().__init__()
    self.image = pygame.Surface((size, size))
    self.image.fill((0,142,35))
    self.image = pygame.transform.scale(self.image, (32, 16)) 
    self.rect = self.image.get_rect(topleft=pos) 

class Map(pygame.sprite.Sprite):

  def __init__(self, pos, size):
    super().__init__()
    self.image=pygame.Surface((size,size))
   # self.image.fill("grey")
    self.image = pygame.image.load("f_g_i/g_map1.png").convert_alpha()
    self.image = pygame.transform.scale(self.image, (2240,2240)) 
    self.rect = self.image.get_rect(topleft=pos)

class Xp(pygame.sprite.Sprite):

  def __init__(self, pos, size):
    super().__init__()
    self.image=pygame.Surface((size,size))
    self.image = pygame.image.load("f_g_i/xp.png").convert_alpha()
    self.image = pygame.transform.scale(self.image, (10,10)) 
    self.rect = self.image.get_rect(topleft=pos)
    self.direction = pygame.math.Vector2(0, 0) 
    self.speed = 3

class Tree(pygame.sprite.Sprite):

  def __init__(self, pos, size):
    super().__init__()
    self.image=pygame.Surface((size,size))
    self.image = pygame.image.load("f_g_i/ağaç.png").convert_alpha()
    self.image = pygame.transform.scale(self.image, (65,70)) 
    self.rect = self.image.get_rect(topleft=pos)
    self.direction = pygame.math.Vector2(0, 0) 
    self.speed = 3
    self.type = "ağaç" 

class Bed(pygame.sprite.Sprite):

  def __init__(self, pos, size):
    super().__init__()
    self.image=pygame.Surface((size,size))
    self.image.fill("grey")
    self.image = pygame.transform.scale(self.image, (46,50)) 
    self.rect = self.image.get_rect(topleft=pos)
    self.direction = pygame.math.Vector2(0, 0) 
    self.speed = 3

class Water(pygame.sprite.Sprite):

  def __init__(self, pos, size):
    super().__init__()
    self.image = pygame.Surface((size, size))
    self.image.fill((147,0,0))
    self.image = pygame.transform.scale(self.image, (32, 32)) 
    self.rect = self.image.get_rect(topleft=pos) 