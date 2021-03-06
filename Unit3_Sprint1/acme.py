import random


class Product:
    def __init__(self, name):
        self.name = name
        self.price = 10
        self.weight = 20
        self.flammability = 0.5
        self.identifier = random.randint(1000000, 9999999)
     
    def stealability(self):
        if self.price/self.weight < 0.5:
            return 'Not so stealable...'
        elif self.price/self.weight >=0.5:
            return 'Kinda stealable.'
        else:
            return 'Very stealable!'

    def explode(self):
        if self.flammability*self.weight < 10:
            return '...fizzle'
        elif self.flammability*self.weight >= 10 and self.flammability*self.weight < 50:
            return '...boom!'
        else:
            return '...BABOOM'

class BoxingGlove(Product):
    def __init__(self, name):
        self.weight = 10
        
    def explode(self):
        return '...it"s a glove.'
        
    def punch(self):
        if self.weight < 5:
            return 'That tickles'
        else:
            return 'OUCH!'