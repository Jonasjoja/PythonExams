class Animal:

    def __init__(self,name,species):
        self.name = name
        self.species = species
        
    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def makeSound(self,sound):
        print(f" this animals says {sound}")

class Dog(Animal):
    
    def __init__(self, name,breed,toy):
        super().__init__(name,species="Dog") #Refers to base/super class. Animal class here. Can remove species as a Dog will always be a Dog.
        self.breed = breed
        self.toy = toy

    def play(self):
        print(f"{self.name} plays with {self.toy}")

robert = Dog("Robert","Chiuaua","ball")
robert.play()