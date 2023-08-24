import raylibpy as rl
import math
import config

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
        self.inventory = []
        self.show_inventory = False
        self.inventory_key_pressed = False
 
    def is_valid_position(self, world_map, x, y):
        map_height = len(world_map)
        map_width = len(world_map[0])

        map_x = int(x)
        map_y = int(y)

        if map_x < 0 or map_x >= map_width or map_y < 0 or map_y >= map_height:
            return False

        return world_map[map_y][map_x] == 0

    def handle_input(self, world_map):
        if self.show_inventory: 
            if rl.is_key_pressed(rl.KEY_I):
                self.show_inventory = False
        else:
            if rl.is_key_down(rl.KEY_W):
                new_x = self.x + self.dirX * self.move_speed
                new_y = self.y + self.dirY * self.move_speed 
                if self.is_valid_position(world_map, new_x, new_y):
                    self.x = new_x
                    self.y = new_y

            if rl.is_key_down(rl.KEY_S):
                new_x = self.x - self.dirX * self.move_speed
                new_y = self.y - self.dirY * self.move_speed 
                if self.is_valid_position(world_map, new_x, new_y):
                    self.x = new_x
                    self.y = new_y

            if rl.is_key_down(rl.KEY_D):
                oldDirX = self.dirX
                self.dirX = self.dirX * math.cos(self.rotation_speed) - self.dirY * math.sin(self.rotation_speed)
                self.dirY = oldDirX * math.sin(self.rotation_speed) + self.dirY * math.cos(self.rotation_speed)
                oldPlaneX = self.planeX
                self.planeX = self.planeX * math.cos(self.rotation_speed) - self.planeY * math.sin(self.rotation_speed)
                self.planeY = oldPlaneX * math.sin(self.rotation_speed) + self.planeY * math.cos(self.rotation_speed)

            if rl.is_key_down(rl.KEY_A):
                oldDirX = self.dirX
                self.dirX = self.dirX * math.cos(-self.rotation_speed) - self.dirY * math.sin(-self.rotation_speed)
                self.dirY = oldDirX * math.sin(-self.rotation_speed) + self.dirY * math.cos(-self.rotation_speed)
                oldPlaneX = self.planeX
                self.planeX = self.planeX * math.cos(-self.rotation_speed) - self.planeY * math.sin(-self.rotation_speed)
                self.planeY = oldPlaneX * math.sin(-self.rotation_speed) + self.planeY * math.cos(-self.rotation_speed)
        
            if rl.is_key_pressed(rl.KEY_I) and not self.inventory_key_pressed:
                self.show_inventory = True
                self.inventory_key_pressed = True

        if rl.is_key_released(rl.KEY_I):
            self.inventory_key_pressed = False

    def draw(self):  
        if self.show_inventory:
            draw_inventory(self)

    def add_item_to_inventory(self, item):
        self.inventory.append(item)

    def remove_item_from_inventory(self, item):
        self.inventory.remove(item)

class Item:
    def __init__(self, name):
        self.name = str(name) 

    def __str__(self):
            return self.name

class Collectible:
    def __init__(self, name, description):
        self.name = name
        self.description = description

def collect_item(player, collectible):
    player.inventory.append(collectible)

def draw_inventory(player):
    rl.draw_rectangle(10, 110, 220, 200, rl.Color(0, 0, 0, 200))  

    rl.draw_text("Inventory", 20, 130, 20, (0, 255, 0, 255)) 

    item_y = 160
    for item in player.inventory:
        rl.draw_text(str(item), 40, item_y, 20, rl.RAYWHITE)  
        item_y += 30
