import config
import raylibpy as rl 

class MiniMap:
    def __init__(self, player):
        self.player = player

    def draw(self):
        for y, row in enumerate(config.MAP):
            for x, tile in enumerate(row):
                tile_color = rl.DARKGRAY if tile == 1 else rl.LIGHTGRAY
                rl.draw_rectangle(x * config.MINI_TILE_SIZE, y * config.MINI_TILE_SIZE, config.MINI_TILE_SIZE, config.MINI_TILE_SIZE, tile_color)

        player_x_on_map = int(self.player.x / config.TILE_SIZE) * config.MINI_TILE_SIZE
        player_y_on_map = int(self.player.y / config.TILE_SIZE) * config.MINI_TILE_SIZE
        rl.draw_rectangle(player_x_on_map, player_y_on_map, config.MINI_TILE_SIZE, config.MINI_TILE_SIZE, rl.RED) 
