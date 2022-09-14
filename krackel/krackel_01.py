exec(open('krackel.py').read())

size(200,300)
p1 = (20,0)
p2 = (180,0)
stroke(0)
strokeWidth(2)

translate(0,250)
zittLine(p1,p2)

translate(0,-70)
zittLine(p1,p2,amp=20)

translate(0,-70)
zittLine(p1,p2,f=2)

translate(0,-70)
zittLine(p1,p2,f=2,d=1/2)
