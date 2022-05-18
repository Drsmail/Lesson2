import pygame

class UI:

    def __init__(self,screen):
        self.display_surface = screen



        #health
        self.health_bar = pygame.image.load("Ino_game_asssets/User_Interface/hf.png")
        self.health_bar_pos = (70,70)
        self.health_bar_width = (83-44) + 1  # 44 21  #83 25
        self.health_bar_height = 25 - 21
        self.health_bar_offset = (44,21)
        #    381,79

        #fruits
        self.fruit_icon = pygame.image.load("Ino_game_asssets/User_Interface/fp.png")
        self.fruit_icon_pos = (80, 125)
        #'Ino_game_asssets/User_Interface/ARCADEPI.TTF'
        self.font = pygame.font.Font('Ino_game_asssets/User_Interface/ARCADEPI.TTF', 35)

    def draw_health(self, current, max_value):

        self.display_surface.blit(self.health_bar,self.health_bar_pos)
        ratio = current/max_value
        pos = (self.health_bar_pos[0] + self.health_bar_offset[0],self.health_bar_pos[1] + self.health_bar_offset[1])
        health_bar_rect = pygame.Rect(pos, (self.health_bar_width * ratio, self.health_bar_height))
        color = 'red'
        pygame.draw.rect(self.display_surface, color, health_bar_rect)



    def draw_fruits(self, amount):

        self.display_surface.blit(self.fruit_icon, self.fruit_icon_pos)
        frits_surf = self.font.render(str(amount), True, 'green')
        rect = self.fruit_icon.get_rect(topleft = self.fruit_icon_pos)
        frits_rect = frits_surf.get_rect(midleft = (rect.right + 5, rect.centery ))
        self.display_surface.blit(frits_surf, frits_rect)


        pass