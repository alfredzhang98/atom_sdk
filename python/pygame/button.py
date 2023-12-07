import pygame
from settings import PygameSettings

class ButtonControl:
    def __init__(self, pos_x, pos_y, width, height, text='', font='freesansbold.ttf',
                 text_color=(255, 255, 255), bg_color=(59, 89, 152), text_size=16,
                 text_offset=(0, 0), border_radius=30):  # 添加圆角半径参数
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.text = text
        self.font = font
        self.text_color = text_color
        self.bg_color = bg_color
        self.hover_color = (80, 120, 200)  # 修改悬停颜色
        self.current_color = self.bg_color
        self.text_size = text_size
        self.text_offset = text_offset
        self.border_radius = border_radius  # 圆角半径
        self.button_clicked_status = False
        self.create_widget()

    def create_widget(self):
        self.widget = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        pygame.draw.rect(self.widget, self.current_color, 
                         pygame.Rect(0, 0, self.width, self.height), 
                         border_radius=self.border_radius)  # 绘制圆角矩形
        font = pygame.font.Font(self.font, self.text_size)
        text_surf = font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect()
        text_rect.center = (self.width // 2, self.height // 2)
        self.widget.blit(text_surf, text_rect)

    def is_clicked(self, pos):
        return self.pos_x < pos[0] < self.pos_x + self.width and self.pos_y < pos[1] < self.pos_y + self.height

    def button_clicked(self, text):
        self.button_clicked_status = True
        if text == None:
            pass
        self.set_text(text)
        self.set_text_color((255, 255, 255))
        self.set_bg_color((59, 89, 152))

    def get_button_clicked_status(self):
        return self.button_clicked_status

    def is_hovered(self, pos):
        return self.pos_x < pos[0] < self.pos_x + self.width and self.pos_y < pos[1] < self.pos_y + self.height

    def set_text(self, text):
        self.text = text
        self.create_widget()

    def set_text_color(self, color):
        self.text_color = color
        self.create_widget()

    def set_bg_color(self, color):
        self.bg_color = color
        self.current_color = self.bg_color
        self.create_widget()

    def button_loop(self, u_button, u_screen, mouse_pos):
        if u_button.is_hovered(mouse_pos):
            u_button.current_color = u_button.hover_color
        else:
            u_button.current_color = u_button.bg_color
        u_button.create_widget()
        u_screen.blit(self.widget, (self.pos_x, self.pos_y))


if __name__ == '__main__':
    u_PygameSettings = PygameSettings()
    u_PygameSettings.update_background(0)
    screen = u_PygameSettings.get_screen()
    button = ButtonControl(250, 300, 300, 50, 'Click Me!')
    
    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and not button.get_button_clicked_status():
                if button.is_clicked(mouse_pos):
                    print('Button clicked!')
                    button.button_clicked('Clicked!')

        button.button_loop(button, screen, mouse_pos)

        pygame.display.update()
        
    pygame.quit()
