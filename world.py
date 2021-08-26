from obstacles import Exit, Platform, Sawman, Spikes
import pygame

class World():
    def __init__(self, data, screen_width, tile_size, spike_group, saw_group, plat_group, exit_group):
        self.tile_list = []
        # data = self.make_data(screen_width, tile_size)
        #images
        ground_img = pygame.image.load('img/ground.png').convert_alpha()
        snow_ground_img = pygame.image.load('img/snow_ground.png').convert_alpha()

        
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(ground_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(snow_ground_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    spikes = Spikes(col_count*tile_size, row_count*tile_size+(tile_size//2), tile_size)
                    spike_group.add(spikes)
                if tile == 4:
                    saw_man = Sawman(col_count*tile_size, row_count*tile_size, tile_size, 1, 0)
                    saw_group.add(saw_man)
                if tile == 5:
                    saw_man = Sawman(col_count*tile_size, row_count*tile_size, tile_size, 0, 1)
                    saw_group.add(saw_man)
                if tile == 6:
                    platform = Platform(col_count*tile_size, row_count*tile_size, tile_size, 1, 0)
                    plat_group.add(platform)
                if tile == 7:
                    platform = Platform(col_count*tile_size, row_count*tile_size, tile_size, 0, 1)
                    plat_group.add(platform)
                if tile == 8: 
                    exit_door = Exit(col_count*tile_size, row_count*tile_size, tile_size)
                    exit_group.add(exit_door)
                
                col_count += 1
            row_count += 1

    