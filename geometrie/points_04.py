exec(open('geometrie.py').read())

size(600,100)
p = (50,50)

ovalFromPoints(p,100,50,0)
translate(100,0)
ovalFromPoints(p,100,50,1)
translate(100,0)
ovalFromPoints(p,100,50,2)
