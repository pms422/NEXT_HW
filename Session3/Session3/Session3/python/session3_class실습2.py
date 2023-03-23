class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    
    def introduce(self):
        print(f"{self.name} is {self.age} years old and has {self.height}")
    
    def yell(self):
        print("아?")

class Developer(Person):
    keyboard = '기계식'
    def __init__(self, name, age, height):
        super().__init__(name, age, height)
    
    def yell(self):
        print("어?")

minsu = Developer("minsu", 25, 174)
minsu.yell()