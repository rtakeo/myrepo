from math import sqrt
def distance( pointA, pointB ):
    x12Sq = (pointA[0] - pointB[0]) **2
    y12Sq = (pointA[1] - pointB[1])**2
    return sqrt(x12Sq + y12Sq)

p1 = (2,2)
p2 = (-2,-3)
print("Distance is {0:.2f}".format(distance(p1,p2)))