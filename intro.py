import turtle

a = 5
print(a)

b = "hello"
print(b)

credit_card = 123456789012
print(credit_card)

# this is a square
ant_turtle = turtle.Turtle()

# function that makes square
def square():
    ant_turtle.forward(100)
    ant_turtle.right(90)
    ant_turtle.forward(100)
    ant_turtle.right(90)
    ant_turtle.forward(100)
    ant_turtle.right(90)
    ant_turtle.forward(100)

# function call
square()
ant_turtle.forward(200)
square()