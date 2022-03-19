def pointCentered(p,r=5):
    """draws point centered around p with radius r"""
    x,y = p
    oval(x-r,y-r,r*2,r*2)
    
def pointFromPoints(p,r=5,numpoints=100):
    """draw a point from points constructed geometrically
    (potential for drawing with random etc)"""
    from math import sin,cos,pi
    x,y = p
    points = []
    for i in range(numpoints):
        rad = i*2*pi/numpoints
        points.append((x+cos(rad)*r,y+sin(rad)*r))
    polygon(*points)
    
def ovalFromPoints(p,w=10,h=5,tf_angle=0,numpoints=100):
    """draw an oval from points constructed geometrically
    width, height, transformation angle in radians
    (potential for drawing with random etc)"""
    from math import sin,cos,pi
    x0,y0 = p
    points = []
    tf_sin = sin(tf_angle)
    tf_cos = cos(tf_angle)
    for i in range(numpoints):
        rad = i*2*pi/numpoints
        x1 = cos(rad)*(w/2) #without transformation and around (0,0)
        y1 = sin(rad)*(h/2)
        x = x1*tf_cos - y1*tf_sin #transformation
        y = x1*tf_sin + y1*tf_cos
        points.append((x+x0,y+y0))
    polygon(*points)

def ovalRotated(p,w=10,h=5,angle=0):
    """oval with optional rotation"""
    x,y = p[0]-w/2, p[1]-h/2
    path = BezierPath()
    path.oval(x,y,w,h)
    path.rotate(angle,p)
    drawPath(path)