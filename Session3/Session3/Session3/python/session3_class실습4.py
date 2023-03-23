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

class Designer(Person):
    def __init__(self, name, age, height, disease):
        super().__init__(name, age, height)
        self.disease = disease
    
class ProductManager(Person):
    def __init__(self, name, age, height):
        super().__init__(name, age, height)
    def aging(self):
        self.age += 2
        self.height -= 5
        print("개발자를 새로 뽑아야하나...")
        Developer.keyboards = '엠브레인'
    def yell(self):
        print("개발자님 여기 오류있어요")


d1 = Developer("minsu",25,174)
d2 = Designer("minsu",25,174,"X")
p1 = ProductManager("minsu",25,174)
d1.introduce()
d1.yell()
d2.introduce()
d2.yell()
p1.introduce()
p1.yell()
p1.aging()
p1.introduce()




