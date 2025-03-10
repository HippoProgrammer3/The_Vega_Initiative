# game.py
import json
from pyscript import display

# Define a fixed (non-random) tile map for your city.
# For simplicity, each tile is initially "empty".
world_width = 100
world_height = 100
tile_map = [["empty" for _ in range(world_width)] for _ in range(world_height)]

class material:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
    
    def add(self, quantity):
        self.quantity += quantity

    def canuUse(self, quantity):
        if self.quantity >= quantity:
            return True
        else:
            return False
        
    def use(self, quantity):
        if self.canuUse(quantity):
            return True
        else:
            return False



class building:
    def __init__(self, reference, name, width, height, productionMaterial, workers, productionRate, productionQuantity, livingCapacity):
        self.name = name
        self.width = width
        self.height = height
        self.reference = reference
        self.productionMaterial = productionMaterial
        self.workers = workers
        self.productionRate = productionRate
        self.productionQuantity = productionQuantity
        self.livingCapacity = livingCapacity
        self.maxWorkers = maxWorkers
    
    def produce(self):
        if self.workers == self.maxWorkers:
            self.productionMaterial.add(self.productionQuantity)
        else:
            self.productionMaterial.add(self.productionQuantity*(self.workers/self.maxWorkers))

class worker:
    def __init__(self, name, reference, workplace, home, happiness, health, age, productivity):
        self.name = name
        self.reference = reference
        self.workplace = workplace
        self.home = home
        self.happiness = happiness
        self.productivity = productivity
        self.health = health
        self.age = age
    
    def move(self, workplace):
        # Use A* algorithm once pull request is merged
        self.workplace = workplace






# Function to check if a building can be placed at (x, y)
# building_width and building_height are in number of tiles.
def can_place_building(x, y, building_width, building_height):
    # Ensure the building is fully within the bounds.
    if x < 0 or y < 0 or y + building_height > world_height or x + building_width > world_width:
        return False
    # Check each tile that the building would cover.
    for i in range(y, y + building_height):
        for j in range(x, x + building_width):
            if tile_map[i][j] != "empty":
                return False
    return True

# Function to place a building (for example, called when the player clicks)
def place_building(x, y, building_width, building_height, building_type="generic"):
    if can_place_building(x, y, building_width, building_height):
        for i in range(y, y + building_height):
            for j in range(x, x + building_width):
                tile_map[i][j] = building_type
        return f"{building_type} placed at ({x}, {y})!"
    else:
        return "Invalid placement!"

# (Optional) Expose game state for debugging or UI updates.
def get_game_state():
    return {"tile_map": tile_map, "world_width": world_width, "world_height": world_height}

# Display the initial tile map state (for debugging in the PyScript console)
display(tile_map)

