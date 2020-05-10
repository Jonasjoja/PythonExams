class User:

    def __init__(self,firstName,surName):
        self.firstName = firstName
        self.surName = surName

    def fullName(self):
        return f"{self.firstName} {self.surName}" 






user1 = User("Jonas","Hansen")
print(user1.fullName())