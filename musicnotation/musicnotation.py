# LINE SYSTEM

def noteSystem(start,x_len=100,y_space=10,sw=0,numlines=5):
    """draw note system from start points as bottom left
    for sw=0, strokeWidth is sqrt(y_space) / 3"""
    if sw == 0: sw = sqrt(y_space) / 3
    x1,y1 = start
    strokeWidth(sw)
    for i in range(numlines):
        x2 = x1+x_len
        line((x1,y1),(x2,y1))
        y1 += y_space


# CLEFS

def violinClef(start_system,y_space=10,sw=0,rnd=0):
    """start_system is bottom left
    rnd = 1 adds for each point of the bezier curve a maximal 
    deviation of -1 to 1 in x and y direction"""
    if sw==0: sw = sqrt(y_space) 
    strokeWidth(sw)
    fill(None)
    x,y = start_system
    s = y_space
    p1 = (x+s*1.5,y+s/2)
    p2a,p2b,p2c = (x+s*2.2,y+s*3),(x+s*3.5,y),(x+s*2,y-s/4)
    p3a,p3b,p3c = (x+s,y-s/2),(x+s*.7,y),(x+s,y+s)
    p4a,p4b,p4c = (x+s*2,y+s*3),(x+s*2.1,y+s*3.5),(x+s*2.2,y+s*4.5)
    p5a,p5b,p5c = (x+s*2,y+s*5.5),(x+s*1.3,y+s*5),(x+s*1.4,y+s*4)
    p6a,p6b,p6c = (x+s*1.7,y+s*2),(x+s*1.5,y+s),(x+s*1.8,y-s)
    p7a,p7b,p7c = (x+s*1.6,y-s*2),(x+s*1.4,y-s*1.5),(x+s*1.6,y-s*1.1)
    
    from random import uniform
    p = [p2a,p2b,p2c,p3a,p3b,p3c,p4a,p4b,p4c,p5a,p5b,p5c,p6a,p6b,p6c,p7a,p7b,p7c]
    for i in range(len(p)):
        old = p[i]
        new = (x+uniform(-rnd,rnd) for x in old)
        p[i] = new
    
    path = BezierPath()
    path.moveTo(p1)
    path.curveTo(p[0],p[1],p[2])
    path.curveTo(p[3],p[4],p[5])
    path.curveTo(p[6],p[7],p[8])
    path.curveTo(p[9],p[10],p[11])
    path.curveTo(p[12],p[13],p[14])
    path.curveTo(p[15],p[16],p[17])
    drawPath(path)

def bassClef(start_system,y_space=10,sw=0,rnd=0):
    """start_system is bottom left
    rnd = 1 adds for each point of the bezier curve a maximal 
    deviation of -1 to 1 in x and y direction"""
    from random import uniform
    if sw==0: sw = sqrt(y_space) 
    strokeWidth(sw)
    x,y = start_system
    sp = y_space
    oval(x+sp*.5,y+sp*2.8,sp*.4,sp*.4)
    oval(x+sp*2.4,y+sp*3.4,sp*.1,sp*.1)
    oval(x+sp*2.4,y+sp*2.5,sp*.1,sp*.1)
    fill(None)
    path = BezierPath()
    path.moveTo((x+sp*.5,y+sp*3))
    p1 = (x+sp*1.8+uniform(-rnd,rnd),y+sp*5.5+uniform(-rnd,rnd))
    p2 = (x+sp*2.5+uniform(-rnd,rnd),y+sp*1.5+uniform(-rnd,rnd))
    p3 = (x+sp*.5+uniform(-rnd,rnd),y+sp*.5+uniform(-rnd,rnd))
    path.curveTo(p1,p2,p3)
    drawPath(path)


# NOTE HEADS

def note(p,y_space=10):
    """draw a note as transformed oval
    p adjusts the middle point
    """
    x,y = p
    w = y_space
    h = w * .7
    x -= w/2
    y -= h/2
    angle = 35
    path = BezierPath()
    path.oval(x,y,w,h)
    path.rotate(angle,p)
    drawPath(path)

def noteDiamond(p,y_space=10):
    """p adjusts middle point"""
    x,y = p
    w,h = y_space*.8, y_space*.8
    line((x-w/2,y),(x,y+h/2))
    line((x,y+h/2),(x+w/2,y))
    line((x+w/2,y),(x,y-h/2))
    line((x,y-h/2),(x-w/2,y))


# AKCIDENTS

def accNatural(note,y_space=10,sw=0):
    """accidental natural"""
    if sw==0: sw = sqrt(y_space)/2
    strokeWidth(sw)
    x,y = note[0]-y_space/2, note[1]-y_space/2
    line((x-y_space*1.3,y+y_space*2),(x-y_space*1.3,y-y_space*.1))
    line((x-y_space*.5,y+y_space*1.2),(x-y_space*.5,y-y_space))
    line((x-y_space*1.3,y+y_space*.8),(x-y_space*.5,y+y_space*1.1))
    line((x-y_space*1.3,y-y_space*.1),(x-y_space*.5,y+y_space*.2))

def accSharp(note,y_space=10,sw=0):
    """accidental sharp"""
    if sw==0: sw = sqrt(y_space)/2
    strokeWidth(sw)
    x,y = note[0]-y_space*1.3-y_space/2, note[1]
    line((x,y-y_space),(x,y+y_space))
    line((x+y_space*.5,y-y_space),(x+y_space*.5,y+y_space))
    line((x-y_space*.3,y+y_space*.1),(x+y_space*.8,y+y_space*.7))
    line((x-y_space*.3,y-y_space*.7),(x+y_space*.8,y-y_space*.1))

def accFlat(note,y_space=10,sw=0):
    """accidental flat"""
    if sw==0: sw = sqrt(y_space)/2
    strokeWidth(sw)
    x,y = note[0]-y_space*1.7,note[1]-y_space*.5
    fill(None)
    path = BezierPath()
    path.moveTo((x,y-y_space*.1))
    path.lineTo((x,y+y_space*2))
    path.moveTo((x,y-y_space*.1))
    path.curveTo((x+y_space,y+y_space*.5),(x+y_space,y+y_space*1.5),(x,y+y_space*.7))
    drawPath(path)

