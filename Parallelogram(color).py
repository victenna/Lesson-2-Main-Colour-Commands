import turtle
t=turtle.Turtle()
turtle.bgcolor("violet")        
t.color("blue")
t.pensize(5)                

t.color('green','navy')
t.begin_fill()
t.forward(200)
t.rt(140)
t.forward(110)
t.rt(40)
t.fd(200)
t.rt(140)
t.fd(110)
t.hideturtle()
t.end_fill()

turtle.exitonclick()            # wait for a user click on the canvas
