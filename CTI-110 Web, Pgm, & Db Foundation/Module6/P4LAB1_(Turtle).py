import turtle

pn = turtle.Turtle()

pn.color('black','blue')    
pn.begin_fill()  
pn.forward(60) 
pn.right(90)
pn.forward(20)
pn.right(90)
pn.forward(20)
pn.left(90)
for i in range(6):
    pn.forward(10)
pn.right(90)
for i in range(5):
    pn.forward(10)
pn.right(90)
pn.forward(30)
pn.right(90)
pn.forward(10)
pn.right(90)
pn.forward(10)
pn.left(90)
pn.forward(20)
pn.left(90)
for i in range(4):
    pn.forward(10)
pn.left(90)
pn.forward(20)
pn.right(90)
pn.forward(20)
pn.end_fill()

pn.right(90)
pn.penup()
pn.color('black','red')
pn.begin_fill()
pn.forward(80)
pn.pendown()
for i in range(7):
    pn.forward(10)
pn.right(90)
for i in range(8):
    pn.forward(10)
pn.right(90)
pn.forward(20)
pn.right(90)
pn.forward(60)
pn.left(90)
pn.forward(10)
pn.left(90)
pn.forward(40)
pn.right(90)
pn.forward(10)
pn.right(90)
pn.forward(40)
pn.left(90)
pn.forward(10)
pn.left(90)
pn.forward(60)
pn.right(90)
pn.forward(20)
pn.right(90)
pn.forward(80)
pn.end_fill()
   
    

    




turtle.done()