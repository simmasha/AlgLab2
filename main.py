from classes import *
from EnumerationAlgorithm import *
from MapAlgorithm import *
from TreeAlgorithm import *
from datas import *

n = int(input())
Rectangles = []
if n != 0:
    for i in range(n):
        s = str(input())
        s = s.split(' ')
        Rectangles.append(Rectangle(int(s[0]), int(s[1]), int(s[2]), int(s[3])))

# print("Rectangles:")
# for i in range(n):
#     print("(", Rectangles[i].x1, Rectangles[i].y1, ")",
#           "(", Rectangles[i].x2, Rectangles[i].y2, ")")

m = int(input())
Points = []
if m != 0:
    for i in range(m):
        s = str(input())
        s = s.split(' ')
        Points.append(Point(int(s[0]), int(s[1])))


# print("Points:")
# for i in range(m):
#     print("(", Points[i].x, Points[i].y, ")")
# Rectangles, Points = Generation(1000, 10)


if len(Rectangles) != 0 and len(Points) != 0:
    RectanglesCompressed, PointsCompressed, X, Y = CoordinateCompressing(Rectangles, Points)
    Enumeration(Points, Rectangles)

    Map = Map(RectanglesCompressed, len(X), len(Y))
    RectanglesCounting(Map, PointsCompressed)
    print()
    solution(Rectangles, Points)