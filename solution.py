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
    print(image)

square(512,128,(32,64))

"""
3 - Koło
"""
def midcircle(size):
    pass

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
