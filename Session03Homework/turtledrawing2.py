from turtle import *

speed(-1)
shape("turtle")

colors = ["red", "blue", "brown", "yellow", "grey"]

for i in range(5):
    fillcolor(colors[i])
    
    begin_fill()

    right(90)
    forward(30)
    right(90)
    forward(100-i*20)
    right(90)
    forward(30)
    right(90)
    forward(100-i*20)

    end_fill()

mainloop()