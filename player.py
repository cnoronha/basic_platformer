import pygame

class Player():
    def __init__(self, x, y):
        self.reset(x,y)
        

        

    def update(self,screen, world, spike_group, saw_group, exit_group, plat_group, game_over):

        dx = 0
        dy = 0
        col_thresh = 20
        img_R = pygame.image.load('img/NinjaMan_R.png').convert_alpha()
        img_L = pygame.image.load('img/NinjaMan_L.png').convert_alpha()


        if game_over == 0:
            # get key presses
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT]:
                self.dir = 1
                dx -= 5
                self.image = pygame.transform.scale(img_L, self.size)
                
            if key[pygame.K_RIGHT]:
                self.dir = 0
                dx += 5
                self.image = pygame.transform.scale(img_R, self.size)
                
            if key[pygame.K_UP] and self.jumped==False and self.in_air == False:
                self.vel_y = -15
                self.jumped = True
            if key[pygame.K_UP]==False:
                self.jumped = False
            if key[pygame.K_SPACE] and self.dashed==False and self.air_dash == False:
                if self.dir == 0:
                    self.vel_x += 10
                elif self.dir == 1:
                    self.vel_x -= 10
                self.dashed = True
                if self.in_air == True:
                    self.air_dash = True
            if key[pygame.K_SPACE] == False: 
                self.dashed = False

            
            # add gravity
            if self.air_dash == True and self.vel_x != 0:
                self.vel_y = 0
            else:
                self.vel_y +=1
                if self.vel_y > 10:
                    self.vel_y = 10
            # add drag
            if self.vel_x > 0:
                self.dashed = True
                self.vel_x -= 1
                if self.vel_x ==0:
                    
                    self.vel_x = 0
            if self.vel_x < 0:
                self.dashed = True
                self.vel_x += 1
                if self.vel_x ==0:
                    
                    self.vel_x = 0


            dy += self.vel_y
            dx += self.vel_x

            self.in_air = True
            # check for object collision
            for tile in world.tile_list:
                # check in x direction
                if tile[1].colliderect(self.rect.x+dx, self.rect.y, self.width, self.height):
                    dx = 0
                # check in y direction
                if tile[1].colliderect(self.rect.x, self.rect.y+dy, self.width, self.height):
                    # check if below ground(jump into block)
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                    # check above ground(falling) 
                    elif self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0
                        self.in_air = False
                        self.air_dash = False

            # check for harmful object collision
            if pygame.sprite.spritecollide(self, spike_group, False):
                game_over = -1
            
            if pygame.sprite.spritecollide(self, saw_group, False):
                game_over = -1

            # check for moving platform collision

            for platform in plat_group:
                #collision in the x direction
                if platform.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                #collision in the y direction
                if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    #check if below platform
                    if abs((self.rect.top + dy) - platform.rect.bottom) < col_thresh:
                        self.vel_y = 0
                        dy = platform.rect.bottom - self.rect.top
                    #check if above platform
                    elif abs((self.rect.bottom + dy) - platform.rect.top) < col_thresh:
                        self.rect.bottom = platform.rect.top - 1
                        self.in_air = False
                        self.air_dash = False
                        dy = 0
                    #move sideways with the platform
                    if platform.move_x != 0:
                        self.rect.x += platform.move_direction
            
            
            # check for exit collision
            if pygame.sprite.spritecollide(self, exit_group, False):
                game_over = 1
            
            
                


            # move player
            self.rect.x += dx
            self.rect.y += dy

        
        # draw player
        screen.blit(self.image, self.rect)
        return game_over
       
    def reset(self, x, y):
        img_R = pygame.image.load('img/NinjaMan_R.png')
        self.size = (25, 25)
        self.image = pygame.transform.scale(img_R, self.size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_x = 0
        self.vel_y = 0
        self.jumped = False
        self.in_air = True
        self.dir = 0 # 0 = Right, 1 = Left
        self.dashed = False
        self.air_dash = True