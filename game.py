# game.py
import json
from pyscript import display

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
    def __init__(self, reference, name, width, height, productionMaterial, workers, maxWorkers, productionRate, productionQuantity, livingCapacity):
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