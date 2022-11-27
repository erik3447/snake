from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

#tail position (0.0)

snake_head = Turtle()
snake_head.shape("square")
snake_head.color("White")
snake_head.penup()
snake_head.goto(0,0)
snake_head.penup()

snake_body = Turtle()
snake_body.shape("square")
snake_body.color("White")
snake_body.penup()
snake_body.goto(20,0)









screen.exitonclick()
