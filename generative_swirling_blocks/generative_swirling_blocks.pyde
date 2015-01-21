import random
unit = 32
padding = 1

hue_palette = range(1, 14) + range(52, 64)

def setup():
    size(832, 832)
    colorMode(HSB, 100.0)
    
    background(100)
    noStroke()
    
    unit_size = unit
    chance = 2.0
    
    while unit_size > 2:
        for x in range(0, width, unit_size):
            for y in range(0, height, unit_size):
                random_hue = hue_palette[(x*y) % len(hue_palette)]
                if random.random() * chance > 0.5:
                    fill(random_hue, 50, 75, 20)
                    rect(x+padding, y+padding, unit_size-padding*2, unit_size-padding*2)
                if random.random() * chance > 0.75:
                    fill(random_hue, 70, 100, 40)
                    rect(x+padding, y+padding, unit_size-padding*2, unit_size-padding*2)
        chance /= 2
        unit_size /= 2

