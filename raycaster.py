import config
import raylibpy as rl
import math  

class Raycaster:
    def __init__(self, player):
        self.player = player
        self.wall_texture = rl.load_texture("door.png")

    def cast_rays(self):
        for x in range(0, config.SCREEN_WIDTH, config.RAY_WIDTH):
            cameraX = 2 * x / config.SCREEN_WIDTH - 1 
            rayDirX = self.player.dirX + self.player.planeX * cameraX 
            rayDirY = self.player.dirY + self.player.planeY * cameraX 
              
            mapX = int(self.player.x)
            mapY = int(self.player.y) 

            epsilon = 1e-6

            deltaDistX = abs(1 / (rayDirX + epsilon))
            deltaDistY = abs(1 / (rayDirY + epsilon)) 
            
            stepX = 1 if rayDirX > 0 else -1
            stepY = 1 if rayDirY > 0 else -1
            
            sideDistX = (mapX + 1.0 - self.player.x) * deltaDistX if rayDirX > 0 else (self.player.x - mapX) * deltaDistX
            sideDistY = (mapY + 1.0 - self.player.y) * deltaDistY if rayDirY > 0 else (self.player.y - mapY) * deltaDistY

            hit = 0
            while hit == 0:
                if sideDistX < sideDistY:
                    sideDistX += deltaDistX
                    mapX += stepX
                    side = 0
                else:
                    sideDistY += deltaDistY
                    mapY += stepY
                    side = 1

                if config.MAP[mapY][mapX] > 0:
                    hit = config.MAP[mapY][mapX] 
            if hit == 1:
                if side == 0:
                    collisionX = mapX + (1 - stepX) / 2
                    collisionY = self.player.y + (collisionX - self.player.x) * rayDirY / rayDirX
                    perpWallDist = (collisionX - self.player.x) / rayDirX 
                    if rayDirX > 0:
                        color = (255, 0, 0, 255)  # East wall (for instance, red)
                    else:
                        color = (0, 255, 0, 255)  # West wall (for instance, green)
                else:
                    collisionY = mapY + (1 - stepY) / 2
                    collisionX = self.player.x + (collisionY - self.player.y) * rayDirX / rayDirY
                    perpWallDist = (collisionY - self.player.y) / rayDirY 
                    if rayDirY > 0:
                        color = (0, 0, 255, 255)  # North wall (for instance, blue)
                    else:
                        color = (255, 0, 255, 255)  # South wall (for instance, yellow)
                
                lineHeight = int(config.SCREEN_HEIGHT / perpWallDist)
                drawStart = -lineHeight // 2 + config.SCREEN_HEIGHT // 2
                drawEnd = lineHeight // 2 + config.SCREEN_HEIGHT // 2
                rl.draw_line(x, drawStart, x, drawEnd, color)
            elif hit == 2:  
                if side == 0:
                    collisionX = mapX + (1 - stepX) / 2
                    collisionY = self.player.y + (collisionX - self.player.x) * rayDirY / rayDirX
                    perpWallDist = (collisionX - self.player.x) / rayDirX 
                    tex_x = int(collisionY * self.wall_texture.width)  # For east/west walls
                else:
                    collisionY = mapY + (1 - stepY) / 2
                    collisionX = self.player.x + (collisionY - self.player.y) * rayDirX / rayDirY
                    perpWallDist = (collisionY - self.player.y) / rayDirY 
                    tex_x = int(collisionX * self.wall_texture.width)  # For north/south walls

                lineHeight = int(config.SCREEN_HEIGHT / perpWallDist)
                drawStart = -lineHeight // 2 + config.SCREEN_HEIGHT // 2
                drawEnd = lineHeight // 2 + config.SCREEN_HEIGHT // 2

                texture_rec = rl.Rectangle(tex_x, 0, config.RAY_WIDTH, self.wall_texture.height)
                dest_rec = rl.Rectangle(x, drawStart, config.RAY_WIDTH, lineHeight)

                rl.draw_texture_pro(self.wall_texture, texture_rec, dest_rec, rl.Vector2(0, 0), 0, rl.WHITE)


 