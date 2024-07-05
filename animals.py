import pygame, random

class Sheep(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load("f_g_i/sheep.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (24,20)) 
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.yön = random.choice(["left", "right"])
        self.max_health = 100  
        self.health = self.max_health
        self.left,self.right = 0,0
        self.mesafe = 0
        self.type="normal"

    def draw_health_bar(self, surface):
        bar_length = 30 
        bar_height = 5 
        bar_fill = (self.health / self.max_health) * bar_length 
        bar_x = self.rect.x + (self.rect.width - bar_length) / 2
        bar_y = self.rect.y - 10

        pygame.draw.rect(surface, (255, 0, 0), (bar_x, bar_y, bar_length, bar_height))
        pygame.draw.rect(surface, (0, 255, 0), (bar_x, bar_y, bar_fill, bar_height))

    def move(self):        
        if self.yön == "left":
           self.rect.x -= 1
           self.mesafe += 1
           self.left, self.right = 1, 0        
        elif self.yön == "right":
           self.rect.x += 1
           self.mesafe += 1        
           self.left, self.right = 0, 1        
        elif self.yön == "up":
           self.rect.y -= 1
           self.mesafe += 1        
        elif self.yön == "down":
           self.rect.y += 1
           self.mesafe += 1        
        elif self.yön == "stay":    
           self.mesafe += 1

        if self.mesafe >= 100:
            self.yön = random.choice(["left", "right", "up", "down", "stay"])
            self.mesafe = 0

        if self.left==1:
            self.image = pygame.image.load("f_g_i/sheep2.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (24,20)) 
        elif self.right==1:
            self.image = pygame.image.load("f_g_i/sheep.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (24,20)) 

    def update(self):
        self.direction.x,self.direction.y=0,0

class Lama(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load("f_g_i/lama.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (27,37)) 
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.yön = random.choice(["left", "right", "up", "down", "stay"])
        self.max_health = 100  
        self.health = self.max_health
        self.mesafe = 0
        self.left,self.right = 0,0

    def draw_health_bar(self, surface):
        bar_length = 30 
        bar_height = 5 
        bar_fill = (self.health / self.max_health) * bar_length 
        bar_x = self.rect.x + (self.rect.width - bar_length) / 2
        bar_y = self.rect.y - 10

        pygame.draw.rect(surface, (255, 0, 0), (bar_x, bar_y, bar_length, bar_height))
        pygame.draw.rect(surface, (0, 255, 0), (bar_x, bar_y, bar_fill, bar_height))

    def move(self):        
        if self.yön == "left":
           self.rect.x -= 1
           self.mesafe += 1
           self.left, self.right = 1, 0        
        elif self.yön == "right":
           self.rect.x += 1
           self.mesafe += 1        
           self.left, self.right = 0, 1        
        elif self.yön == "up":
           self.rect.y -= 1
           self.mesafe += 1        
        elif self.yön == "down":
           self.rect.y += 1
           self.mesafe += 1        
        elif self.yön == "stay":    
           self.mesafe += 1

        if self.mesafe >= 100:
            self.yön = random.choice(["left", "right", "up", "down", "stay"])
            self.mesafe = 0

        if self.left==1:
            self.image = pygame.image.load("f_g_i/lama2.png").convert_alpha()
        elif self.right==1:
            self.image = pygame.image.load("f_g_i/lama.png").convert_alpha()

    def update(self):
        self.direction.x,self.direction.y=0,0