class Human():
    def __init__(self,first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f"Human named {self.first} {self.last} aged {self.age}"

    def __len__(self): #Defining len method to represent "length of life" / age
        return self.age

    def __add__(self,other):
        if isinstance(other,Human): #just a check to see if other instance is a human
            return(Human(first="Newborn",last=self.last, age=0))
        return "U cant add that"




j = Human("Human1","Humanson",30)
k = Human("Human2","Humanita",23)
print(len(j))

print(j+k)
print(j)
