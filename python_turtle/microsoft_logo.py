"""
Developed by Pragati Sahu
Youtube Channel link
https://www.youtube.com/channel/codeatrandom/
"""
from turtle import *

colors =['#f65314','#7cbb00', '#ffbb00', '#00a1f1' ]
pos = [(0,0), (100,0), (0,-100), (100,-100)]
for (x,y), color in zip(pos,colors):
    up()
    goto(x,y)
    down()
    fillcolor(color)
    begin_fill()
    for i in range(4):
        forward(90)
        right(90)
    end_fill()