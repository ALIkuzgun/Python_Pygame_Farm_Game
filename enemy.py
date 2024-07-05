import pygame,random
from config import *

class Slime(pygame.sprite.Sprite):
  def __init__(self, pos, size):
    super().__init__()
   # self.image=pygame.Surface((size,size))
    self.animation_frames = [pygame.image.load("f_g_i/g_slime1.png").convert_alpha(),
                         pygame.image.load("f_g_i/g_slime2.png").convert_alpha(),
                         pygame.image.load("f_g_i/g_slime1.png").convert_alpha()
                            ]
    self.current_frame_index = 0
    self.image = self.animation_frames[self.current_frame_index]
    self.image = pygame.transform.scale(self.image, (28, 20)) 
    self.rect = self.image.get_rect(topleft=pos)
    self.health, self.max_health =50, 50
    self.direction = pygame.math.Vector2(0, 0)
    self.animation_delay = 25  
    self.animation_counter = 0 
    self.move_direction = random.choice(["left","right","up","down"])
    self.haraket=0
    self.speed=2
  
  def draw_health_bar(self, surface):
        bar_height, bar_length = 5, 30 
        bar_fill = (self.health / self.max_health) * bar_length 
        bar_x = self.rect.x + (self.rect.width - bar_length) / 2
        bar_y = self.rect.y - 8

        pygame.draw.rect(surface, (255, 0, 0), (bar_x, bar_y, bar_length, bar_height))
        pygame.draw.rect(surface, (0, 255, 0), (bar_x, bar_y, bar_fill, bar_height))
  
  def move(self):
    self.direction.x, self.direction.y=0, 0
    
    if self.move_direction == "up":
        self.rect.y -= self.speed
        self.haraket+=1
    if self.move_direction == "down":
        self.rect.y += self.speed
        self.haraket+=1
    elif self.move_direction == "left":
        self.rect.x -= self.speed
        self.haraket+=1
        self.animation_frames = [pygame.image.load("f_g_i/g_slime3.png").convert_alpha(),
                         pygame.image.load("f_g_i/g_slime4.png").convert_alpha(),
                         pygame.image.load("f_g_i/g_slime3.png").convert_alpha() ]
        self.current_frame_index = 0
        self.image = self.animation_frames[self.current_frame_index]
        self.image = pygame.transform.scale(self.image, (28, 20)) 
        
    elif self.move_direction == "right":
        self.rect.x += self.speed
        self.haraket+=1
        self.animation_frames = [pygame.image.load("f_g_i/g_slime1.png").convert_alpha(),
                         pygame.image.load("f_g_i/g_slime2.png").convert_alpha(),
                         pygame.image.load("f_g_i/g_slime1.png").convert_alpha()
                            ]
        self.current_frame_index = 0
        self.image = self.animation_frames[self.current_frame_index]
        self.image = pygame.transform.scale(self.image, (28, 20)) 

    if self.haraket>=40:
        self.haraket=0
        self.move_direction=random.choice(["left","right","up","down"])

  def update(self):
    self.move()
    self.animation_counter += 1
    if self.animation_counter >= self.animation_delay:
            self.animation_counter = 0
            self.current_frame_index = (self.current_frame_index + 1) % len(self.animation_frames)
            self.image = self.animation_frames[self.current_frame_index]

class Goblin(pygame.sprite.Sprite):
  def __init__(self, pos, size):
    super().__init__()
   # self.image=pygame.Surface((size,size))
    self.animation_frames = [pygame.image.load("f_g_i/goblin.png").convert_alpha(),
                         pygame.image.load("f_g_i/goblin.png").convert_alpha()
                            ]
    self.current_frame_index = 0
    self.image = self.animation_frames[self.current_frame_index]
    self.image = pygame.transform.scale(self.image, (30, 28)) 
    self.rect = self.image.get_rect(topleft=pos)
    self.health, self.max_health =50, 50
    self.direction = pygame.math.Vector2(0, 0)
    self.animation_delay = 55  
    self.animation_counter = 0 
    self.move_direction = random.choice(["left","right","up","down"])
    self.haraket=0
    self.speed=2
    self.goblin_temas=0
  
  def draw_health_bar(self, surface):
        bar_height, bar_length = 5, 30 
        bar_fill = (self.health / self.max_health) * bar_length 
        bar_x = self.rect.x + (self.rect.width - bar_length) / 2
        bar_y = self.rect.y - 8

        pygame.draw.rect(surface, (255, 0, 0), (bar_x, bar_y, bar_length, bar_height))
        pygame.draw.rect(surface, (0, 255, 0), (bar_x, bar_y, bar_fill, bar_height))
  
  def move(self):
    self.direction.x, self.direction.y=0, 0
    
    if self.move_direction == "up":
        self.rect.y -= self.speed
        self.haraket+=1
    if self.move_direction == "down":
        self.rect.y += self.speed
        self.haraket+=1
    elif self.move_direction == "left":
        self.rect.x -= self.speed
        self.haraket+=1
        self.animation_frames = [pygame.image.load("f_g_i/goblin2.png").convert_alpha(),
                         pygame.image.load("f_g_i/goblin.png").convert_alpha()]
        self.current_frame_index = 0
        self.image = self.animation_frames[self.current_frame_index]
        self.image = pygame.transform.scale(self.image, (30, 28)) 
        
    elif self.move_direction == "right":
        self.rect.x += self.speed
        self.haraket+=1
        self.animation_frames = [pygame.image.load("f_g_i/goblin.png").convert_alpha(),
                         pygame.image.load("f_g_i/goblin.png").convert_alpha()]
        self.current_frame_index = 0
        self.image = self.animation_frames[self.current_frame_index]
        self.image = pygame.transform.scale(self.image, (30, 28)) 

    if self.haraket>=40:
        self.haraket=0
        self.move_direction=random.choice(["left","right","up","down"])

    if self.goblin_temas==0:    
        self.animation_frames = [pygame.image.load("f_g_i/goblin.png").convert_alpha(),
                         pygame.image.load("f_g_i/goblin.png").convert_alpha()]
    if self.goblin_temas==1:
        self.animation_frames = [pygame.image.load("f_g_i/goblin_ab.png").convert_alpha(),
                         pygame.image.load("f_g_i/goblin_a.png").convert_alpha()]
        self.current_frame_index = 0
        self.image = self.animation_frames[self.current_frame_index]
        self.image = pygame.transform.scale(self.image, (34, 28)) 
        print("enemy png değişti")

  def update(self):
    self.animation_counter += 1
    if self.animation_counter >= self.animation_delay:
            self.animation_counter = 0
            self.current_frame_index = (self.current_frame_index + 1) % len(self.animation_frames)
            self.image = self.animation_frames[self.current_frame_index]