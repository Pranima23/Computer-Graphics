def form_symmetry_points(x, y, points):
    points.append([x, y])
    points.append([x, -y])
    points.append([-x, y])
    points.append([-x, -y])
    points.append([y, x])
    points.append([y, -x])
    points.append([-y, x])
    points.append([-y, -x])


def update_center(xc, yc, points):
    for point in points:
        point[0] += xc
        point[1] += yc


def circle_midpoint(xc, yc, r):
   
    x = 0 # initial point of circle is (0, r)
    y = r
    points = []
    form_symmetry_points(x, y, points)

    P = []
    if type(r) == "float": # initial decision parameter
        P.append(5/4.0 - r)
    else:
        P.append(1 - r)

    # find coordinates of a point in first octant
    i = 0
    while (x < y):
        
        if P[i] < 0:
            x += 1
            P.append(P[i] + 2*x + 1)
        else:
            x += 1
            y -= 1
            P.append(P[i] + 2*x + 1 - 2*y)
        i += 1
        form_symmetry_points(x, y, points)

    update_center(xc, yc, points)
    return points