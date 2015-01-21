
def setup():
    size(512, 512, "processing.core.PGraphicsRetina2D")
    colorMode(HSB, 1, 1, 1, 1)
    generate_array()
    
def generate(resolution, pixel_size, rate, secondary_rate, colour):
    pushStyle()    
    s = pixel_size
    for y in range(1, resolution-1):
        fill(*colour)
        if y > resolution/2:
            fill(colour[0], colour[1]-0.1, colour[2]-0.2)
        for x in range(1, resolution/2):
            px = s * x
            py = s * y 
            px2 = s * map(x, 0, resolution/2, resolution-1, resolution/2-1)
            rate2 = map(x, 0, resolution/2, 0, secondary_rate)
            
            if random(0, 1) < (rate + rate2):
                rect(px, py, s, s)
                rect(px2, py, s, s)
    popStyle()
                
def generate_array():
    reset()
    resolution = 16
    pixel_size = 4
    rate = 0.05
    secondary_rate = 0.8
    block = resolution * pixel_size
    for y in range(8):
        for x in range(8):
            pushMatrix()
            translate(x * block, y * block)
            c = (random(0.4, 0.6), 0.4, 0.9)
            generate(resolution, 
                     pixel_size, 
                     rate, 
                     secondary_rate,
                     colour=c)
            popMatrix()
                
def mouseMoved():
    generate_array()
    
def draw():
    pass
    
def reset():
    background(0)
    noStroke()
