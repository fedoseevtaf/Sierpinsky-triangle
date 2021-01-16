#==============================================================#
iterCount = 3000
width = 4

#==============================================================#
pos1 = 0, 200
pos2 = -200, -200
pos3 = 200, -200

#==============================================================#
from random import randint as random_int
import turtle as tp

#==============================================================#
tp.penup()
tp.left(90)
tp.speed(0)

#==============================================================#


class fractal_painter():
    def __init__(self):
        self.pos = [0, 0]


    def newpos(self):
        flag = random_int(1, 3)

        if flag == 1:
            self.pos[0] += pos1[0]
            self.pos[0] /= 2

            self.pos[1] += pos1[1]
            self.pos[1] /= 2

        elif flag == 2:
            self.pos[0] += pos2[0]
            self.pos[0] /= 2

            self.pos[1] += pos2[1]
            self.pos[1] /= 2


        elif flag == 3:
            self.pos[0] += pos3[0]
            self.pos[0] /= 2

            self.pos[1] += pos3[1]
            self.pos[1] /= 2

        else:
            raise ValueError('Module \"random\" does not work correctly!')


    def dot(self):
        tp.pendown()
        tp.width(width)
        tp.forward(1)
        tp.backward(1)
        tp.penup()


    def _2paint(self):
        count = iterCount
        
        while count > 0:
            tp.setx(self.pos[0])
            tp.sety(self.pos[1])
            
            self.newpos()
            self.dot()
            
            count -= 1


myfractal = fractal_painter()
myfractal._2paint()
