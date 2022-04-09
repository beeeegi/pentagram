import turtle
 
pen = turtle.Turtle()
screen = turtle.Screen()

screen.bgcolor('black')
screen.setup(800, 600)

pen.pensize(4)
pen.hideturtle()

for i in range(5):
  pen.pencolor('red')
  pen.forward(200)
  pen.right(144)
pen.up()
pen.setposition(100, -160)
pen.down()
pen.circle(125)



turtle.done()