class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health = "good"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Add your method here!
    
    def description(self):
        print self.name
        print self.age
        

hippo = Animal("Daniel", 32)

hippo.description()

sloth = Animal("Dean", 400)
ocelot = Animal("Du", 100)

print hippo.health
print sloth.health
print ocelot.health