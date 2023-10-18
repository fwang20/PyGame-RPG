import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type, surface = pygame.Surface((TILESIZE, TILESIZE))):
        super().__init__(groups)
        self.sprite_type = sprite_type
        self.image = surface
        if sprite_type == 'object':
            self.rect = self.image.get_rect(bottomleft = (pos[0], pos[1] - TILESIZE + 32))
        else:
            self.rect = self.image.get_rect(topleft = pos)

        self.hitbox = self.rect.inflate(0, -10)

        if (surface.get_size()[0] == 16 and surface.get_size()[1] == 16):
            self.hitbox = self.rect.inflate(-15.99999, 0)

        #tree
        if (surface.get_size()[0] == 96 and surface.get_size()[1] == 96):
            self.hitbox = self.rect.inflate(-70, -45)
        if (surface.get_size()[0] == 96 and surface.get_size()[1] == 128):
            self.hitbox = self.rect.inflate(-55, -45)

        #small house
        if (surface.get_size()[0] == 112 and surface.get_size()[1] == 176):
            self.hitbox = self.rect.inflate(-30, -55)

        # red small house
        if (surface.get_size()[0] == 144 and surface.get_size()[1] == 160):
            self.hitbox = self.rect.inflate(-55, -55)

        #fence
        if (surface.get_size()[0] == 144 and surface.get_size()[1] == 144):
            self.hitbox = self.rect.inflate(-25, -35)

        #rock and sign and bush
        if (surface.get_size()[0] == 48 and surface.get_size()[1] == 48):
             self.hitbox = self.rect.inflate(-45, -30)

        # minirock
        if (surface.get_size()[0] == 48 and surface.get_size()[1] == 16):
            self.hitbox = self.rect.inflate(-47, 0)

        #vertical looking rock
        if (surface.get_size()[0] == 48 and surface.get_size()[1] == 80):
            self.hitbox = self.rect.inflate(-40, -35)

        #BIG HOUSES
        if (surface.get_size()[0] == 208 and surface.get_size()[1] == 176):
            self.hitbox = self.rect.inflate(-45, -55)
