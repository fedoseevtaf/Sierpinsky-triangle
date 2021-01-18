#==============================================================#
filename = 'file.png'

size = 10

#==============================================================#
from pngclass import *

#==============================================================#
hieght = 2 ** size
width = hieght + 1

mypng = png(width, hieght)
mypng[(width - 2), 0].setcolor(0)

#==============================================================#
for y in range(1, mypng.hieght):
    for x in range((mypng.width - 2), (mypng.width - 3 - y), -1):

        n1 = mypng[x, (y - 1)].getcolor()
        n2 = mypng[(x + 1), (y - 1)].getcolor()
        newcolor = int(n1 == n2)

        mypng[x, y].setcolor(newcolor)

#==============================================================#
mypng.create(filename)
