
 
from random import random
from turtle import Turtle

def color_random():
    return (random(),random(),random())

llama = Turtle()

while True:
   llama.color(color_random())
   llama.pensize(10)
   llama.forward(100)
   llama.right(120)
   llama.right(10)

   
