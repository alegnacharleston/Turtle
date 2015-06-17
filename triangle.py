import turtle
for i in range(10, 95, 5):
    turtle.fd(i)
    turtle.left(120)
    if i> 96:
        raw_input("Press enter to terminate")
