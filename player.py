import raylibpy as rl
import math

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rotation = 0.0
        self.move_speed = 0.05
        self.rotation_speed = 0.05
        self.dirX = 1.0
        self.dirY = 0.0
        self.planeX = 0.0
        self.planeY = 0.66

    def is_valid_position(self, world_map, x, y):
        map_height = len(world_map)
        map_width = len(world_map[0])

        map_x = int(x)
        map_y = int(y)

        if map_x < 0 or map_x >= map_width or map_y < 0 or map_y >= map_height:
            return False

        return world_map[map_y][map_x] == 0

    def handle_input(self, world_map):
        if rl.is_key_down(rl.KEY_W):
            new_x = self.x + self.dirX * self.move_speed
            new_y = self.y + self.dirY * self.move_speed 
            if self.is_valid_position(world_map, new_x, new_y):
                self.x = new_x
                self.y = new_y

        if rl.is_key_down(rl.KEY_S):
            new_x = self.x - self.dirX * self.move_speed
            new_y = self.y - self.dirY * self.move_speed
            if (
                world_map[int(new_x)][int(self.y)] == 0
                and world_map[int(self.x)][int(new_y)] == 0
            ):
                self.x = new_x
                self.y = new_y

        if rl.is_key_down(rl.KEY_A):
            oldDirX = self.dirX
            self.dirX = self.dirX * math.cos(self.rotation_speed) - self.dirY * math.sin(self.rotation_speed)
            self.dirY = oldDirX * math.sin(self.rotation_speed) + self.dirY * math.cos(self.rotation_speed)
            oldPlaneX = self.planeX
            self.planeX = self.planeX * math.cos(self.rotation_speed) - self.planeY * math.sin(self.rotation_speed)
            self.planeY = oldPlaneX * math.sin(self.rotation_speed) + self.planeY * math.cos(self.rotation_speed)

        if rl.is_key_down(rl.KEY_D):
            oldDirX = self.dirX
            self.dirX = self.dirX * math.cos(-self.rotation_speed) - self.dirY * math.sin(-self.rotation_speed)
            self.dirY = oldDirX * math.sin(-self.rotation_speed) + self.dirY * math.cos(-self.rotation_speed)
            oldPlaneX = self.planeX
            self.planeX = self.planeX * math.cos(-self.rotation_speed) - self.planeY * math.sin(-self.rotation_speed)
            self.planeY = oldPlaneX * math.sin(-self.rotation_speed) + self.planeY * math.cos(-self.rotation_speed)
