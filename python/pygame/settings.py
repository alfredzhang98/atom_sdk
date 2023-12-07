import pygame
import os

class PygameSettings:
    def __init__(self, window_width = 800, window_hight = 600, caption = "Default", background_image = [str(os.getcwd()) + "\python\pygame\source\default0.png", str(os.getcwd()) + "\python\pygame\source\default1.png"]):
        pygame.init()
        self.window_width = window_width
        self.window_hight = window_hight
        self.background_image = background_image
        self.font_text = 'freesansbold.ttf'
        self.font_size = 16
        # main objects
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(self.font_text, self.font_size)
        self.caption = pygame.display.set_caption(caption)
        self.screen = pygame.display.set_mode((self.window_width, self.window_hight))
        self.update_background(0)
        pygame.display.update()

    def update_black_background(self):
        self.screen.fill((0, 0, 0))

    def update_background(self, index):
        self.background = pygame.image.load(self.background_image[index])
        self.background = pygame.transform.scale(self.background, (self.window_width, self.window_hight))
        self.screen.blit(self.background, (0, 0))

    def get_screen(self):
        return self.screen
    
    def get_clock(self):
        return self.clock

# 测试
if  __name__ == "__main__":
    pygame_settings = PygameSettings()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

