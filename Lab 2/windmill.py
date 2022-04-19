from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

PI=3.14159
current_angle=0
step_angle=0.1

def drawWindblades():
    global current_angle, step_angle
    # Rotate object
    glPushMatrix()
    glTranslatef(250, 250, 0)
    glRotatef(current_angle, 0, 0, 1)
    current_angle += step_angle
    glTranslatef(-250, -250, 0)
    # First rotor blade
    glBegin(GL_TRIANGLES)
    glColor3f(1, 1, 1)
    glVertex2f(250,250)
    glVertex2f(185,150)
    glVertex2f(150,185)
    glEnd()
    # Second rotor blade
    glBegin(GL_TRIANGLES)
    glColor3f(1, 1, 1)
    glVertex2f(250,250)
    glVertex2f(220,360)
    glVertex2f(280,360)
    glEnd()
    # Third rotor blade
    glBegin(GL_TRIANGLES)
    glColor3f(1, 1, 1)
    glVertex2f(250,250)
    glVertex2f(370,230)
    glVertex2f(350,190)
    glEnd()
    glPopMatrix()

def drawStand():
    glBegin(GL_POLYGON)
    glColor3f(1, 0.5, 1)
    glVertex2f(150,0)
    glVertex2f(350,0)
    glVertex2f(250,280)
    
    glEnd()

def setup():
    glClearColor(0,0,0,1)
    gluOrtho2D(0,500,0,500)
    glMatrixMode(GL_PROJECTION)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)

    drawStand()
    drawWindblades()
  
    glFlush()
    glutSwapBuffers()
    glutPostRedisplay()

def idle():
    glutPostRedisplay()

def Menu(choice):
    global step_angle
    if choice==1:
        step_angle=0.4
    if choice==2:
        step_angle=0.1

if __name__=="__main__":
    glutInit()
    glutInitWindowSize(500,500)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutCreateWindow("WindMill")
    setup()
    glutCreateMenu(Menu)
    glutAddMenuEntry("Fast Speed",1)
    glutAddMenuEntry("Slow Speed",2)
    glutAttachMenu(GLUT_RIGHT_BUTTON)
    glutIdleFunc(idle)
    glutDisplayFunc(display)
    glutMainLoop()