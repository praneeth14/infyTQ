import turtle

wn = turtle.Screen()  # creates a graphics window
wn.setup(540, 508)  # set window dimension

alex = turtle.Turtle()  # create a turtle named alex
alex.shape("turtle")  # alex looks like a turtle
alex.color("blue")  # alex has a color

# Provide different values and test your program
destination = "north"

if (destination == "south"):
    alex.right(90)
    alex.forward(220)
elif (destination == "north"):
    alex.left(90)
    alex.forward(220)
elif (destination == "east"):
    alex.forward(200)
elif (destination == "west"):
    alex.backward(200)
else:
    alex.write("Looks like you have typed a wrong destination")
