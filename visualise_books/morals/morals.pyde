book_name = 'Principles of Morals_Hume.txt'
words = []
important_words = ['reason', 'society', 'nature', 'sentiment', 'without', 'justice', 'human', 'good', 'moral', 'virtue']
screen_scale = 1
web_connection_threshold = 200
word_count = [
 (u'may', 173),
 (u'one', 158),
 (u'every', 149),
 (u'man', 148),
 (u'us', 131),
 (u'must', 129),
 (u'society', 123),
 (u'would', 113),
 (u'nature', 110),
 (u'sentiment', 108),
 (u'without', 103),
 (u'general', 99),
 (u'even', 97),
 (u'justice', 95),
 (u'human', 93),
 (u'though', 91),
 (u'men', 89),
 (u'regard', 88),
 (u'good', 88),
 (u'moral', 83),
 (u'virtue', 81),
 (u'reason', 81),
 (u'others', 81),
 (u'much', 78),
 (u'sentiments', 78),
 (u'particular', 77),
 (u'mankind', 73),
 (u'virtues', 71),
 (u'ever', 67),
 (u'footnote', 66),
 (u'object', 65),
 (u'interest', 64),
 (u'qualities', 64),
 (u'self', 64),
 (u'property', 62),
 (u'approbation', 62),
 (u'love', 61),
 (u'never', 60),
 (u'happiness', 58),
 (u'humanity', 57),
 (u'person', 57),
 (u'well', 57),
 (u'natural', 55),
 (u'laws', 55),
 (u'like', 55),
 (u'utility', 55),
 (u'order', 54),
 (u'common', 54),
 (u'social', 53),
 (u'character', 53),
 (u'merit', 53),
 (u'among', 53),
 (u'great', 53),
 (u'could', 53),
 (u'public', 51),
 (u'species', 51),
 (u'mind', 50),
 (u'yet', 50),
 (u'many', 50),
 (u'part', 50),
 (u'different', 49),
 (u'give', 48),
 (u'also', 48),
 (u'useful', 47),
 (u'first', 45),
 (u'often', 44),
 (u'agreeable', 44),
 (u'principles', 43),
 (u'principle', 43),
 (u'life', 43),
 (u'affection', 43),
 (u'conduct', 42),
 (u'another', 42),
 (u'kind', 41),
 (u'case', 40),
 (u'pleasure', 40),
 (u'present', 40),
 (u'make', 39),
 (u'seems', 39),
 (u'indeed', 38),
 (u'still', 38),
 (u'former', 38),
 (u'rules', 38),
 (u'alone', 37),
 (u'influence', 37),
 (u'benevolence', 37),
 (u'tendency', 36),
 (u'objects', 36),
 (u'praise', 36),
 (u'esteem', 36),
 (u'purpose', 34),
 (u'entirely', 34),
 (u'passions', 34),
 (u'sense', 34),
 (u'shall', 34),
 (u'upon', 34),
 (u'beauty', 33),
 (u'distinction', 33),
 (u'blame', 33),
 (u'either', 33),
 (u'find', 33),
 (u'whole', 33),
 (u'private', 33),
 (u'interests', 33),
 (u'arises', 33),
 (u'immediately', 33),
 (u'whether', 33),
 (u'therefore', 32),
 (u'foundation', 32),
 (u'manner', 32),
 (u'place', 32),
 (u'origin', 32),
 (u'always', 32),
 (u'degree', 32),
 (u'rule', 32),
 (u'indifferent', 31),
 (u'morals', 31),
 (u'cannot', 31),
 (u'observe', 31),
 (u'friendship', 31),
 (u'nothing', 31),
 (u'relations', 31),
 (u'says', 30),
 (u'say', 30),
 (u'pernicious', 30),
 (u'actions', 30),
 (u'certain', 30),
 (u'found', 30),
 (u'source', 30),
 (u'passion', 30),
 (u'account', 30),
 (u'concerning', 29),
 (u'suppose', 29),
 (u'whatever', 29),
 (u'instance', 29),
 (u'consequences', 29),
 (u'generous', 29),
 (u'circumstances', 28),
 (u'arise', 28),
 (u'instances', 28),
 (u'sufficient', 28),
 (u'made', 28),
 (u'force', 27),
 (u'latter', 27),
 (u'right', 27),
 (u'theory', 27),
 (u'enjoyment', 27),
 (u'least', 27),
 (u'contrary', 27),
 (u'means', 27),
 (u'greater', 27),
 (u'whose', 26),
 (u'subject', 26),
 (u'advantage', 26),
 (u'allowed', 26),
 (u'views', 26),
 (u'reasoning', 26),
 (u'vice', 26),
 (u'regarded', 25),
 (u'heart', 25),
 (u'fortune', 25),
 (u'far', 25),
 (u'action', 25),
 (u'might', 25),
 (u'sympathy', 25),
 (u'individual', 25),
 (u'considerable', 25),
 (u'system', 25),
 (u'requisite', 24),
 (u'however', 24),
 (u'intercourse', 24),
 (u'persons', 24),
 (u'industry', 24),
 (u'imagination', 24),
 (u'consider', 24),
 (u'misery', 24),
 (u'feel', 24),
 (u'supposed', 24),
 (u'affections', 24),
 (u'view', 24),
 (u'strong', 23),
 (u'possessed', 23),
 (u'gives', 23),
 (u'selfish', 23),
 (u'circumstance', 23),
 (u'lib', 23),
 (u'appear', 23),
 (u'relation', 23),
 (u'use', 23),
 (u'quality', 23),
 (u'perhaps', 23),
 (u'proper', 23),
 (u'end', 22),
 (u'characters', 22),
 (u'commonly', 22),
 (u'ideas', 22),
 (u'according', 22),
 (u'known', 22),
 (u'philosophy', 22),
 (u'less', 22),
 (u'authority', 22),
 (u'evident', 22),
 (u'beneficial', 21),
 (u'civil', 21),
 (u'time', 21),
 (u'totally', 21),
 (u'satisfaction', 21),
 (u'chiefly', 21),
 (u'obvious', 21),
 (u'conversation', 21),
 (u'frequently', 21),
 (u'reflection', 21),
 (u'necessary', 21),
 (u'given', 20),
 (u'opposite', 20),
 (u'behaviour', 20),
 (u'experience', 20),
 (u'immediate', 20),
 (u'manners', 20),
 (u'naturally', 20),
 (u'ill', 19),
 (u'towards', 19),
 (u'war', 19),
 (u'form', 19),
 (u'censure', 19),
 (u'appears', 19),
 (u'world', 19),
 (u'difference', 19),
 (u'eye', 19),
 (u'rather', 19),
 (u'possession', 19),
 (u'hypothesis', 19),
 (u'parts', 19),
 (u'little', 18),
 (u'render', 18),
 (u'hand', 18),
 (u'greatest', 18),
 (u'discover', 18),
 (u'concern', 18),
 (u'situation', 18)
]
freq_words = {k: v for k, v in word_count}
coordinates = {k: [] for k in important_words}
all_coordinates = []
block_size = 8 / screen_scale

def setup():
    global words, screen_scale
    size(1920 / screen_scale, 1080 / screen_scale)
#     size(1920 / screen_scale, 1080 / screen_scale, "processing.core.PGraphicsRetina2D")
    colorMode(HSB, 1.0)
    textFont(createFont('SourceSansPro-ExtraLight', block_size))
    textSize(block_size)
    noLoop()
    words = load_corpus(book_name)
    
def load_corpus(path):
    with open(path, 'r') as f:
        return f.read().split()
    
def generate_color(word):
    return float(important_words.index(word)) / len(important_words)

def draw_word():
    global words
    spacing = 1
    x = 0
    y = height - block_size
    for word in reversed(words):
        word = word.lower()
        if (x + textWidth(word) + spacing) > width - 10:
            x = 0
            y -= block_size

        if word in coordinates:
            coordinates[word].append((x, y))
            
        all_coordinates.append((word, x, y))
        
        x += textWidth(word) + spacing

def draw_star(word, xy):
    with pushStyle():
        noStroke()
        ellipseMode(CENTER)
        for x, y in xy:
            dy = pow(float(y) / height, 2)
            dx = pow(float(x) / width, 2)
            a = 0.9
            s = 0.7
            fill(generate_color(word), s, 0.9-dy/2, a-dy)
            ellipse(x+block_size/2, y+block_size/2, block_size, block_size)
            depth = -1
            with pushMatrix():
                translate(int(x/block_size)*block_size, y)
                if x != width:
                    rotate(-atan(float(y)/(width-x)))
                else:
                    rotate(PI/2)
                fill(generate_color(word), s-0.2, 1-dy, 1-(dy+dx)*1.5/2)
                rect(0, 0, block_size, -height)
            
            for _x, _y in xy:
                if dist(x, y, _x, _y) < web_connection_threshold:
                    noFill()
                    stroke(generate_color(word), s-0.1, 0.8-dy/4, a-dy*2)
                    line(x+block_size/2, y+block_size/2, _x+block_size/2, _y+block_size/2)
                
                
def draw_land():
    with pushStyle():
        noStroke()
        for i, (w, c) in enumerate(sorted(word_count)):
            c /= screen_scale
            fill(0, 0, 0, 0.2)
            rect(i*block_size, height-c, block_size, c)
            fill(1, 0, 1, 1.2*c/height)
            rect(i*block_size, height-c, block_size, block_size)
            with pushMatrix():
                translate((i+1)*block_size-1, height-1)
                rotate(-PI/2)
                if w in important_words:
                    fill(generate_color(w), 0.8, 1, 0.6)
                else:
                    fill(0, 0, 1, 0.5)
                text(w, 0, 0)
    
def draw():
    background(0)
    
    with pushStyle():
        colorMode(RGB, 1.0)
        lines = height/block_size
        with pushMatrix():
#             rotate(PI/16)
            for y in range(-30, lines+31):
                dc = float(y)/lines/10
                fill(0.8-dc*3, 0.3-dc, 0.2+dc, 1)
                noStroke()
                rect(-500, y*block_size, width+500, (y+1)*block_size)
    
    with pushMatrix():
#         padding = (10.0 / screen_scale, -10.0 / screen_scale)
        padding = (10 / screen_scale, 0)
        translate(*padding)
        draw_word()
            
        for word, xy in coordinates.iteritems():
            draw_star(word, xy)
            
        with pushStyle():
            for word, x, y in all_coordinates:
                if word in important_words:
                    fill(generate_color(word), 0.7, 1, 1-float(y)/height)
                else:
                    fill(1, 0, 1, 1-float(y)/height)
                text(word, x, y)
            
    draw_land()
            
    save('Morals.png')
    
