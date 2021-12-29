import  turtle              # Nos permite usar tortugas 
def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
           koch(t, order-1, size/3)
           t.left(angle)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue","red")
tess.pensize(2)
tess.speed(9)
size = 100
tess.left(180)
tess.penup()
tess.forward(9*size)
tess.left(90)
tess.forward(3*size)
tess.right(270)
tess.pendown()
koch(tess,7,30000)
wn.mainloop()