"""
Rozwiązania do laboratorium 1 z Obrazowania Biomedycznego.
"""
import numpy as np
from obpng import write_png

"""
3 - Kwadrat
"""
#start[1] = y, start[0] = x
def square(size, side, start):
    mainSquare = (size, size)
    image = np.zeros(mainSquare).astype(np.uint8)
    image.fill(128)    
    image[start[1]:start[1] + side, start[0]:start[0] + side] = 64
    write_png(image, 'results/1_square.png')    

square(512,128,(32,64))

"""
3 - Koło
"""
def midcircle(size):
    mainSquare = (size[0], size[1])
    image = np.zeros(mainSquare).astype(np.uint8)
    image.fill(128)

    radius = 0;
    divider = 4
    if size[0] < size[1]:
        radius = size[0] / divider
    else:
        radius = size[1] / divider

    xCenter = size[0] / 2
    yCenter = size[1] / 2

    radius = int(radius)
    xCenter = int(xCenter)
    yCenter = int(yCenter)

    for x in range (xCenter - radius, xCenter + radius):
        for y in range (yCenter - radius, yCenter + radius):
            value = (x - xCenter)**2 + (y - yCenter)**2 <= radius**2
            if value:
                image[x,y] = 64
    
    write_png(image, 'results/2_circle_2.png')
    
midcircle((256,512))

"""
3 - Szachownica.
"""
def checkerboard(size):
    pass

"""
4 - Interpolacja najbliższych sąsiadów.
"""
def nn_interpolation(source, new_size):
    pass

"""
5 - Interpolacja dwuliniowa

"""
def bilinear_interpolation(source, new_size):
    pass
