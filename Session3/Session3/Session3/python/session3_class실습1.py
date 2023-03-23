class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    
    def introduce(self):
        print(f"{self.name} is {self.age} years old and has {self.height}")
    
    def yell(self):
        print("아?")

minsu = Person("minsu", 25, 174)
minsu.introduce()