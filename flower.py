from turtle import *
import colorsys

speed(0)
bgcolor("black")
for j in range(16):
    begin_fill()
    pencolor("white")
    for z in range(9):
        c  = colorsys.hsv_to_rgb(j / 19, z / 10, 1)
        color(c)
        circle(300 - 15 * z, 70)
        lt(110)
        circle(300 - 15 * z, 70)
        lt(110)
    end_fill()
    lt(75)
    fd(20)
    rt(52.5)
done()
