exec(open('musicnotation.py').read())

size(800,110)
p = (0,20)
stroke(0)
noteSystem(p,200)
translate(10,0)
for n in range(10):
    note(p)
    translate(20,5)

translate(10,-50)
noteSystem(p,200)
fill(None)
translate(10,0)
strokeWidth(2)
for n in range(10):
    note(p)
    translate(20,5)

translate(10,-50)
noteSystem(p,200)
translate(10,0)
strokeWidth(1.5)
for n in range(10):
    noteDiamond(p)
    translate(20,5)
