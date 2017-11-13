class animal(object):
    def __init__(self,sound,name,age,favorite_color):
        self.sound = sound
        self.name = name
        self.age = age
        self.favorite_color = favorite_color
    def eat(self,food):
        print("yummy!! " + self.name + " is eating " + food)
    def description(self):
        print(self.name + " is " + str(self.age) + " years old and loves the color " + self.favorite_color)
    def make_sound(self):
        print(self.sound * 3 )
cat = animal("meaw","george",2,"blue")
cat.eat("fish")
cat.description()
cat.make_sound()

class person(object):
    def __init__(self,name,age,city,gender,):
        self.name = name
        self.age = age
        self.city = city
        self.gender = gender
        
    def eat(self,food):
        print("i want to eat " + food)
    def play(self,sport):
        print("i like to play " + sport)

adan = person("adan",14 , "nazareth" , "female")
adan.eat("waraq dawali")
adan.play("basketball")
