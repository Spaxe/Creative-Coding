book_name = 'Laughter_Bergson.txt'
words = []

screen_scale = 1
web_connection_threshold = 200

important_words = ['comic', 'life', 'laughter', 'certain', 'comedy', 'character', 'laugh', 'kind', 'idea', 'nature']
word_count = [
 (u'comic', 316),
 (u'one', 261),
 (u'us', 217),
 (u'life', 121),
 (u'would', 118),
 (u'may', 107),
 (u'laughter', 89),
 (u'two', 85),
 (u'though', 83),
 (u'must', 79),
 (u'certain', 79),
 (u'comedy', 79),
 (u'even', 70),
 (u'find', 65),
 (u'character', 62),
 (u'laugh', 62),
 (u'upon', 62),
 (u'form', 61),
 (u'always', 58),
 (u'kind', 57),
 (u'see', 57),
 (u'something', 57),
 (u'like', 57),
 (u'another', 55),
 (u'every', 54),
 (u'man', 54),
 (u'idea', 54),
 (u'first', 53),
 (u'point', 53),
 (u'nature', 52),
 (u'however', 52),
 (u'art', 52),
 (u'effect', 52),
 (u'mind', 50),
 (u'laughable', 50),
 (u'person', 50),
 (u'thus', 50),
 (u'made', 50),
 (u'many', 48),
 (u'might', 48),
 (u'shall', 48),
 (u'let', 48),
 (u'take', 47),
 (u'time', 47),
 (u'nothing', 46),
 (u'body', 46),
 (u'far', 45),
 (u'make', 44),
 (u'word', 43),
 (u'general', 43),
 (u'element', 43),
 (u'words', 43),
 (u'series', 42),
 (u'say', 42),
 (u'characters', 41),
 (u'living', 41),
 (u'society', 40),
 (u'well', 40),
 (u'forms', 39),
 (u'rather', 39),
 (u'also', 39),
 (u'makes', 39),
 (u'scene', 39),
 (u'become', 39),
 (u'think', 37),
 (u'attention', 37),
 (u'things', 37),
 (u'instance', 37),
 (u'mechanical', 37),
 (u'play', 36),
 (u'said', 35),
 (u'without', 35),
 (u'fact', 35),
 (u'soul', 34),
 (u'indeed', 34),
 (u'language', 34),
 (u'different', 34),
 (u'reason', 34),
 (u'never', 33),
 (u'way', 33),
 (u'social', 33),
 (u'short', 33),
 (u'law', 32),
 (u'imagination', 32),
 (u'stage', 32),
 (u'matter', 31),
 (u'case', 31),
 (u'events', 31),
 (u'seems', 31),
 (u'image', 31),
 (u'natural', 30),
 (u'still', 30),
 (u'often', 30),
 (u'latter', 29),
 (u'yet', 29),
 (u'less', 29),
 (u'whole', 29),
 (u'within', 29),
 (u'thing', 28),
 (u'ideas', 28),
 (u'ever', 27),
 (u'object', 27),
 (u'human', 27),
 (u'absentmindedness', 27),
 (u'back', 27),
 (u'order', 26),
 (u'situation', 26),
 (u'particular', 26),
 (u'individual', 26),
 (u'impression', 26),
 (u'repetition', 26),
 (u'logic', 26),
 (u'possible', 25),
 (u'simple', 25),
 (u'rigidity', 25),
 (u'others', 25),
 (u'cause', 25),
 (u'result', 24),
 (u'capable', 24),
 (u'real', 24),
 (u'common', 24),
 (u'called', 24),
 (u'appear', 23),
 (u'good', 23),
 (u'moment', 23),
 (u'state', 23),
 (u'poet', 23),
 (u'mere', 23),
 (u'come', 22),
 (u'expression', 22),
 (u'absurdity', 22),
 (u'look', 22),
 (u'meaning', 22),
 (u'go', 22),
 (u'work', 21),
 (u'effects', 21),
 (u'side', 21),
 (u'men', 21),
 (u'making', 21),
 (u'get', 21),
 (u'part', 21),
 (u'actions', 21),
 (u'set', 21),
 (u'drama', 21),
 (u'light', 21),
 (u'special', 21),
 (u'could', 21),
 (u'type', 20),
 (u'de', 20),
 (u'terms', 20),
 (u'speak', 20),
 (u'hand', 20),
 (u'reality', 20),
 (u'cannot', 20),
 (u'sense', 20),
 (u'perhaps', 20),
 (u'moral', 19),
 (u'times', 19),
 (u'end', 19),
 (u'already', 19),
 (u'along', 19),
 (u'persons', 19),
 (u'feelings', 19),
 (u'wit', 19),
 (u'face', 19),
 (u'etc', 19),
 (u'whether', 19),
 (u'second', 18),
 (u'found', 18),
 (u'phrase', 18),
 (u'give', 18),
 (u'feeling', 18),
 (u'seen', 18),
 (u'generally', 18),
 (u'serious', 18),
 (u'merely', 18),
 (u'place', 18),
 (u'aspect', 18),
 (u'automatism', 18),
 (u'ready', 18),
 (u'analysis', 18),
 (u'either', 18),
 (u'following', 18),
 (u'machine', 17),
 (u'mean', 17),
 (u'seem', 17),
 (u'dreams', 17),
 (u'longer', 17),
 (u'cases', 17),
 (u'comes', 17),
 (u'method', 17),
 (u'action', 17),
 (u'mental', 17),
 (u'really', 17),
 (u'self', 17),
 (u'ludicrous', 17),
 (u'consequently', 17),
 (u'mechanism', 17),
 (u'fashion', 16),
 (u'child', 16),
 (u'everything', 16),
 (u'witty', 16),
 (u'effort', 16),
 (u'gesture', 16),
 (u'eyes', 16),
 (u'movements', 16),
 (u'complete', 16),
 (u'contrast', 16),
 (u'simply', 16),
 (u'm', 16),
 (u'becomes', 16),
 (u'arrangement', 16),
 (u'instead', 16),
 (u'transposition', 16),
 (u'almost', 16),
 (u'force', 15),
 (u'obtained', 15),
 (u'amusing', 15),
 (u'much', 15),
 (u'therefore', 15),
 (u'lies', 15),
 (u'formula', 15),
 (u'given', 15),
 (u'ridiculous', 15),
 (u'note', 15),
 (u'taken', 15),
 (u'number', 15),
 (u'closely', 15),
 (u'anything', 15),
 (u'fresh', 15),
 (u'hence', 15),
 (u'inner', 15),
 (u'consists', 14),
 (u'third', 14),
 (u'independent', 14),
 (u'scenes', 14),
 (u'altogether', 14),
 (u'three', 14),
 (u'call', 14),
 (u'together', 14)]

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
#                 if x != width:
#                     rotate(-atan(float(y)/(width-x)))
#                 else:
#                     rotate(PI/2)
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
            for y in range(lines+1):
                dc = float(y)/lines/10
                fill(0.5-dc*2, 0.2, 0.4+dc, 1)
                noStroke()
                rect(0, y*block_size, width, (y+1)*block_size)
    
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
            
    save('Laughter.png')
    
