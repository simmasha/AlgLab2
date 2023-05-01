from classes import *

def Generation(N: int, M: int):
    Rectangles = []
    for i in range(N):
        x1 = 10*i
        y1 = 10*i
        x2 = 10*(2*N-i)
        y2 = 10*(2*N-i)
        Rectangles.append(Rectangle(x1, y1, x2, y2))

    Points = []
    p = 1
    q = 2

    for i in range(M):
        x = pow(p*i, 31 % (20*N))
        y = pow(q*i, 31 % (20*N))
        Points.append((Point(x, y)))

    return Rectangles, Points

