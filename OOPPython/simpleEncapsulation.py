class Pizza():
    def __init__(self,topping):
        self.__topping = None #private
        self.topping = topping

    
    @property #using property decorator, getter method
    def topping(self):
        print("Getter method called")
        return self.__topping

    @topping.setter #setter
    def topping(self, topping):
        if(topping != "Pepperoni"):
            print("Setter method called")
            self.__topping = "Pepperoni"
            print(f"YOU CAN ONLY HAVE PEPPERONI!! NOT {topping}")
        else:    
            print("Setter method called")
            self.__topping = topping

yourPizza = Pizza()
myPizza = Pizza()
testPiz = Pizza()

yourPizza.topping = "Pineapple"
myPizza.topping = "Pepperoni"

print(testPiz.topping)
print(myPizza.topping)
print(yourPizza.topping)