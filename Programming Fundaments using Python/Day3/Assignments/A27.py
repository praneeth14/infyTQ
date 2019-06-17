import turtle  # allows us to use the turtles library

wn = turtle.Screen()  # creates a graphics window
wn.setup(500, 500)  # set window dimension

alex = turtle.Turtle()  # create a turtle named alex
alex.shape("turtle")  # alex looks like a turtle

alex.color("green")
# draws circles
for counter in range(1, 5):
    alex.circle(15 * counter)
alex.color("red")
alex.left(120)
for counter in range(1, 5):
    alex.circle(15 * counter)
alex.color("blue")
alex.left(120)
for counter in range(1, 5):
    alex.circle(15 * counter)

# Write the logic to create the given pattern
# Refer the statements given above to draw the pattern
