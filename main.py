import pygame
from pygame.locals import *

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
WINDOW_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
BLACK = (0, 0, 0)
OFF_WHITE = '#FAF9F6'
DARK_GRAY = '#4B4E54'
LIGHT_GRAY = '#B0B3B8'

def main():
    global current_screen
    
    current_screen = 'main_menu'
    # Initialise screen       
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption('Teste')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill('#586273')
    
    def buttons(buttonxpos, buttonypos, buttonw, buttonh, color, text, size):
        global current_screen
        
        pos = pygame.mouse.get_pos()
        button_font = pygame.font.Font(None, size)
        button_text = button_font.render(text, True, OFF_WHITE)
        
        button_surface = pygame.Surface((buttonw, buttonh))
        button_surface.fill(color)
        button_rect = pygame.Rect(buttonxpos, buttonypos, buttonw, buttonh)
        
        button_text_pos = button_text.get_rect(center=(button_surface.get_width()/2,
                                                       button_surface.get_height()/2))
        
        button_surface.blit(button_text, button_text_pos)
        background.blit(button_surface, (button_rect.x, button_rect.y))
        
        if button_rect.collidepoint(pos):
            button_surface.fill(LIGHT_GRAY)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    current_screen = 'fishing'

    def main_menu():
        screen.blit(background, (0, 0))
        buttons(((SCREEN_WIDTH-150)/2), ((SCREEN_HEIGHT-50)/5), 150, 50, LIGHT_GRAY, "Fishing", 24)
        
    def fishing_page():
        screen.blit(background, (0, 0))
        buttons(((SCREEN_WIDTH-150)/2), ((SCREEN_HEIGHT-50)/5), 150, 50, LIGHT_GRAY, "teste", 24)

        
    
    # Event loop
    while True:
        if current_screen == 'main_menu':
            main_menu()
        elif current_screen == 'fishing':
            fishing_page()
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        pygame.display.flip()
            
if __name__ == '__main__': main()