import asyncio
import pygame
import random
import pathfinding, tilemap # import custom libraries

# define classes
class Material:
    def __init__(self,name:str,quantity:int):
        self.name = str(name)
        self.quantity = int(quantity)
    
    def add(self,quantity):
        self.quantity += int(quantity)
    
    def use(self,quantity):
        if quantity <= self.quantity:
            self.quantity -= quantity
            return True
        else:
            return False

class Inhabitant:
    def __init__(self, name:str, workplace:Workplace, home:Home, happiness:int, health:int, age:int, productivity:int):
        self.name = name
        self.workplace = workplace
        self.home = home
        self.happiness = happiness
        self.productivity = productivity
        self.health = health
        self.age = age
    def move(self,destination:Building):
        # implement move algorithm here
        pass
    def entertain(self,potentialLocations):
        destination = random.choice(potentialLocations)
        self.move(destination)

class Building:
    def __init__(self, name:str, width:int, height:int, maxInhabitants:int):
        self.name = name
        self.width = width
        self.height = height
        self.inhabitants = []
        self.maxInhabitants = maxInhabitants
    def addInhabitant(self, inhabitant:Inhabitant):
        if len(self.inhabitants) < self.maxInhabitants:
            self.maxInhabitants.append(inhabitant)
            return True
        else:
            return False
    def removeInhabitant(self, inhabitant:Inhabitant):
        if inhabitant in self.inhabitants:
            self.inhabitants.remove(inhabitant)
            return True
        else:
            return False

class Home(Building):
    pass

class Workplace(Building):
    def __init__(self, name:str, width:int, height:int, productionMaterial:Material, maxInhabitants:int, productionQuantity:int):
        self.name = name
        self.width = width
        self.height = height
        self.productionMaterial = productionMaterial
        self.inhabitants = []
        self.productionQuantity = productionQuantity
        self.maxInhabitants = maxInhabitants
    def produce(self):
        self.productionMaterial.add(self.productionQuantity*len(inhabitants))


pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
screen.fill("red")
running = False
buildings = []

async def main():
    global running
    if running:
        clock.tick()
        pygame.display.flip()
        await asyncio.sleep(0)
    pygame.quit()
    sys.exit()

asyncio.run(main())
