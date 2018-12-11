class Animal:
    def __init__(self):
        print("Animal Created")
    def animaleat(self):
        print("Animal Eating")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")
    def WhoAmI(self):
        print("Dog")
    def Action(self):
        print("Whoof!")

# Aobj = Animal()
Dobj = Dog()

# Aobj.animaleat()
Dobj.WhoAmI()
Dobj.animaleat()
