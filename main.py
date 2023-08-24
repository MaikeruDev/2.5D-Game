import config
from player import Player
from raycaster import Raycaster
import raylibpy as rl 
from config import MAP
from minimap import MiniMap 
import raycaster

def main():
    rl.init_window(config.SCREEN_WIDTH, config.SCREEN_HEIGHT, "Pixel Gallery")
    rl.set_target_fps(config.FPS) 

    player = Player(2, 2)

    raycaster = Raycaster(player)
    
    mini_map = MiniMap(player)


    while not rl.window_should_close():
        player.handle_input(MAP)
        raycaster.cast_rays()
         
        rl.draw_text("Mini Map", 10, 70, 20, rl.DARKGRAY)
        draw_mini_map(player)
        rl.draw_fps(config.SCREEN_WIDTH - 100, 10) 

        rl.begin_drawing()
        rl.clear_background(rl.RAYWHITE) 
        
        rl.end_drawing()

    rl.close_window()

def draw_mini_map(player):
    map_scale = 5 
    map_x = 10
    map_y = 10

    for y, row in enumerate(config.MAP):
        for x, tile in enumerate(row):
            if tile == 1:
                rl.draw_rectangle(map_x + x * map_scale, map_y + y * map_scale, map_scale, map_scale, rl.DARKGRAY)

    player_map_x = int(player.x * map_scale) + map_x
    player_map_y = int(player.y * map_scale) + map_y
    rl.draw_circle(player_map_x, player_map_y, 3, rl.RED) 


if __name__ == "__main__":
    main()
