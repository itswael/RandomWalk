import random
import turtle as t

tim = t.Turtle()
colors = ["aquamarine", "teal", "wheat", "lime", "hot pink", "salmon"]
tim.pensize(15)
turns = [0, 90, 180, 270]
t.colormode(255)

for _ in range(200):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    tim.color(color)
    tim.setheading(random.choice(turns))
    tim.forward(50)