import turtle

# Function to draw a petal
def draw_petal(t, radius):
    for _ in range(2):
        t.circle(radius, 60)
        t.left(120)
        t.circle(radius, 60)
        t.left(120)

# Function to draw the flower
def draw_flower(t, num_petals, radius):
    for _ in range(num_petals):
        draw_petal(t, radius)
        t.left(360 / num_petals)

# Function to draw the stem
def draw_stem(t, length):
    t.right(90)
    t.forward(length)

# Function to draw a leaf
def draw_leaf(t, leaf_length):
    t.begin_fill()
    t.circle(leaf_length, 90)
    t.left(90)
    t.circle(leaf_length, 90)
    t.end_fill()

# Main drawing
screen = turtle.Screen()
screen.bgcolor("white")

rose = turtle.Turtle()
rose.speed(5)
rose.color("red", "red")  # Outline color and fill color

# Draw the flower
rose.begin_fill()
draw_flower(rose, 6, 100)  # 6 petals
rose.end_fill()

# Draw the stem
rose.color("green")
rose.penup()
rose.goto(0, -10)
rose.pendown()
draw_stem(rose, 200)

# Draw the leaves
rose.left(45)
draw_leaf(rose, 60)
rose.right(90)
rose.penup()
rose.goto(0, -110)
rose.pendown()
draw_leaf(rose, 60)

turtle.done()
