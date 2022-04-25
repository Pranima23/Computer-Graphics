from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

choice = 0
clipping_window = {
    "xmin": -300.0,
    "xmax": 300.0,
    "ymin": -200.0,
    "ymax": 200.0
    }

polygon = [
        [100.0, 100.0],
        [0.0, 400.0],
        [-100.0, 100.0],
        [-400.0, 0.0],
        [-100.0, -100.0],
        [0.0, -400.0],
        [100.0, -100.0],
        [400.0, 0.0],
]

def find_slope(start, end):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]
    m = (y2 - y1) / (x2 - x1)
    return m

def find_intersection_vertical(point, x, m):
    x1, y1 = point
    y = y1 + m * (x - x1)  
    return [x, y]
      
def find_intersection_horizontal(point, y, m):
    x1, y1 = point
    x = x1 + (y - y1) / m
    return [x, y]
    
def left_clipper(polygon, xmin):
    clipped_polygon = []
    for i in range(len(polygon)):
        first_v = polygon[i-1]
        second_v = polygon[i]
        
        first_vx = first_v[0]
        second_vx = second_v[0]
        print(first_v, second_v)
        if first_vx < xmin and second_vx > xmin:           
            print("first vertex outside, second vertex inside")
            m = find_slope(first_v, second_v)
            new_first = find_intersection_vertical(first_v, xmin, m)
            clipped_polygon.append(new_first)
            clipped_polygon.append(second_v)
        elif first_vx > xmin and second_vx > xmin:
            print("first vertex inside, second vertex inside")
            clipped_polygon.append(second_v)
        elif first_vx > xmin and second_vx < xmin:
            print("first vertex inside, second vertex outside")
            m = find_slope(first_v, second_v)
            new_second = find_intersection_vertical(second_v, xmin, m)
            clipped_polygon.append(new_second)
        elif first_vx < xmin and second_vx < xmin:
            print("first vertex outside, second vertex outside")
    return clipped_polygon

def right_clipper(polygon, xmax):       
    clipped_polygon = []
    for i in range(len(polygon)):
        first_v = polygon[i-1]
        second_v = polygon[i]        
        first_vx = first_v[0]
        second_vx = second_v[0]
        print(first_v, second_v)
        if first_vx > xmax and second_vx < xmax:           
            print("first vertex outside, second vertex inside")
            m = find_slope(first_v, second_v)
            new_first = find_intersection_vertical(first_v, xmax, m)
            clipped_polygon.append(new_first)
            clipped_polygon.append(second_v)
        elif first_vx < xmax and second_vx < xmax:
            print("first vertex inside, second vertex inside")
            clipped_polygon.append(second_v)
        elif first_vx < xmax and second_vx > xmax:
            print("first vertex inside, second vertex outside")
            m = find_slope(first_v, second_v)
            new_second = find_intersection_vertical(second_v, xmax, m)
            clipped_polygon.append(new_second)
        elif first_vx > xmax and second_vx > xmax:
            print("first vertex outside, second vertex outside")
    return clipped_polygon

def bottom_clipper(polygon, ymin):       
    clipped_polygon = []
    for i in range(len(polygon)):
        first_v = polygon[i-1]
        second_v = polygon[i]
        
        first_vy = first_v[1]
        second_vy = second_v[1]
        print(first_v, second_v)
        if first_vy < ymin and second_vy > ymin:           
            print("first vertex outside, second vertex inside")
            m = find_slope(first_v, second_v)
            new_first = find_intersection_horizontal(first_v, ymin, m)
            clipped_polygon.append(new_first)
            clipped_polygon.append(second_v)
        elif first_vy > ymin and second_vy > ymin:
            print("first vertex inside, second vertex inside")
            clipped_polygon.append(second_v)
        elif first_vy > ymin and second_vy < ymin:
            print("first vertex inside, second vertex outside")
            m = find_slope(first_v, second_v)
            new_second = find_intersection_horizontal(second_v, ymin, m)
            clipped_polygon.append(new_second)
        elif first_vy < ymin and second_vy < ymin:
            print("first vertex outside, second vertex outside")
    return clipped_polygon

def top_clipper(polygon, ymax):       
    clipped_polygon = []
    for i in range(len(polygon)):
        first_v = polygon[i-1]
        second_v = polygon[i]        
        first_vy = first_v[1]
        second_vy = second_v[1]
        print(first_v, second_v)
        if first_vy > ymax and second_vy < ymax:           
            print("first vertex outside, second vertex inside")
            m = find_slope(first_v, second_v)
            new_first = find_intersection_horizontal(first_v, ymax, m)
            clipped_polygon.append(new_first)
            clipped_polygon.append(second_v)
        elif first_vy < ymax and second_vy < ymax:
            print("first vertex inside, second vertex inside")
            clipped_polygon.append(second_v)
        elif first_vy < ymax and second_vy > ymax:
            print("first vertex inside, second vertex outside")
            m = find_slope(first_v, second_v)
            new_second = find_intersection_horizontal(second_v, ymax, m)
            clipped_polygon.append(new_second)
        elif first_vy > ymax and second_vy > ymax:
            print("first vertex outside, second vertex outside")
    return clipped_polygon     

def sutherland_hodgeman(polygon, clipping_window):
    xmin, xmax, ymin, ymax = (clipping_window[i] for i in ('xmin','xmax','ymin','ymax'))

    left_clipped = left_clipper(polygon, xmin)
    right_clipped = right_clipper(left_clipped, xmax)
    bottom_clipped = bottom_clipper(right_clipped, ymin)
    top_clipped = top_clipper(bottom_clipped, ymax)
    print(left_clipped)
    print(right_clipped)
    print(bottom_clipped)
    print(top_clipped)
    return top_clipped

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
    glutAddMenuEntry("Clip Polygon", 1)   
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
    glColor3f(1, 0.5, 1)

def draw_polygon(polygon):
    glBegin(GL_LINES)
    for i in range(len(polygon)):
        glVertex2fv(polygon[i-1])
        glVertex2fv(polygon[i])
    glEnd()

def draw_clipped_polygon(polygon, clipping_window):
    draw_default(clipping_window)
    draw_polygon(polygon)

def display():
    global choice, clipping_window, polygon
    glClear(GL_COLOR_BUFFER_BIT)

    draw_default(clipping_window)        

    draw_polygon(polygon)
    
    clipped_polygon = sutherland_hodgeman(polygon, clipping_window)   
    if choice==1: draw_clipped_polygon(clipped_polygon, clipping_window)
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(800, 800)
glutInitWindowPosition(350, 0)
glutCreateWindow("Sutherland Hodgeman Polygon Clipping using OpenGL")
setup()
createMenu()
glutDisplayFunc(display)
glutMainLoop()