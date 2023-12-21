import pygame
from settings import PygameSettings
from button import ButtonControl


if __name__ == '__main__':
    u_PygameSettings = PygameSettings()
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
                    u_PygameSettings.update_background(1)

        button.button_loop(button, screen, mouse_pos)

        pygame.display.update()
        
    pygame.quit()
