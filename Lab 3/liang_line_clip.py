from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def liang_barsky(line, clipping_window):
    xmin, xmax, ymin, ymax = (clipping_window[i] for i in ('xmin','xmax','ymin','ymax'))
    start, end = (line[i] for i in ('start', 'end'))

    x1, y1 = start
    x2, y2 = end
    
    dx = x2 - x1
    dy = y2 - y1

    ps = []
    qs = []
    ps.append(-dx)
    ps.append(dx)
    ps.append(-dy)
    ps.append(dy)
    qs.append(x1 - xmin)
    qs.append(xmax - x1)
    qs.append(y1 - ymin)
    qs.append(ymax - y1)

    r = []
    for i in range(4):
        if ps[i] != 0:
            r.append(qs[i] / ps[i])
        else:
            r.append(None)
    r1s = [0]
    r2s = [1]
    for i in range(4):
        if ps[i]<0:
            r1s.append(r[i])
        elif ps[i]>0:
            r2s.append(r[i])
        else:            
            if qs[i]<0:                
                return None   
            else:
                print("parallel and inside")

    u1 = max(r1s)
    u2 = min(r2s)

    if u1 < u2:
        if u1>=0:
            new_x1 = x1 + u1 * dx
            new_y1 = y1 + u1 * dy
            line["start"] = [new_x1, new_y1]
        if u2<=1:
            new_x2 = x1 + u2 * dx
            new_y2 = y1 + u2 * dy
            line["end"] = [new_x2, new_y2]
        
        return line
    else:
        return None
choice = 0
clipping_window = {
        "xmin": -300.0,
        "xmax": 300.0,
        "ymin": -200.0,
        "ymax": 200.0
    }  
lines = {
        # intersecting with window
        "redLine": {
            "start": [-400.0, 400.0],
            "end": [400.0, -400.0],
            "color": [1, 0, 0]
        },
        "purpleLine": {
            "start": [-200.0, -300.0],
            "end": [-100.0, -150.0],
            "color": [128/255, 0, 128/255]
        },
        "orangeLine": {
            "start": [-200.0, -100.0],
            "end": [-400.0, 200],
            "color": [1, 69/255, 0]
        },
        "whiteLine": {
            "start": [-100, 300],
            "end": [-100, -300],
            "color": [1, 1, 1]
        },
        # inside window
        "yellowLine": {
            "start": [100.0, 100.0],
            "end": [150.0, -100.0],
            "color": [1, 1, 0]
        },
        # outside window
        "blueLine": {
            "start": [-450.0, 200.0],
            "end": [-400.0, -300.0],
            "color": [0, 0.5, 1]
        }
    }
def setup():
    glClearColor(0, 0, 0, 1)
    glColor3fv([0.2, 0.5, 0.4])
    glPointSize(10.0)
    gluOrtho2D(-500, 500, -500, 500)

def menu(option):
    global choice
    choice = option
    glutPostRedisplay()
    return choice

def createMenu():
    glutCreateMenu(menu)
    glutAddMenuEntry("Red Line", 1)
    glutAddMenuEntry('Purple Line', 2)
    glutAddMenuEntry('Orange Line', 3)
    glutAddMenuEntry('Yellow Line', 4)
    glutAddMenuEntry('Blue Line', 5)
    glutAddMenuEntry('White Line', 6)
    glutAttachMenu(GLUT_RIGHT_BUTTON)

def draw_axis():
    glColor3f(1, 1, 1)
    glBegin(GL_LINES)
    glVertex2f(0, -500)
    glVertex2f(0, 500)
    glVertex2f(-500, 0)
    glVertex2f(500, 0)
    glEnd()

def draw_clipping_window(clipping_window):
    xmin, xmax, ymin, ymax = (clipping_window[i]
                              for i in ('xmin', 'xmax', 'ymin', 'ymax'))
    glColor3f(0, 1, 0)
    glBegin(GL_LINES)

    glVertex2f(xmin, ymin)
    glVertex2f(xmax, ymin)

    glVertex2f(xmax, ymin)
    glVertex2f(xmax, ymax)

    glVertex2f(xmax, ymax)
    glVertex2f(xmin, ymax)

    glVertex2f(xmin, ymax)
    glVertex2f(xmin, ymin)

    glEnd()

def draw_default(clipping_window):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_axis()
    draw_clipping_window(clipping_window)

def draw_line(line):
    if line:
        start, end, color = (line[i] for i in ('start', 'end', 'color'))
        glColor3fv(color)
        glBegin(GL_LINES)
        glVertex2fv(start)
        glVertex2fv(end)
        glEnd()

def draw_lines(lines):
    for i in lines:
        draw_line(lines[i])

def draw_clipped_line(choice, lines, clipping_window):
    redLine, purpleLine, orangeLine, yellowLine, blueLine, whiteLine = (lines[i] for i in (
        'redLine', 'purpleLine', 'orangeLine', 'yellowLine', 'blueLine', 'whiteLine'))
    if choice == 1:
        draw_default(clipping_window)
        if redLine:
            lines["redLine"] = liang_barsky(redLine, clipping_window)
    elif choice == 2:
        draw_default(clipping_window)
        if purpleLine:
            lines["purpleLine"] = liang_barsky(purpleLine, clipping_window)
    elif choice == 3:
        draw_default(clipping_window)
        if orangeLine:
            lines["orangeLine"] = liang_barsky(orangeLine, clipping_window)
    elif choice == 4:
        draw_default(clipping_window)
        if yellowLine:
            lines["yellowLine"] = liang_barsky(yellowLine, clipping_window)
    elif choice == 5:
        draw_default(clipping_window)
        if blueLine:
            lines["blueLine"] = liang_barsky(blueLine, clipping_window)
    elif choice == 6:
        draw_default(clipping_window)
        if whiteLine:
            lines["whiteLine"] = liang_barsky(whiteLine, clipping_window)
    draw_lines(lines)

def display():
    global choice, lines, clipping_window
    glClear(GL_COLOR_BUFFER_BIT)    

    draw_default(clipping_window)
    draw_lines(lines)

    draw_clipped_line(choice, lines, clipping_window)
    
    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(800, 800)
glutInitWindowPosition(350, 0)
glutCreateWindow("Liang Barsky Line Clipping using OpenGL")
setup()
createMenu()
glutDisplayFunc(display)
glutMainLoop()
