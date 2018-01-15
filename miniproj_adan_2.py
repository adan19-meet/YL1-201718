import turtle
import math
import random
import time
from ball import Ball



#turtle.tracer(0)
turtle.hideturtle()
RUNNING = True
SLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2


MY_BALL = Ball(0,0,10,10,13,"green")
NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5
BALLS = []


#PART 0
for i in range(NUMBER_OF_BALLS):
    X = random.randint(round(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS),round(SCREEN_WIDTH - MAXIMUM_BALL_RADIUS))
    
    Y = random.randint(round(- SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS),round(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
    DX = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX )
    DY = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY )
    while DX and DY == 0:
        DX = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX )#how can we make  sure that the dx and dy are not 0
        DY = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY )
    RADIUS = random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
    COLOR = (random.random(), random.random() , random.random())
    new_ball = Ball(X,Y,DX,DY,RADIUS,COLOR)
    BALLS.append(new_ball)

# PART 1 

def move_balls(SCREEN_WIDTH,SCREEN_HEIGHT,BALLS):
    for ball in BALLS:
        ball.penup()
        random_place_x = random.randint(round(-SCREEN_WIDTH + RADIUS) , round(SCREEN_WIDTH-RADIUS))
        random_place_y = random.randint(round(-SCREEN_HEIGHT + RADIUS) , round(SCREEN_HEIGHT - RADIUS))
        ball.goto(random_place_x , random_place_y)

move_balls(SCREEN_WIDTH,SCREEN_HEIGHT,BALLS)


#PART 2

def collide(ball_a,ball_b):
    if ball_a.r == ball_b.r and ball_a.pos() == ball_b.pos():
        return False
    d = math.sqrt(math.pow(ball_a.xcor()-ball_b.xcor(),2)+math.pow(ball_a.ycor()-ball_b.ycor(),2))
    if d +10 <= ball_a.RADIUS + ball_b.RADIUS:
        return True 
    else:
         return False


#part 3

#def check_all_balls_collision():
    #for ball_a in [BALLS]:
        #for ball_b in [BALLS]:
            #if ball_a.collide(ball_a,ball_b)== True:
                #A_radius =  ball_a.RADIUS 
                #B_radius = ball_b.RADIUS
                
    #X_COORDINATE= random.randinit(-SCREEN_WIDTH + ball_a.RADIUS , SCREEN_WIDTH - a.RADIUS)
    #Y_COORDINATE= random.randinit(-SCREEN_HEIGHT + ball_a.RADIUS , SCREEN_HEIGHT - a.RADIUS)
    #X_AXISSPEED = random.randinit(                
    #Y_AXISSPEED = random.randinit(
    #Radius =random.randinit(
    #Color =  
    

    

    
        










                   





























  
            
        
        
        
        
