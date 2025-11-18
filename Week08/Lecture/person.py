class Person:
    def __init__(self, id, myName, age=10):
        self.id = id
        self.name = myName
        self.age = age
    
    def __str__(self):
        return "A person whose name is " + self.name + ", age is " + str(self.age)
    
    def __repr__(self):
        return self.name + " - " + str(self.age)
    
    # setter method
    def changeAge(self, newAge):
        if isinstance(newAge, int):
            if newAge > 0:
                self.age = newAge
            else:
                print("Age must be positive")
        else:
            print("Age should be integer!")
    
    # getter method
    def getAge(self):
        return self.age