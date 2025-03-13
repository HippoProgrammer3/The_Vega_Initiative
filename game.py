# game.py
from pyscript import display
from tilemap import Tilemap
import random, math, time, pygame

class material:
    def __init__(self, name:str, quantity:int):
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
    def __init__(self, reference:hex, name:str, width:int, height:int, workers:list, maxWorkers:int):
        self.name = name
        self.width = width
        self.height = height
        self.reference = reference

class workplace(building):
    def __init__(self, reference:hex, name:str, width:int, height:int, productionMaterial:material, workers:list, maxWorkers:int, productionRate:int, productionQuantity:int):
        self.name = name
        self.width = width
        self.height = height
        self.reference = reference
        self.productionMaterial = productionMaterial
        self.workers = workers
        self.productionRate = productionRate
        self.productionQuantity = productionQuantity
        self.maxWorkers = maxWorkers
    
    def produce(self):
        if self.workers == self.maxWorkers:
            self.productionMaterial.add(self.productionQuantity)
        else:
            self.productionMaterial.add(self.productionQuantity*(self.workers/self.maxWorkers))

class home(building):
    def __init__(self, reference:hex, name:int, width:int, height:int, residents:list, maxResidents:int):
        self.name = name
        self.width = width
        self.height = height
        self.reference = reference
        self.residents = residents
        self.maxResidents = maxResidents
    
    def addResident(self, resident):
        if len(self.residents) < self.maxResidents:
            self.residents.append(resident)
        else:
            print("Home is full")
    
    def removeResident(self, resident):
        if resident in self.residents:
            self.residents.remove(resident)
        else:
            print("Resident not found")

class statusWorker:
    def __init__(self, name:str):
        self.name = name

class worker:
    def __init__(self, name:str, status:statusWorker, reference:hex, workplace:workplace, home:home, happiness:float, health:float, age:float, productivity:float):
        self.name = name
        self.reference = reference
        self.workplace = workplace
        self.home = home
        self.happiness = happiness
        self.productivity = productivity
        self.health = health
        self.age = age
        self.status = status
    
    def assignHome(self):
        if homes.len() > 1:
            self.workplace = random.choice(homes)
        else:
            return("No available homes to assign to")
    
    def assignWorkplace(self, type):
        if workplaces.len() > 1:
            

    def move(self, destination):
        # Use A* Algorithm to pathfind
    
    def entertain(self):
        destination = random.choice(entertainmentBuildings)
        self.move(destination)






entertainmentBuildings = []
workplaces = []
homes = []
citisens = []
numCitisens = citisens.len()
lastTime = time.time()
timeStep = 1/60
accumulator = 0.0
game = True
currentTime = time.time()

while game:
    currentTime = time.time()
    deltaTime = currentTime-lastTime
    lastTime = currentTime
    accumulator += deltaTime

    while accumulator >= timeStep:
        accumulator -= timeStep