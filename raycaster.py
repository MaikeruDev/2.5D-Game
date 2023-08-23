import config
import raylibpy as rl
import math

class Raycaster:
    def __init__(self, player):
        self.player = player

    def cast_rays(self):
        for x in range(0, config.SCREEN_WIDTH, config.RAY_WIDTH):
            # Calculate ray position and direction
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

            # DDA algorithm
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
                    hit = 1 

            if side == 0:
                perpWallDist = (mapX - self.player.x + (1 - stepX) / 2) / rayDirX 
                if rayDirX > 0:
                    color = (255, 0, 0, 255)  # East wall (for instance, red)
                else:
                    color = (0, 255, 0, 255)  # West wall (for instance, green)
            else:
                perpWallDist = (mapY - self.player.y + (1 - stepY) / 2) / rayDirY 
                if rayDirY > 0:
                    color = (0, 0, 255, 255)  # North wall (for instance, blue)
                else:
                    color = (255, 255, 0, 255)  # South wall (for instance, yellow)
                

            lineHeight = int(config.SCREEN_HEIGHT / perpWallDist)

            drawStart = -lineHeight // 2 + config.SCREEN_HEIGHT // 2
            drawEnd = lineHeight // 2 + config.SCREEN_HEIGHT // 2

            rl.draw_line(x, drawStart, x, drawEnd, color)


"""     def draw_map(self):
        for y, row in enumerate(config.MAP):
            for x, tile in enumerate(row):
                if tile == 1:
                    rl.draw_rectangle(x * config.TILE_SIZE, y * config.TILE_SIZE, config.TILE_SIZE, config.TILE_SIZE, rl.GRAY) """
