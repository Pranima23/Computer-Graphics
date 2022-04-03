def line_dda(x1, y1, x2, y2):
    
    dx = x2 - x1 # total change in x
    dy = y2 - y1 # total change in y

    x = x1 # set (x, y) as initial point
    y = y1 

    if abs(dx) > abs(dy): # set number of steps to draw line from start to end point
        step_size = abs(dx)
    else:
        step_size = abs(dy)

    x_inc = dx / step_size # calculate increment factor for x 
    y_inc = dy / step_size # calculate increment factor for y

    points = []
    for i in range(0, step_size+1): 
        
        points.append([x, y]) # coordinates for a point in line
        x += x_inc # calculate next (x, y)
        y += y_inc 
    
    return points

def line_bla(x1, y1, x2, y2):
    
    x = x1 # set (x, y) as initial point
    y = y1 

    dx = x2 - x1 # total change in x
    dy = y2 - y1 # total change in y
    slope = dy / dx

    # |m| <= 1
    if abs(slope) <= 1:
        P = []
        P.append(2*dy - dx) # initial decision parameter

        points = []
        for i in range(0, dx+1):
            points.append([x, y])
            if P[i] < 0:
                x += 1
                P.append(P[i] + 2*dy)
            else:
                x += 1
                y += 1
                P.append(P[i] + 2*dy - 2*dx)
    # |m| > 1
    else:
        P = []
        P.append(2*dx - dy) # initial decision parameter

        points = []
        for i in range(0, dy+1):
            points.append([x, y]) # coordinates of a point in line
            if P[i] < 0:
                y += 1
                P.append(P[i] + 2*dx)
            else:
                x += 1
                y += 1
                P.append(P[i] + 2*dx - 2*dy)

    return points