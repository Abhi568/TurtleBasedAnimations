import turtle
t = turtle.Turtle()
w = turtle.Screen()
w.bgpic("image.gif")
t.color("yellow","green")
t.pensize(2)
t.speed(1)
t.begin_fill()
t.forward(100)
t.left(135)
t.forward(70)
t.left(90)
t.forward(70)
t.fillcolor("red")

t.end_fill()

t.left(225)
t.up()
#t.forward(50)
t.goto(-75,50)
t.down()
t.right(90)
t.begin_fill()
t.forward(250)
t.left(120)
t.forward(255)
t.left(120)
t.forward(255)
t.fillcolor("orange")
t.end_fill()

#for circles
t.begin_fill()
t.circle(48, 180)
t.left(238)
t.fillcolor("wheat")
t.end_fill()
t.begin_fill()
t.circle(55, 122)
t.left(225)
t.fillcolor("blue")
t.end_fill()
t.begin_fill()
t.circle(45, 220)
t.fillcolor("purple")
t.end_fill()





    
