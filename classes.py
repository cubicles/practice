# A Sample class with init method
class Person:

    # init method or constructor
    def __init__(self, name):
        self.name = name

    # Sample method
    def say_hi(self):
        print('Hello my name is', self.name)
    
    tension = []

p = Person('Gabriel')
p.say_hi()
