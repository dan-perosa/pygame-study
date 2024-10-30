import pygame
from pygame.locals import *
from start_fishing import start_fishing
from start_woodcutting import start_woodcutting
import sys

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
WINDOW_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
BLACK = (0, 0, 0)
OFF_WHITE = '#FAF9F6'
DARK_GRAY = '#4B4E54'
LIGHT_GRAY = '#B0B3B8'
BACKGROUND_COLOR = '#586273'

def button_click_handle(button_functionality, button_text, chosen):
    global current_screen
    if button_functionality == 'set_fishing_screen':
        current_screen = button_text
    elif button_functionality == 'set_main_menu_screen':
        current_screen = button_text
    elif button_functionality == 'set_woodcutting_screen':
        current_screen = button_text
    elif button_functionality == 'start_fishing_in_pond':
        start_fishing(chosen)
    elif button_functionality == 'start_woodcutting_in_forest':
        start_woodcutting(chosen)
    
    return

def main():
    global background
    global current_screen
    current_screen = 'Main menu'
    # Initialise screen       
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption('Teste')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()

    def buttons(buttonxpos, buttonypos, buttonw, buttonh, color, text, size, functionality, chosen):
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
        screen.blit(button_surface, (button_rect.x, button_rect.y))
        
        if button_rect.collidepoint(pos):
            button_surface.fill(LIGHT_GRAY)
            button_surface.blit(button_text, button_text_pos)
            screen.blit(button_surface, (button_rect.x, button_rect.y))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    button_click_handle(functionality, text, chosen)

    def main_menu():
        screen.fill(BACKGROUND_COLOR)
        buttons(((SCREEN_WIDTH-150)/2), ((SCREEN_HEIGHT-50)/5), 150, 50, DARK_GRAY, "Fishing", 24, 'set_fishing_screen', '')
        buttons(((SCREEN_WIDTH-150)/2), ((SCREEN_HEIGHT-50)/5*2), 150, 50, DARK_GRAY, "Woodcutting", 24, 'set_woodcutting_screen', '')
        
    def fishing_page():
        screen.fill(BACKGROUND_COLOR)
        buttons(((SCREEN_WIDTH-150)/2), ((SCREEN_HEIGHT-50)/5), 150, 50, DARK_GRAY, "Pond", 24, 'start_fishing_in_pond', 'pond')
        buttons(((SCREEN_WIDTH-150)/2), ((SCREEN_HEIGHT-50)/5*4), 150, 50, DARK_GRAY, "Main menu", 24, 'set_main_menu_screen', '')
    
    def woodcutting_page():
        screen.fill(BACKGROUND_COLOR)
        buttons(((SCREEN_WIDTH-150)/2), ((SCREEN_HEIGHT-50)/5), 150, 50, DARK_GRAY, "Forest", 24, 'start_woodcutting_in_forest', 'forest')
        buttons(((SCREEN_WIDTH-150)/2), ((SCREEN_HEIGHT-50)/5*4), 150, 50, DARK_GRAY, "Main menu", 24, 'set_main_menu_screen', '')

    # Event loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        if current_screen == 'Main menu':
            main_menu()
        elif current_screen == 'Fishing':
            fishing_page()
        elif current_screen == 'Woodcutting':
            woodcutting_page()
            
        pygame.display.flip()

    sys.exit()
    pygame.quit()
            
if __name__ == '__main__': main()