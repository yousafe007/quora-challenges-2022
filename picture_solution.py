
import math

def line_intersection(line1, line2):
    x1, x2, x3, x4 = line1[0][0], line1[1][0], line2[0][0], line2[1][0]
    y1, y2, y3, y4 = line1[0][1], line1[1][1], line2[0][1], line2[1][1]

    dx1 = x2 - x1
    dx2 = x4 - x3
    dy1 = y2 - y1
    dy2 = y4 - y3
    dx3 = x1 - x3
    dy3 = y1 - y3

    det = dx1 * dy2 - dx2 * dy1
    det1 = dx1 * dy3 - dx3 * dy1
    det2 = dx2 * dy3 - dx3 * dy2

    if det == 0.0:  # lines are parallel
        if det1 != 0.0 or det2 != 0.0:  # lines are not co-linear
            return None  # so no solution

        if dx1:
            if x1 < x3 < x2 or x1 > x3 > x2:
                return math.inf  # infinitely many solutions
        else:
            if y1 < y3 < y2 or y1 > y3 > y2:
                return math.inf  # infinitely many solutions

        if line1[0] == line2[0] or line1[1] == line2[0]:
            return line2[0]
        elif line1[0] == line2[1] or line1[1] == line2[1]:
            return line2[1]

        return None  # no intersection

    s = det1 / det
    t = det2 / det

    if 0.0 < s < 1.0 and 0.0 < t < 1.0:
        return x1 + t * dx1, y1 + t * dy1


def isRectangle(a, b, c, d):
    aby = a[1]-b[1]
    abx = a[0]-b[0]
    acy = a[1]-c[1]
    acx = a[0]-c[0]
    ady = a[1]-d[1]
    adx = a[0]-d[0]
    bcy = b[1]-c[1]
    bcx = b[0]-c[0]
    bdy = b[1]-d[1]
    bdx = b[0]-d[0]
    cdy = c[1]-d[1]
    cdx = c[0]-d[0]
    return ((aby*aby) + (abx*abx)) == ((cdy*cdy) + (cdx*cdx)) and ((acy*acy) + (acx*acx)) == ((bdy*bdy) + (bdx*bdx)) and ((ady*ady) + (adx*adx) == (bcy*bcy) + (bcx*bcx))


def isPerp(a, b, c, d):
    x1, y1 = (a[0]-b[0]), (a[1]-b[1])
    x2, y2 = (c[0]-d[0]), (c[1]-d[1])
    cross = (x1*x2)+(y1*y2)
    if(cross == 0):
        return True
    else:
        return False


points = []

num = input()
for i in range(int(num)):
    point = input().split()
    points.append(point)

coord = [int(p) for point in points for p in point]
points = [(coord[k], coord[k+1]) for k in range(0, len(coord), 2)]

print(points)

intersects = []

for i in points:
    for j in points:
        if(i != j):
            # line_intersection((i, j), (i, j))
            for k in points:
                for l in points:
                    if(k != l and k != i and k != j and l != i and k != i and isPerp(i, j, k, l)):
                        try:
                            intr = line_intersection((i, j), (k, l))
                            # print(i, j, k, l)

                            if(intr[0] >= 0 and intr[1] >= 0):
                                intersects.append(intr)
                        except:
                            pass

newlist = [ii for n, ii in enumerate(intersects) if ii not in intersects[:n]]

for i in newlist:
    points.append((int(i[0]), int(i[1])))

points = [ii for n, ii in enumerate(points) if ii not in points[:n]]

count = 0
for i in points:
    for j in points:
        if(i != j):
            # line_intersection((i, j), (i, j))
            for k in points:
                for l in points:
                    if(k != l and k != i and k != j and l != i and k != i and isPerp(i, j, k, l)):
                        try:
                            if(isRectangle(i, j, k, l)):
                                count = count+1
                        except:
                            pass

print('count:', count/int(num))

