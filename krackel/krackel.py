def zittLine(p1,p2,amp=10,f=1/2,d=1/3):
    """p1 und p2 sind zwei punkte als (x,y)
    amp ist die maximale auslenkung in pixeln
    f ist die frequenz (1 = 2pi punkte als periode)
    d ist die mögliche abweichung von der frequenz
    bei f=1/2 und d=1/3 kann die frequenz zwischen 1/3 und 2/3 schwanken"""
    from random import random, uniform
    from math import sin, pi
    x1,y1 = p1
    x2,y2 = p2
    points_x = [x for x in range(round(x1),round(x2))]
    len_x = x2 - x1
    len_y = y2 - y1
    points = []
    x0 = points_x[0]
    f1,f2 = f-f*d,f+f*d
    for x in points_x:
        y = y1 + ((x-x1)/len_x) * len_y
        if floor((x-x0)%(2*pi/f))==0:
            rand = random()
            f = uniform(f1,f2)
            x0 = x
        y += sin((x-x0)*f) * amp * rand
        points.append((x,y))
    fill(None)
    polygon(*points,close=False)

def zittLineDotted(p1,p2,amp=10,f=1/2,d=1/3,dot=(10,20)):
    """p1 und p2 sind zwei punkte als (x,y)
    amp ist die maximale auslenkung in pixeln
    f ist die frequenz (1 = 2pi punkte als periode)
    d ist die mögliche abweichung von der frequenz
    bei f=1/2 und d=1/3 kann die frequenz zwischen 1/3 und 2/3 schwanken
    dot ist ein minimum und maximum in pixeln für die (schwarzen oder weissen) abschnitte"""
    from random import random, uniform, randint
    from math import sin, pi
    x1,y1 = p1
    x2,y2 = p2
    dot1,dot2 = dot
    points_x = [x for x in range(round(x1),round(x2))]
    len_x = x2 - x1
    len_y = y2 - y1
    points = []
    x0 = points_x[0]
    f1,f2 = f-f*d,f+f*d
    len_dots = randint(dot1,dot2)
    write_dots = 1
    dot_count = 0
    fill(None)
    for x in points_x:
        y = y1 + ((x-x1)/len_x) * len_y
        if floor((x-x0)%(2*pi/f))==0:
            rand = random()
            f = uniform(f1,f2)
            x0 = x
        if write_dots == 1:
            y += sin((x-x0)*f) * amp * rand
            points.append((x,y))
        if dot_count == len_dots:
            if write_dots == 1:
                polygon(*points,close=False)
            points = []
            len_dots = randint(dot1,dot2)
            write_dots = 1-write_dots
            dot_count = 0
        dot_count += 1
        

