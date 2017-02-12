import turtle

def drawFlower():
    
    window = turtle.Screen()
    window.bgcolor("blue")
    petals = 36
    rhombus = 45
    size = 60
    draw = turtle.Turtle()
    draw.shape("circle")
    draw.color("green")
    draw.speed(0)
    draw.setheading(270)
   
    for i in range(0,petals):
        oblique = True
        for x in range(0,4):
            draw.forward(size)
            if(oblique):
                draw.right(90-rhombus)
                oblique = False
            else:
                draw.right(90+rhombus)
                oblique = True
            draw.right(360/petals)
        draw.right(360/petals)
    draw.forward(size*5)
    
    window.exitonclick()

drawFlower()

# Find Output at https://github.com/shaikhsardar/TurtleDrawingPython/blob/master/TurtleSunflower.png
