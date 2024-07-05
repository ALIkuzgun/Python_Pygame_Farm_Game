import pygame
class Npc(pygame.sprite.Sprite):
  def __init__(self, pos, size):
    super().__init__()
    self.image=pygame.Surface((size,size))
    self.image = pygame.image.load("f_g_i/npc.png").convert_alpha()
    self.image = pygame.transform.scale(self.image, (35, 30)) 
    self.rect = self.image.get_rect(topleft=pos)

class Npc_satış(pygame.sprite.Sprite):
  def __init__(self, pos, size):
    super().__init__()
    self.image=pygame.Surface((size,size))
    self.image = pygame.image.load("f_g_i/npc2.png").convert_alpha()
    self.image = pygame.transform.scale(self.image, (30, 30)) 
    self.rect = self.image.get_rect(topleft=pos)

class Npc_asker(pygame.sprite.Sprite):
  def __init__(self, pos, size):
    super().__init__()
    self.image=pygame.Surface((size,size))
    self.image = pygame.image.load("f_g_i/asker.png").convert_alpha()
    self.image = pygame.transform.scale(self.image, (30, 30)) 
    self.rect = self.image.get_rect(topleft=pos)