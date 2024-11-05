from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def display():
    glutSwapBuffers()

glutInit()
window = glutCreateWindow("OpenGL")
glutDisplayFunc(display)
glutMainLoop()