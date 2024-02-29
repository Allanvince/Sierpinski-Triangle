from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Edge:
    def __init__(self, start, end):
        self.start = start
        self.end = end

def clip_polygon(polygon_subject, polygon_clipping):
    result = []

    return result

def clipped_sierpinski_triangle(sierpinski_triangle):
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0) # Red color for the clipped triangle
    for point in sierpinski_triangle:
        glVertex2f(point.x, point.y)
    glEnd()

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    
    
    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 0.0, 1.0) 
    glVertex2f(0.0, 0.0)
    glVertex2f(25.0, 50.0)
    glVertex2f(50.0, 0.0)
    glEnd()
    
    
    glColor3f(0.0, 0.0, 0.0) 
    glLineWidth(2.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(10.0, 10.0)
    glVertex2f(40.0, 10.0)
    glVertex2f(40.0, 40.0)
    glVertex2f(10.0, 40.0)
    glEnd()
    glLineWidth(1.0)
    
    polygon_subject = [Point(0.0, 0.0), Point(25.0, 50.0), Point(50.0, 0.0)]
    polygon_clipping = [Point(10.0, 10.0), Point(40.0, 10.0), Point(40.0, 40.0), Point(10.0, 40.0)]
    sierpinski_triangle = clip_polygon(polygon_subject, polygon_clipping)
    
   
    clipped_sierpinski_triangle(sierpinski_triangle)
    
    glFlush()

def initialize():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, 50.0, 0.0, 50.0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Clipping Sierpinski Triangle")
    initialize()
    glutDisplayFunc(draw)
    glutMainLoop()

if __name__ == "__main__":
    main()
