from math import cos, sin, radians
import random
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

choice = 0

# def [1, 0.5, 1]:
#     for i in range(3):
#         r = random.randint(0,255)
#         g = random.randint(0,255)
#         b = random.randint(0,255)
#     return [r,g,b]

def matrix_multiplication(A, B):    
    result=[ [0]*len(B[0]) for i in range(len(A)) ]
    for i in range(0, len(A)):
        for j in range(0, len(B[0])):
            for k in range(0, len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result    

def draw_axis():    
    glBegin(GL_LINES)
    glVertex2f(0, -500)
    glVertex2f(0, 500)
    glVertex2f(-500, 0)
    glVertex2f(500, 0)
    glEnd()

def transform_triangle(choice, vertices_matrix):
    if choice == 1:
        translate_triangle(vertices_matrix, tx=-100, ty=-100) 
    elif choice == 2:
        rotate_triangle(vertices_matrix, theta=60)
    elif choice == 3:
        scale_triangle(vertices_matrix, sx=1, sy=2)
    elif choice == 4:
        reflect_triangle(vertices_matrix, axis='x')
    elif choice == 5:
        reflect_triangle(vertices_matrix, axis='y')
    elif choice == 6:
        reflect_triangle(vertices_matrix, axis='origin')
    elif choice == 7:
        reflect_triangle(vertices_matrix, axis='y=x')
    elif choice == 8:
        shear_triangle(vertices_matrix, axis='x', shx=0.5, shy=0)
    elif choice == 9:
        shear_triangle(vertices_matrix, axis='y', shx=0, shy=0.5)

def draw_triangle(vertices_matrix, color):
    glColor3fv(color)
    glBegin(GL_TRIANGLES) 
    glVertex2f(vertices_matrix[0][0], vertices_matrix[1][0]) 
    glVertex2f(vertices_matrix[0][1], vertices_matrix[1][1]) 
    glVertex2f(vertices_matrix[0][2], vertices_matrix[1][2]) 
    glEnd() 

def translate_triangle(vertices_matrix, tx, ty):   
    translation_matrix = [[1, 0, tx],
                          [0, 1, ty],
                          [0, 0, 1]]
    draw_triangle(matrix_multiplication(translation_matrix, vertices_matrix), [1, 1, 1])

def rotate_triangle(vertices_matrix, theta):
    rotation_matrix = [[cos(radians(theta)), -sin(radians(theta)), 0],
                        [sin(radians(theta)), cos(radians(theta)), 0],
                        [0, 0, 1]]
    draw_triangle(matrix_multiplication(rotation_matrix, vertices_matrix), [1, 1, 1])

def scale_triangle(vertices_matrix, sx, sy):
    scaling_matrix = [[sx, 0, 0],
                       [0, sy, 0],
                       [0, 0, 1]]
    draw_triangle(matrix_multiplication(scaling_matrix, vertices_matrix), [1, 1, 1])

def reflect_triangle(vertices_matrix, axis):
    if axis == 'x':
        reflection_matrix = [[1, 0, 0],
                             [0, -1, 0],
                             [0, 0, 1]]
    elif axis == 'y':
        reflection_matrix = [[-1, 0, 0],
                             [0, 1, 0],
                             [0, 0, 1]]
    elif axis == 'origin':
        reflection_matrix = [[-1, 0, 0],
                             [0, -1, 0],
                             [0, 0, 1]]
    elif axis == 'y=x':
        reflection_matrix = [[0, 1, 0],
                             [1, 0, 0],
                             [0, 0, 1]]
    draw_triangle(matrix_multiplication(reflection_matrix, vertices_matrix), [1, 1, 1])  

def shear_triangle(vertices_matrix, axis, shx, shy):
    if axis == 'x':
        shear_matrix = [[1, shx, 0],
                        [0, 1, 0],
                        [0, 0, 1]]
    if axis == 'y':
        shear_matrix = [[1, 0, 0],
                        [shy, 1, 0],
                        [0, 0, 1]]
    draw_triangle(matrix_multiplication(shear_matrix, vertices_matrix), [1, 1, 1])
                    
def setup():    
    gluOrtho2D(-500, 500, -500, 500)

def menu(option):
    global choice
    choice = option
    glutPostRedisplay()
    return choice

def createMenu():
    glutCreateMenu(menu)
    glutAddMenuEntry("Translate",1)
    glutAddMenuEntry('Rotate',2)
    glutAddMenuEntry('Scale',3)
    glutAddMenuEntry('Reflect-x',4)
    glutAddMenuEntry('Reflect-y',5)
    glutAddMenuEntry('Reflect-origin',6)
    glutAddMenuEntry('Reflect-y=x',7)
    glutAddMenuEntry('Shear-x',8)
    glutAddMenuEntry('Shear-y',9)
    glutAttachMenu(GLUT_RIGHT_BUTTON)

def display():
    global choice
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1, 1, 1)
    draw_axis()

    vertices_matrix = [[100.0, 300.0, 300.0],
                [100.0, 100.0, 200.0],
                [1, 1, 1]]
    color = [1, 1, 0.5]

    draw_triangle(vertices_matrix, color)    
    transform_triangle(choice, vertices_matrix)

    glFlush()

if __name__ == "__main__":    
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

    glutInitWindowSize(800, 800)
    glutInitWindowPosition(350, 0)
    glutCreateWindow("2D Transformations")

    createMenu()

    setup()

    glutDisplayFunc(display) 
    glutMainLoop()    