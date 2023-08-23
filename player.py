import raylibpy as rl
import math

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rotation = 0  # Angle at which the player is facing, initially set to 0.
        self.move_speed = 0.05  # Speed of movement forward/backward.
        self.rotation_speed = 0.05  # Speed of rotation.
        self.dirX = 1
        self.dirY = 0
        self.planeX = 0 
        self.planeY = 0.66   
        self.rotation_angle = 0  # Angle in radians

    def handle_input(self, world_map):
        if rl.is_key_down(rl.KEY_W):
            new_x = self.x + self.dirX * self.move_speed
            new_y = self.y + self.dirY * self.move_speed
            
            if world_map[int(new_x)][int(self.y)] == 0:
                self.x = new_x
            if world_map[int(self.x)][int(new_y)] == 0:
                self.y = new_y

        if rl.is_key_down(rl.KEY_S):
            new_x = self.x - self.dirX * self.move_speed
            new_y = self.y - self.dirY * self.move_speed
            
            if world_map[int(new_x)][int(self.y)] == 0:
                self.x = new_x
            if world_map[int(self.x)][int(new_y)] == 0:
                self.y = new_y

        if rl.is_key_down(rl.KEY_D):
            # Turn left.
            self.rotation_angle += self.rotation_speed
            if self.rotation_angle >= 2 * math.pi:
                self.rotation_angle -= 2 * math.pi

        if rl.is_key_down(rl.KEY_A):
            # Turn right.
            self.rotation_angle -= self.rotation_speed
            if self.rotation_angle < 0:
                self.rotation_angle += 2 * math.pi

        # Update direction and camera plane vectors based on rotation_angle
        self.dirX = math.cos(self.rotation_angle)
        self.dirY = math.sin(self.rotation_angle)

        # The camera plane is perpendicular to the direction vector
        self.planeX = -self.dirY
        self.planeY = self.dirX