# Editado por 
# Kevin Valdez - A01254336
# Daniela Ruiz - A01254229
# Ximena López - A01254325
# Gustavo Betancourt - A01252532

from turtle import *
import turtle

from freegames import vector

def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

# Creamos la funcion para crear un circulo
def circle(start, end):
    """Draw circle from start to end."""

    t = turtle
    r = 50
    t.circle(r)


# Creamos la funcion para crear un rectangulo
def rectangle(start, end):
    """Draw rectangle from start to end."""

    t = turtle
 
    l = 100
    w = 50
    
    t.forward(l) 
    t.left(90) 
    
    t.forward(w) 
    t.left(90) 
    
    t.forward(l) 
    t.left(90) 
    
    t.forward(w) 
    t.left(90) 

# Creamos la funcion para crear un triangulo
def triangle(start, end):
    """Draw triangle from start to end."""

    t = turtle

    t.forward(100)
    t.left(120)

    t.forward(100)
    t.left(120)

    t.forward(100)
    t.left(120)

def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')

# Agregue el color rosa
onkey(lambda: color('pink'), 'P')

onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')

done()