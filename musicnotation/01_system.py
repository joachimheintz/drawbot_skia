exec(open('musicnotation.py').read())

size(600,110)
p = (0,20)

stroke(0)
noteSystem(p)

translate(110,0)
noteSystem(p,y_space=20)

translate(110,0)
noteSystem(p,sw=3,numlines=7)

translate(110,0)
stroke(.8)
noteSystem(p)

translate(110,0)
stroke(1,0,0)
noteSystem(p)
