import turtle

def draw_heart():
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.left(50)
    turtle.forward(160)
    turtle.circle(60, 200)
    turtle.right(140)
    turtle.circle(60, 200)
    turtle.forward(160)
    turtle.end_fill() 

def write_message(message):
    turtle.penup()
    turtle.goto(0, -220)
    turtle.color("black")
    turtle.pendown()
    turtle.hideturtle()
    turtle.write(message, align="center", font=("Arial", 50, "bold"))

def main():
    turtle.speed(1)
    turtle.bgcolor("white")

    # Draw heart
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    draw_heart()

    # Write message
    write_message("----Happy 25th Anniversary\n     Mom and Dad!-----")
    turtle.done()

if __name__ == "__main__":
    main()
    
