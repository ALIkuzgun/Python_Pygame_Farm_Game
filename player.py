import pygame,os
from config import *
class Player(pygame.sprite.Sprite):
  def __init__(self,pos):
    super().__init__() 
    self.image = pygame.image.load("f_g_i/c1.png").convert_alpha()
    self.image = pygame.transform.scale(self.image, (21, 30)) 
    self.rect = self.image.get_rect(topleft=pos)

    self.right, self.left=1,0
    self.haraket=1
    self.zeminteması=0
    self.k2=0
    self.k3=0
    self.k4=0
    self.x=0
    self.speed=1
    self.png=1
    self.p, self.o=0,0
    self.can_move = True
    
    self.strength_decrease_timer = pygame.time.get_ticks()  
    self.hunger_decrease_timer = pygame.time.get_ticks()  
    self.strength_decrease_delay = 10000
    self.hunger_decrease_delay = 8900

    if self.png==1:
      self.images_left =[    
      pygame.transform.scale(pygame.image.load(os.path.join('f_g_i/c1.png')), (22, 29)),
      pygame.transform.scale(pygame.image.load(os.path.join('f_g_i/c1.png')), (22, 29)),
      pygame.transform.scale(pygame.image.load(os.path.join('f_g_i/c1.png')), (22, 29)),
    ]

    if self.png==1:
      self.images_right = [
      pygame.transform.scale(pygame.image.load(os.path.join('f_g_i/c1.png')), (22, 29)),
      pygame.transform.scale(pygame.image.load(os.path.join('f_g_i/c1.png')), (22, 29)),
      pygame.transform.scale(pygame.image.load(os.path.join('f_g_i/c1.png')), (22, 29)),
    ]
    
    self.direction=pygame.math.Vector2(0,0)
    self.speed=4
    self.gravity=1
    self.jump_speed=-13
    self.is_jumping = False
    self.animation_counter = 0 
    self.facing="right"
    self.a=0
    self.b=1
    self.c=0
    self.e_1=0
    self.attack=0
    self.kılıç=1
    self.total_distance = 0
    self.çapa=0
    
    self.attack_animation_frames = [
      pygame.transform.scale(pygame.image.load(os.path.join('f_g_i/ca1.png')), (24, 29)), 
      pygame.transform.scale(pygame.image.load(os.path.join('f_g_i/ca3.png')), (30, 29)),      
      pygame.transform.scale(pygame.image.load(os.path.join('f_g_i/ca2.png')), (34, 29))]
    self.attack_animation_frames2 = [
      pygame.transform.scale(pygame.image.load(os.path.join('f_g_i/ca4.png')), (24, 29)), 
      pygame.transform.scale(pygame.image.load(os.path.join('f_g_i/ca5.png')), (30, 29)),      
      pygame.transform.scale(pygame.image.load(os.path.join('f_g_i/ca6.png')), (34, 29))]

    self.çapa_animation_frames = [
      pygame.transform.scale(pygame.image.load(os.path.join('f_g_i/cç2.png')), (25, 29)), 
      pygame.transform.scale(pygame.image.load(os.path.join('f_g_i/cç3.png')), (30, 29)),      
      pygame.transform.scale(pygame.image.load(os.path.join('f_g_i/cç1.png')), (34, 29))]
    self.çapa_animation_frames2 = [
      pygame.transform.scale(pygame.image.load(os.path.join('f_g_i/cç5.png')), (25, 29)), 
      pygame.transform.scale(pygame.image.load(os.path.join('f_g_i/cç6.png')), (30, 29)),      
      pygame.transform.scale(pygame.image.load(os.path.join('f_g_i/cç4.png')), (34, 29))]
    
    self.attack_animation_index = 0
    self.attack_animation_counter = 0

    self.attack_index = 0
    self.attack_counter = 0
    self.is_attacking=False
    self.pos = pos

    self.çapa_animation_index = 0
    self.çapa_animation_counter = 0

    self.çapa_index = 0
    self.çapa_counter = 0
    self.is_çapa=False
    self.topla=0
  
  def get_input(self):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and self.can_move == True:
        self.direction.x = -1
        self.facing = "left"
        self.left=1
        self.right=0
    elif keys[pygame.K_RIGHT] and self.can_move == True:
        self.direction.x = 1
        self.facing = "right"
        self.right=1
        self.left=0
    else:
        self.direction.x = 0

    if keys[pygame.K_UP] and self.can_move == True:
      self.direction.y = -1
    elif keys[pygame.K_DOWN] and self.can_move == True:
      self.direction.y = 1
    else:
        self.direction.y = 0

    if keys[pygame.K_SPACE] and self.kılıç==1:
        self.is_attacking = True
        self.a = 1
        self.haraket = 0
        self.attack=1
    else:
        self.a = 0
        self.haraket = 1
        self.attack=0

    if keys[pygame.K_v]:
        self.is_çapa = True
        self.haraket = 0
        self.çapa=1
        self.topla=1
    else:
        self.a = 0
        self.haraket = 1
        self.çapa=0
        self.topla=0
      
    if keys[pygame.K_x]:
      self.x = 1
      self.png=0
      if self.facing=="right":
         self.images_right=[    
          pygame.transform.scale(pygame.image.load(os.path.join('f_g_i/c3.png')), (28, 30)),
          pygame.transform.scale(pygame.image.load(os.path.join('f_g_i/c3.png')), (28, 30)),
          pygame.transform.scale(pygame.image.load(os.path.join('f_g_i/c3.png')), (28, 30)),
        ]
      if self.facing=="left":
         self.images_left=[    
          pygame.transform.scale(pygame.image.load(os.path.join('f_g_i/c3.png')), (28, 30)),
          pygame.transform.scale(pygame.image.load(os.path.join('f_g_i/c3.png')), (28, 30)),
          pygame.transform.scale(pygame.image.load(os.path.join('f_g_i/c3.png')), (28, 30)),
        ]

    else:
      self.x = 0
      self.png=1
      self.images_left =[    
      pygame.transform.scale(pygame.image.load(os.path.join('f_g_i/c1.png')), (22, 29)),
      pygame.transform.scale(pygame.image.load(os.path.join('f_g_i/c1.png')), (22, 29)),
      pygame.transform.scale(pygame.image.load(os.path.join('f_g_i/c1.png')), (22, 29)),
    ]

      self.images_right = [
      pygame.transform.scale(pygame.image.load(os.path.join('f_g_i/c1.png')), (22, 29)),
      pygame.transform.scale(pygame.image.load(os.path.join('f_g_i/c1.png')), (22, 29)),
      pygame.transform.scale(pygame.image.load(os.path.join('f_g_i/c1.png')), (22, 29)),
    ]
    
    if keys[pygame.K_c]:
      self.c = 1
    else:
       self.c = 0

    if keys[pygame.K_1]:
      self.e_1=1
    else:
      self.e_1=0

    if keys[pygame.K_p]:
      self.p=1
    else:
      self.p=0

    if keys[pygame.K_o]:
      self.o=1
    else:
      self.o=0
  
  def animate(self):
        if self.facing == "right":
          self.image = self.images_right[self.animation_counter // 10 % len(self.images_right)]
          self.image.set_colorkey((255, 255, 255))
        elif self.facing == "left":
          self.image = pygame.transform.flip(self.images_left[self.animation_counter // 10 % len(self.images_left)], True, False)
          self.image.set_colorkey((255, 255, 255))
          
        if self.is_attacking and self.right==1 and self.left==0:
          self.image = self.attack_animation_frames[self.attack_index]
          self.image.set_colorkey((255, 255, 255))
          self.attack_counter += 1
          if self.attack_counter >= 5:
            self.attack_counter = 0
            self.attack_index += 1
            if self.attack_index >= len(self.attack_animation_frames):
                self.is_attacking = False
                self.attack_index = 0

        if self.is_attacking and self.right==0 and self.left==1:
          self.image = self.attack_animation_frames2[self.attack_index]
          self.image.set_colorkey((214, 214, 214))
          self.attack_counter += 1
          if self.attack_counter >= 5:
            self.attack_counter = 0
            self.attack_index += 1
            if self.attack_index >= len(self.attack_animation_frames2):
                self.is_attacking = False
                self.attack_index = 0

        if self.is_çapa and self.right==1 and self.left==0:
          self.image = self.çapa_animation_frames[self.çapa_index]
          self.image.set_colorkey((255, 255, 255))
          self.çapa_counter += 1
          if self.çapa_counter >= 5:
            self.çapa_counter = 0
            self.çapa_index += 1
            if self.çapa_index >= len(self.çapa_animation_frames):
                self.is_çapa = False
                self.çapa_index = 0

        if self.is_çapa and self.right==0 and self.left==1:
          self.image = self.çapa_animation_frames2[self.çapa_index]
          self.image.set_colorkey((214, 214, 214))
          self.çapa_counter += 1
          if self.çapa_counter >= 5:
            self.çapa_counter = 0
            self.çapa_index += 1
            if self.çapa_index >= len(self.çapa_animation_frames2):
                self.is_çapa = False
                self.çapa_index = 0
    
        self.animation_counter += 1
    
  def update(self):
        self.get_input()
        self.animate()