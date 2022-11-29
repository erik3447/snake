from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# tail position (0.0)

snake_position = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in snake_position:
    new_segment = Turtle()
    new_segment.shape("square")
    new_segment.color("White")
    new_segment.penup()
    new_segment.goto(position)
    new_segment.penup()
    segments.append(new_segment)

game_on = True

while game_on:
    for all_segment in segments:
        all_segment.forward(20)


screen.exitonclick()
