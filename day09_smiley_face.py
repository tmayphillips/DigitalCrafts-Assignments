from graphics import *

win = GraphWin('Window 1',600,600)

center = Point(300,300)
eye_left = Point(250,250)
eye_right = Point(350,250)
mouth_left = Point(225,350)
mouth_right = Point(375,350)

# face
face = Circle(center,150)
face.setOutline('black')
face.setFill('yellow')
face.draw(win)

# eyes
left_eye = Circle(eye_left,25)
left_eye.setOutline('black')
left_eye.setFill('blue')
left_eye.draw(win)
right_eye = Circle(eye_right,25)
right_eye.setOutline('black')
right_eye.setFill('blue')
right_eye.draw(win)

# mouth
mouth = Line(mouth_left,mouth_right)
mouth.draw(win)

win.getMouse()
win.close()
