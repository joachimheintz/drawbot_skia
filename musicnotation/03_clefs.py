exec(open('musicnotation.py').read())

size(800,110)
p = (0,20)
stroke(0)
noteSystem(p,50)
violinClef(p)

translate(60,0)
noteSystem(p,140)
violinClef(p,rnd=1)
translate(30,0)
violinClef(p,rnd=1)
translate(30,0)
violinClef(p,rnd=3)
translate(30,0)
violinClef(p,rnd=3)

translate(60,0)
noteSystem(p,150)
bassClef(p)
translate(30,0)
bassClef(p,rnd=1)
translate(30,0)
bassClef(p,rnd=1)
translate(30,0)
bassClef(p,rnd=3)
translate(30,0)
bassClef(p,rnd=3)