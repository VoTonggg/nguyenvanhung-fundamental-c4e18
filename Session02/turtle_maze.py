from turtle import *

speed(-1)
shape("turtle")

length = 5
for i in range(80):
    forward(length)
    left(90)

    length += 5

mainloop()

