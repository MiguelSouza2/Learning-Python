from turtle import *

screen = Screen()
t = Turtle()
t.speed(0)

a = 2
x = 1

def follow():
    # Pega posição atual
    cx, cy = t.position()
    
    # Ajusta a janela para ficar centrada no lápis
    screen.setworldcoordinates(cx - 100, cy - 100,
                               cx + 100, cy + 100)

for i in range(20):
    fx = 2**x
    t.goto(x, fx)
    t.write(f"({x}, {fx})", align="center", font=("Arial", 8))
    
    follow()
    x += 1
