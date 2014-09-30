#http://studio.code.org/s/1/level/25

from random import random
from turtle import Turtle

def color_random():
    return (random(),random(),random())

llama= Turtle()
llama.color(color_random())
llama.pensize(10)
llama.forward(100)
llama.right(120)
llama.forward(100)
llama.right(120)
llama.forward(100)
llama.right(120)
llama.forward(100)
