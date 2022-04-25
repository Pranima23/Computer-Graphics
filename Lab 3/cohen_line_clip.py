from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def find_slope(line):
    x1 = line["start"][0]
    y1 = line["start"][1]
    x2 = line["end"][0]
    y2 = line["end"][1]
    m = (y2 - y1) / (x2 - x1)
    return m

def assign_region_code(x, y, clipping_window):
    xmin, xmax, ymin, ymax = (clipping_window[i] for i in ('xmin','xmax','ymin','ymax'))
    bit4 = str(1 if y>ymax else 0)
    bit3 = str(1 if y<ymin else 0)
    bit2 = str(1 if x>xmax else 0)
    bit1 = str(1 if x<xmin else 0)
    region_code = bit4 + bit3 + bit2 + bit1
    return region_code

def bit_and(code1, code2):
    result = ""
    for i, bit in enumerate(code1):
        result+=(str(int(code1[i]) & int(code2[i])))
    return result

def find_intersection_vertical(point, x, m):
    x1, y1 = point
    y = y1 + m * (x - x1)  
    return [x, y]
      
def find_intersection_horizontal(point, y, m):
    x1, y1 = point
    x = x1 + (y - y1) / m
    return [x, y]

def cohen_sutherland(line, clipping_window):
    xmin, xmax, ymin, ymax = (clipping_window[i] for i in ('xmin','xmax','ymin','ymax'))
    start, end = (line[i] for i in ('start', 'end'))

    x1, y1 = start
    x2, y2 = end

    # Assign region code
    start_region = assign_region_code(x1, y1, clipping_window)
    end_region = assign_region_code(x2, y2, clipping_window)

    if start_region == '0000' and end_region == '0000':
        return line
    elif bit_and(start_region, end_region) != '0000':
        return None
    else:
        m = find_slope(line)
        if start_region != '0000':            
            if x1 < xmin:
                new_start = find_intersection_vertical(start, xmin, m)
                line["start"] = new_start
                return cohen_sutherland(line, clipping_window)
            elif x1 > xmax:
                new_start = find_intersection_vertical(start, xmax, m)
                line["start"] = new_start
                return cohen_sutherland(line, clipping_window)
            elif y1 < ymin:
                new_start = find_intersection_horizontal(start, ymin, m)
                line["start"] = new_start
                return cohen_sutherland(line, clipping_window)
            elif y1 > ymax:
                new_start = find_intersection_horizontal(start, ymax, m)
                line["start"] = new_start
                return cohen_sutherland(line, clipping_window)                     
           
        elif end_region != '0000':
            if x2 < xmin:
                new_end = find_intersection_vertical(end, xmin, m)
                line["end"] = new_end
                return cohen_sutherland(line, clipping_window)
            elif x2 > xmax:
                new_end = find_intersection_vertical(end, xmax, m)
                line["end"] = new_end
                return cohen_sutherland(line, clipping_window)
            elif y2 < ymin:
                new_end = find_intersection_horizontal(end, ymin, m)
                line["end"] = new_end
                return cohen_sutherland(line, clipping_window)
            elif y2 > ymax:
                new_end = find_intersection_horizontal(end, ymax, m)
                line["end"] = new_end
                return cohen_sutherland(line, clipping_window)
    return cohen_sutherland(line, clipping_window)
    
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
    redLine, purpleLine, orangeLine, yellowLine, blueLine = (lines[i] for i in (
        'redLine', 'purpleLine', 'orangeLine', 'yellowLine', 'blueLine'))
    if choice == 1:
        draw_default(clipping_window)
        if redLine:
            lines["redLine"] = cohen_sutherland(redLine, clipping_window)
    elif choice == 2:
        draw_default(clipping_window)
        if purpleLine:
            lines["purpleLine"] = cohen_sutherland(purpleLine, clipping_window)
    elif choice == 3:
        draw_default(clipping_window)
        if orangeLine:
            lines["orangeLine"] = cohen_sutherland(orangeLine, clipping_window)
    elif choice == 4:
        draw_default(clipping_window)
        if yellowLine:
            lines["yellowLine"] = cohen_sutherland(yellowLine, clipping_window)
    elif choice == 5:
        draw_default(clipping_window)
        if blueLine:
            lines["blueLine"] = cohen_sutherland(blueLine, clipping_window)
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
glutCreateWindow("Cohen Sutherland Line Clipping using OpenGL")
setup()
createMenu()
glutDisplayFunc(display)
glutMainLoop()
