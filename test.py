import numpy
from scipy import stats

def avg():
    speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
    x = numpy.mean(speed)
    print(x)
def med():
    speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
    y = numpy.median(speed)
    print(y)
def mod():
    speed = [15,20, 15, 30, 40, 20, 30, 55, 20, 45, 15]
    z= stats.mode(speed)
    print(z)
mod()
med()
avg()






