import config
from player import Player
from raycaster import Raycaster
import raylibpy as rl 
from config import MAP

def main():
    rl.init_window(config.SCREEN_WIDTH, config.SCREEN_HEIGHT, "Pixel Gallery")
    rl.set_target_fps(config.FPS) 

    player = Player(2, 2)
    raycaster = Raycaster(player)

    while not rl.window_should_close():
        player.handle_input(MAP)
        raycaster.cast_rays()

        rl.begin_drawing()
        rl.clear_background(rl.RAYWHITE)

        #raycaster.draw_map()
        
        rl.end_drawing()

    rl.close_window()

if __name__ == "__main__":
    main()
