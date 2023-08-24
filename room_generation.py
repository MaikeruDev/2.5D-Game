import random

WIDTH = 80
HEIGHT = 30

# Constants
WALL = 1
EMPTY = 0
DOOR = 2

def create_empty_map(width, height):
    return [[WALL if x == 0 or y == 0 or x == width-1 or y == height-1 else EMPTY for x in range(width)] for y in range(height)]

def add_door(map_, x1, y1, x2, y2):
    doors = []
    if x2 - x1 > 2:
        doors.extend([(random.randint(x1+1, x2-2), y1), (random.randint(x1+1, x2-2), y2-1)])
    if y2 - y1 > 2:
        doors.extend([(x1, random.randint(y1+1, y2-2)), (x2-1, random.randint(y1+1, y2-2))])
    
    if not doors:  # If we can't place a door, exit the function
        return
    
    door = random.choice(doors)
    map_[door[1]][door[0]] = DOOR


def split_rectangle(map_, x1, y1, x2, y2):
    MIN_SIZE = 8  # Minimum room size. Adjust as needed.
    horizontal_possible = y2 - y1 > 2 * MIN_SIZE
    vertical_possible = x2 - x1 > 2 * MIN_SIZE

    if not horizontal_possible and not vertical_possible:
        return

    if horizontal_possible and (not vertical_possible or random.choice(['H', 'V']) == 'H'):  # Horizontal split
        split_y = random.randint(y1 + MIN_SIZE, y2 - MIN_SIZE)
        for x in range(x1, x2):
            map_[split_y][x] = WALL
        split_rectangle(map_, x1, y1, x2, split_y)
        split_rectangle(map_, x1, split_y, x2, y2)
        add_door(map_, x1, split_y, x2, split_y+1)
    elif vertical_possible:  # Vertical split
        split_x = random.randint(x1 + MIN_SIZE, x2 - MIN_SIZE)
        for y in range(y1, y2):
            map_[y][split_x] = WALL
        split_rectangle(map_, x1, y1, split_x, y2)
        split_rectangle(map_, split_x, y1, x2, y2)
        add_door(map_, split_x, y1, split_x+1, y2)

""" def print_map(map_):
    for row in map_:
        for tile in row:
            if tile == WALL:
                print('#', end='')
            elif tile == DOOR:
                print('D', end='')
            else:
                print(' ', end='')
        print() """

map_ = create_empty_map(WIDTH, HEIGHT)
split_rectangle(map_, 0, 0, WIDTH, HEIGHT)
 
