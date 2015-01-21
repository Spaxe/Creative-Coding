unit = 128
padding = 64

def setup():
    size(840, 840)
    noStroke()
    colorMode(HSB, 100)
    background(0)
    ellipseMode(CENTER)
    
    dc = 0
    for gx in range(padding, width-padding, unit+padding):
        for gy in range(padding, height-padding, unit+padding):
            fill(random(dc % 100, (15+dc) % 100), 80, 70, 50)
            ellipse(gx+unit/2, gy+unit/2, unit+40, unit+40)
            dc += 35
    filter(BLUR, 8)
    
    dc = 0
    for gx in range(padding, width-padding, unit+padding):
        for gy in range(padding, height-padding, unit+padding):
            fill(random(dc % 100, (15+dc) % 100), 75, 80, 5)
            ellipse(gx+unit/2, gy+unit/2, unit+32, unit+32)
            dc += 35
    blendMode(OVERLAY);

    dc = 0
    for gx in range(padding, width-padding, unit+padding):
        for gy in range(padding, height-padding, unit+padding):
            points = zip([random(1) * unit for _ in range(64)],
                         [random(1) * unit for _ in range(64)])
            points = sorted(points, key=lambda p: p[0]**2+p[1]**2)
            
            fill(random(dc % 100, (15+dc) % 100), 80, 25, 0.5)
            ellipse(gx+unit/2, gy+unit/2, unit+32, unit+32)
            filter(None)
            
            for t in range(1):
                fill(random(dc % 100, (10+dc) % 100), random(50, 100), random(25, 50), 0.1)
                beginShape(TRIANGLES)
                vertex(gx+unit, gy+unit)
                for p in range(64):
#                     i = floor(random(len(points)))
                    i = p
                    x, y = points[i][0], points[i][1]
                    vertex(x+gx, y+gy)
                    r = random(3,8)
                    fill(random(dc % 100, (10+dc) % 100), random(100), random(50, 100), 0.2)
                    ellipse(x+gx, y+gy, r, r)
                endShape()
            dc += 35
