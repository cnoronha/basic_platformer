from player import Player
import pygame
from pygame.locals import *
from pygame import mixer
import pickle
from os import path
from world import World
from button import Button


mixer.pre_init(44100, -16, -2, 512)
mixer.init()
pygame.init()

clock = pygame.time.Clock()
fps = 45

screen_width = 1000
screen_height = 1000

# game variables
tile_size = 50
game_over = 0
main_menu = True
level = 1
max_levels = 5

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer of Destiny')

#images
bg_img = pygame.transform.scale(pygame.image.load('img/background.png').convert_alpha(), (screen_width,screen_height))
reset_img = pygame.image.load('img/reset_btn.png').convert_alpha()
start_img = pygame.image.load('img/start_btn.png').convert_alpha()
quit_img = pygame.image.load('img/quit_btn.png').convert_alpha()
home_img = pygame.image.load('img/home_btn.png').convert_alpha()


# misc functions
def reset_level(level):
    player.reset(100, screen_height-25) 
    spike_group.empty()
    plat_group.empty()
    saw_group.empty()
    exit_group.empty()
    if path.exists(f'level{level}_data'):
        pickle_in = open(f'level{level}_data', 'rb')
    data = pickle.load(pickle_in)
    world = World(data, screen_width, tile_size, spike_group, saw_group, plat_group, exit_group)
    return world


# player
player = Player(100, screen_height-25)

# obstacles
spike_group = pygame.sprite.Group()
plat_group = pygame.sprite.Group()

# enemies
saw_group = pygame.sprite.Group()

exit_group = pygame.sprite.Group()

sprites = [spike_group, saw_group]
# level data
if path.exists(f'level{level}_data'):
    pickle_in = open(f'level{level}_data', 'rb')
data = pickle.load(pickle_in)
world = World(data, screen_width, tile_size, spike_group, saw_group, plat_group, exit_group)

# buttons
reset_button = Button(screen_width//2+100, screen_height//4, reset_img)
home_button = Button(screen_width//2-200, screen_height//4, home_img)
start_button = Button(screen_width//4, screen_height//3, start_img)
quit_button = Button(screen_width-(screen_width//4)-200, screen_height//3, quit_img)


game_running = True
while game_running:

    clock.tick(fps)
    
    screen.blit(bg_img, (0,0))

    if main_menu:
        start = start_button.draw(screen)
        quit = quit_button.draw(screen)
        if quit:
            game_running = False
        if start:
            main_menu=False
            player.reset(100, screen_height-25)
            game_over = 0
    else:

        spike_group.draw(screen)
        plat_group.update()
        plat_group.draw(screen)
        saw_group.update()
        saw_group.draw(screen)
        exit_group.draw(screen)
        game_over = player.update(screen, world, spike_group, saw_group, exit_group, plat_group, game_over)

        # world.draw(screen_width, screen_height)
        for tile in world.tile_list:
                screen.blit(tile[0], tile[1])

        # lose game
        if game_over == -1:
            reset = reset_button.draw(screen)
            home = home_button.draw(screen)
            if reset:
                data = []
                world = reset_level(level)
                game_over = 0
            if home:
                main_menu = True

        # win game
        if game_over == 1:
            level += 1
            if level <= max_levels:
                # go to next level
                data = []
                world = reset_level(level)
                game_over = 0
            else:
                if reset_button.draw(screen):
                    level = 1
                    data = [] 
                    world = reset_level(level)
                    game_over = 0
                # game won, reset



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                data = []
                world = reset_level(level)
                game_over = 0
            if event.key == pygame.K_q:
                game_running = False


    pygame.display.update()




pygame.quit()