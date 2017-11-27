
from turtle import *
colormode(255)
import random
#class Square(Turtle):
    #def __init__(self,size):
        #Turtle.__init__(self)
        #self.shapesize(size)
        #self.shape("square")
    #def Random_color(self):
        #g = random.randint(0,256)
        #r = random.randint(0,256)
        #b = random.randint(0,256)
        #self.color(r,g,b)

#square1 = Square(10)
#square1.Random_color()


#class Hexagon(Turtle):
    #def __init__(self,size,color):
        #Turtle.__init__(self)
        #self.shapesize(size)
        #self.color(color)
        #self.begin_poly()
        #for i in range (6):
            #self.forward(10)
            #self.right(60)
        #self.end_poly()
        #register_shape("hexagon", self.get_poly())
        #self.shape("hexagon")
#hexagon1 = Hexagon(1,"blue")

class Rectangle(Turtle):
    def __init__(self,size,width,hight):
        Turtle.__init__(self)
        self.shapesize(size)
        self.width(width)
        self.hight(hight)
        self.begin_poly()
        self.forward(width)
        self.right(90)
        self.forward(hight)
        self.right(90)
        self.forward(width)
        self.right(90)
        self.forward(hight)
        self.end_poly()
        register_shape("rectangle",self.get_poly())
        self.shape("rectangle")
rectangle1 = Rectangle(10,10,15)
        
        
