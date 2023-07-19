import turtle
import tkinter

wn = turtle.Screen()
wn.title('My Turtle Baby')

#------------
peter = turtle.Turtle()
peter.speed(1)

peter.left(90)
peter.forward(-200)
peter.left(90)
peter.shape('circle')
peter.forward(200)
peter.right(90)
peter.shape('turtle')
peter.forward(400)
peter.right(90)
peter.shape('square')
peter.forward(200)
peter.right(90)
peter.shape('triangle')
peter.forward(200)
peter.left(90)
peter.shape('turtle')
peter.forward(250)
peter.speed(7)
for x in range(5):
    peter.home()
    peter.forward(250)
peter.home()
peter.up()
peter.setpos(60,30)
peter.home()
peter.left(180)
peter.pendown()
peter.speed(4)
peter.color('red')
peter.stamp()
peter.color('black')
peter.forward(200)
peter.up()
peter.sety(300)
peter.setx(260)
peter.setpos(-50.00,90.00)
peter.home()
peter.down()
peter.pensize(2)
peter.color('red')
for p in range(5):
    peter.circle(50)
    peter.circle(50 + p)
peter.degrees(45)
peter.forward(200)

#wn.exitonclick()
turtle.done()
#------------




##wn.bgcolor('black')
#global alex 
#wn = tkinter.Canvas(width=500, height=500)
#screen = turtle.Screen()
#scr_canvas = turtle.ScrolledCanvas(canvas)

'''
#========
screen.setup(width=500, height=500)
screen.bgcolor("gray")

turtle.shape("circle")
turtle.color("blue")
turtle.speed(5)

turtle.circle(100)
#========
'''

'''
alex = turtle.Turtle()
alex.color('red')
alex.pensize(2)

tess = turtle.Turtle()
tess.color('red')
tess.pensize(2)
tess.shape('turtle')
##tess.shape('classic')

elan = turtle.Turtle()
elan_colors = ['red','dark red']
#wn.bgcolor('orange')
##wn.bgcolor('black')

distance = 2
angle = 90
'''

"""
alex.forward(250)
alex.left(90)
alex.forward(250)
alex.left(90)
alex.forward(250)
alex.left(90)
alex.forward(250)
"""
#for number in range(400):
#    alex.forward(number+1)
#    alex.right(89)
#    alex.pencolor(colors[number%2])
'''
def spiderweb():
    colors = ['red','dark red']
    for number in range(50):
        alex.forward(number+1)
        alex.right(89)
        alex.pencolor(colors[number%2])

alex.color('white')
alex.pensize(3)
alex.left(180)
alex.forward(150)
alex.right(90)
alex.forward(100)

spiderweb()

alex.color('white')
alex.left(130)
alex.forward(80)

spiderweb()

alex.color('white')
alex.right(130)
alex.forward(80)
'''
'''
def alex_turtle():
    alex.forward(100)
    alex.left(90)
    alex.forward(100)
    alex.left(90)
    alex.forward(100)
    alex.left(90)
    tess_turtle()
    alex.forward(100)
    alex.left(90)
    for x in range(10):
        alex.forward(100+x)
        alex.left(90)

def tess_turtle():
    tess.forward(80)  
    tess.left(120)     
    tess.forward(80)
    tess.left(120)
    tess.forward(80)
    tess.left(120)
    tess.right(180)
    tess.forward(80)
    tess.left(90)
    for y in range(10):
        tess.forward(100+y)
        tess.right(90)
'''
        
#alex_turtle()
#tess_turtle()
#alex_turtle()

'''
for _ in range(200):
    elan.forward(distance)
    elan.right(angle)
    distance = distance + 2
    elan.pencolor(elan_colors[_%2])
    angle = angle + 1
'''

'''
tess.up()
for _ in range(150):
    tess.stamp()
    tess.forward(distance)
    tess.right(24)
    distance = distance + 1

tess.color('blue')
#tess.down()
for _ in range(150):
    tess.left(24)
    tess.backward(distance)
    tess.stamp()
    distance = distance -1

'''
#screen.exitonclick()

#wn.exitonclick()
#turtle.done()
