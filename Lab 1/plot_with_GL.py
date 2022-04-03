from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from line import line_dda, line_bla
from circle import circle_midpoint
from piechart import piechart

def plot_points(points):
    glBegin(GL_POINTS)
    for point in points:        
        glVertex2f(point[0], point[1])        
    glEnd()


def plot_line(line):
    glBegin(GL_LINES)        
    glVertex2f(line[0], line[1])        
    glVertex2f(line[2], line[3])        
    glEnd()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Remove everything from screen (i.e. displays all white)
    glLoadIdentity() # Reset all graphic/shape's position
    iterate()

    plot_points(line_dda(x1=20, y1=30, x2=200, y2=500)) # Draw line using DDA
    plot_points(line_dda(x1=0, y1=30, x2=500, y2=300)) # Draw line using DDA

    plot_points(line_bla(x1=20, y1=10, x2=300, y2=400)) # Draw line using BLA
    plot_points(line_bla(x1=20, y1=10, x2=500, y2=350)) # Draw line using BLA
    
    plot_points(circle_midpoint(xc=300, yc=300, r=100)) # Draw circle using midpoint algorithm
    plot_points(circle_midpoint(xc=200, yc=200, r=50)) # Draw circle using midpoint algorithm

    # Draw piechart
    circle_points, lines = piechart(xc=200, yc=300, r=200, data=[5, 15, 25, 30, 65]) 
    plot_points(circle_points)
    for line in lines:
        plot_line(line)

    glColor3f(1.0, 0.0, 3.0) # Set the color to pink
    glutSwapBuffers()


glutInit() # Initialize a glut instance which will allow us to customize our window
glutInitDisplayMode(GLUT_RGBA) # Set the display mode to be colored
glutInitWindowSize(500, 500)   # Set the width and height of your window
glutInitWindowPosition(0, 0)   # Set the position at which this windows should appear
wind = glutCreateWindow("Lines, Circle and Piechart using OpenGL") # Give your window a title
glutDisplayFunc(showScreen)  # Tell OpenGL to call the showScreen method continuously
glutIdleFunc(showScreen)     # Draw any graphics or shapes in the showScreen function at all times
glutMainLoop()  # Keeps the window created above displaying/running in a loop