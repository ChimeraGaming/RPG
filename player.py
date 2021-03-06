import items, action, world

class Player():
    def __init__(self):
        self.inventory = [items.Gold(15), items.Rock()]
        self.hp = 100
        self.location_x, self.location_y = world.starting_position
        self.victory = False
 
    def is_alive(self):
        return self.hp > 0
 
    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')

# Actions
def move(self, dx, dy):
    self.location_x += dx
    self.location_y += dy
    print(world.tile_exists(self.location_x, self.location_y).intro_text())
 
def move_north(self):
    self.move(dx=0, dy=-1)
 
def move_south(self):
    self.move(dx=0, dy=1)
 
def move_east(self):
    self.move(dx=1, dy=0)
 
def move_west(self):