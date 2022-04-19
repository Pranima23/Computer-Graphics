from math import pow

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def form_symmetry_points(x, y, points):
    points.append([x, y])
    points.append([x, -y])
    points.append([-x, y])
    points.append([-x, -y])    

def update_center(xc, yc, points):
    for point in points:
        point[0] += xc
        point[1] += yc    

def ellipse_midpoint(xc, yc, rx, ry):
    
    # Starting point of ellipse
    x = 0
    y = ry
    points = [[x,y]]

    # For Region 1
    P1 = []
    P1.append(pow(ry, 2) - pow(rx, 2)*ry + pow(rx, 2)/4)
    i = 0    
    while 2*ry*ry*x <= 2*rx*rx*y:    
        if P1[i] < 0:
            x += 1            
            form_symmetry_points(x, y, points)
            P1.append(P1[i] + 2*pow(ry, 2)*x + pow(ry, 2))            
        else:
            x += 1
            y -= 1
            form_symmetry_points(x, y, points)
            P1.append(P1[i] + 2*pow(ry, 2)*x + pow(ry, 2) - 2*pow(rx, 2)*y)
        i+=1

    # For region 2
    P2 = []
    P2.append(pow(ry, 2)*pow((x+0.5), 2) + pow(rx, 2)*pow((y-1), 2) - pow(rx, 2)*pow(ry, 2))

    i = 0
    while (y> 0):
        if P2[i] < 0:
            x += 1
            y -= 1
            form_symmetry_points(x, y, points)
            P2.append(P2[i] + 2*pow(ry, 2)*x - 2* pow(rx, 2)*y + pow(rx, 2))
        else:
            y -= 1
            form_symmetry_points(x, y, points)
            P2.append(P2[i] - 2* pow(rx, 2)*y + pow(rx, 2)) 
        i+=1

    update_center(xc, yc, points)
    return points

def plot_points(points):
    glBegin(GL_POINTS)
    for point in points:        
        glVertex2f(point[0], point[1])        
    glEnd()

def setup():    
    gluOrtho2D(0, 500, 0, 500)

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1, 1, 1)
    plot_points(ellipse_midpoint(xc = 200, yc = 200, rx = 100, ry = 150))

    glFlush()

if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Ellipse using Midpoint Algorithm")

    setup()

    glutDisplayFunc(display) 
    glutMainLoop()    