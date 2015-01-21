sides = 6.0
bg = 0
xgrid = 6
ygrid = 6

def setup():
#     size(800, 800, "processing.core.PGraphicsRetina2D")
    size(1024, 1024, P2D)
    colorMode(HSB, 1.0)
    ellipseMode(RADIUS)
    
    
# def draw():
    background(bg)
#     snow_fractal(width/2, height/2, mouseX/2, mouseY/8)

    for i in range(1,xgrid):
        for j in range(1,ygrid):
            mx = random(28, 48)
            my = random(24, 40)
            dc = random(-0.2, 0.3)
            pushMatrix()
            translate(i*width/xgrid, j*height/ygrid)
            snow_fractal(width/2, height/2, mx, my, dc)
            bg_mask(mx-my*4)
            popMatrix()
#     text("params: {}, {}".format(mouseX/2, mouseY/8), 10, 10)
    
    
def snow_fractal(x, y, r, s, dc=0):
    blendMode(ADD)
    for i in reversed(range(sides)):
        pushStyle()
        pushMatrix()
        
#         translate(x, y)
        rotate(PI/3*i)
        translate(r, 0)
        
        noStroke()
        
        c = 0
        if i < sides/2:
            c = map(i, 0, sides/2, 0+random(0.1), 0.2+random(-0.1, 0.1))
        else:
            c = map(i, sides/2, sides, 0.5+random(-0.1, 0.1), 0.7+random(-0.1, 0.1))
            
        c += dc
        
        fill(c, 
#              map(i, sides-1, 0, 0.74, 1),
#              map(i, sides-1, 0, 1, 0.68),
             0.5,
             0.5,
             0.4)
        
        tri_side = s*sqrt(3)
#         triangle(-s/2, tri_side/2, -s/2, -tri_side/2, s, 0)
#         ellipse(0, 0, s, s)
        
        fractal_leaves(r*0.5, s*0.95, 8)
        
        popMatrix()
        popStyle()
    
    
def fractal_leaves(r, s, depth=1):
    if depth < 1 or s < 1:
        return
    
    for a in [PI/3, -PI/3, PI]:
        pushMatrix()
        rotate(a)
        translate(r, 0)
        tri_side = s*sqrt(3)
        triangle(-s/2, tri_side/2, -s/2, -tri_side/2, s, 0)
#         ellipse(0, 0, s, s)
        fractal_leaves(r/2, s/2, depth-1)
        popMatrix()
        
        
def bg_mask(r):
    pushStyle()
    pushMatrix()
    fill(bg)
    noStroke()
    translate(width/2, height/2)
    
    beginShape(QUAD_STRIP)
    divisions = 128
    for b in range(divisions) + [divisions]:
        a = b * PI/(divisions/2)
        vertex(r*cos(a), r*sin(a))
        vertex(2*r*cos(a), 2*r*sin(a))
    endShape()
    
    popMatrix()
    popStyle()
    
    
def globe(x, y, r):
    pushStyle()
    
    # Gradient fill for glancing angles
    noFill()
    for i in range(r):
        stroke(0, 0, 1, map(i, r/4, r-10, 0, 0.1))
        ellipse(x, y, i, i)
    
    # Outline
    stroke(0, 0, 1, 0.05)
    for i in range(5):
        strokeWeight(i)
        ellipse(x, y, r-i, r-i)
    stroke(0, 0, 1, 0.5)
    strokeWeight(1)
    ellipse(x, y, r, r)
    
    popStyle()
    
