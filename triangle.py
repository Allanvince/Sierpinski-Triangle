from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import sys

LINE_LENGTH = 2.7
SCR_WIDTH = 800
SCR_HEIGHT = 800

current = "A"
generation = 0

# Define an array of colors for the triangles
TRIANGLE_COLORS = [
    (1.0, 0.0, 0.0, 1.0),  # Red
    (0.0, 1.0, 0.0, 1.0),  # Green
    (0.0, 0.0, 1.0, 1.0),  # Blue
    (1.0, 1.0, 0.0, 1.0),  # Yellow
    (1.0, 0.0, 1.0, 1.0),  # Magenta
    (0.0, 1.0, 1.0, 1.0)   # Cyan
]

def l_system_representation():
    global current, generation
    while generation < 8:
        next_gen = ""
        for char in current:
            if char == 'A':
                next_gen += "B-A-B"
            elif char == 'B':
                next_gen += "A+B+A"
            elif char in ['-', '+']:
                next_gen += char
        current = next_gen
        generation += 1

def draw():
    global current
    glClear(GL_COLOR_BUFFER_BIT)
    glPushMatrix()
    x = SCR_WIDTH / 24
    y = 0.0
    color_index = 0  # Index to iterate over the list of triangle colors
    for char in current:
        if char in ['A', 'B']:
            glColor4f(*TRIANGLE_COLORS[color_index])  # Set color from the array
            glLineWidth(2.0)
            glBegin(GL_TRIANGLES)
            glVertex2f(x, y)
            glVertex2f(x + LINE_LENGTH / 2, y + LINE_LENGTH)
            glVertex2f(x + LINE_LENGTH, y)
            glEnd()
            x += LINE_LENGTH
            color_index = (color_index + 1) % len(TRIANGLE_COLORS)  # Move to the next color
        elif char in ['-', '+']:
            glTranslatef(x, y, 0.0)
            x = 0.0
            y = 0.0
            angle = -60.0 if char == '-' else 60.0
            glRotatef(angle, 0.0, 0.0, 1.0)
    glPopMatrix()
    glutSwapBuffers()

def main():
    global current, generation
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE)
    glutInitWindowSize(SCR_WIDTH, SCR_HEIGHT)
    glutCreateWindow("Sierpinski Triangle")

    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutKeyboardFunc(lambda key, x, y: exit() if key == b'\x1b' else None)  # ESC key to exit

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, SCR_WIDTH, 0.0, SCR_HEIGHT)
    glMatrixMode(GL_MODELVIEW)

    l_system_representation()

    glutMainLoop()

if __name__ == "__main__":
    main()
