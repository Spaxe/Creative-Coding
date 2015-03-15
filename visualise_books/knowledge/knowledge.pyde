book_name = 'The Problems of Philosophy_Russell.txt'
words = []

screen_scale = 1
web_connection_threshold = 200

important_words = ['knowledge', 'sense', 'things', 'know', 'data', 'true', 'fact', 'object', 'physical', 'belief']
word_count = [(u'knowledge', 306),
 (u'sense', 234),
 (u'may', 173),
 (u'must', 169),
 (u'things', 167),
 (u'know', 162),
 (u'one', 156),
 (u'us', 152),
 (u'two', 149),
 (u'thus', 146),
 (u'data', 138),
 (u'true', 130),
 (u'fact', 108),
 (u'object', 105),
 (u'physical', 101),
 (u'belief', 99),
 (u'see', 98),
 (u'objects', 95),
 (u'relation', 94),
 (u'gutenberg', 93),
 (u'table', 93),
 (u'certain', 91),
 (u'cannot', 89),
 (u'known', 89),
 (u'truth', 89),
 (u'project', 87),
 (u'mind', 87),
 (u'would', 86),
 (u'philosophy', 85),
 (u'self', 84),
 (u'experience', 80),
 (u'world', 78),
 (u'acquaintance', 78),
 (u'something', 78),
 (u'different', 77),
 (u'thing', 76),
 (u'space', 74),
 (u'particular', 74),
 (u'general', 72),
 (u'therefore', 71),
 (u'acquainted', 71),
 (u'time', 67),
 (u'case', 67),
 (u'shall', 67),
 (u'upon', 66),
 (u'man', 63),
 (u'many', 62),
 (u'say', 61),
 (u'proposition', 61),
 (u'universals', 59),
 (u'question', 59),
 (u'nature', 58),
 (u'first', 58),
 (u'colour', 58),
 (u'possible', 57),
 (u'tm', 57),
 (u'could', 57),
 (u'terms', 55),
 (u'existence', 55),
 (u'principle', 54),
 (u'way', 54),
 (u'exist', 54),
 (u'make', 53),
 (u'real', 53),
 (u'reason', 53),
 (u'view', 52),
 (u'though', 51),
 (u'also', 51),
 (u'work', 50),
 (u'principles', 50),
 (u'beliefs', 50),
 (u'really', 50),
 (u'minds', 50),
 (u'truths', 49),
 (u'called', 49),
 (u'law', 48),
 (u'even', 47),
 (u'chapter', 47),
 (u'believe', 47),
 (u'less', 47),
 (u'matter', 46),
 (u'people', 46),
 (u'without', 46),
 (u'thought', 46),
 (u'description', 45),
 (u'kind', 45),
 (u'hence', 45),
 (u'e', 44),
 (u'relations', 44),
 (u'whether', 44),
 (u'four', 43),
 (u'example', 43),
 (u'seem', 43),
 (u'seems', 43),
 (u'evidence', 42),
 (u'since', 42),
 (u'sort', 42),
 (u'whole', 41),
 (u'judgement', 40),
 (u'anything', 40),
 (u'whatever', 40),
 (u'like', 40),
 (u'never', 39),
 (u'cases', 39),
 (u'find', 39),
 (u'word', 38),
 (u'however', 38),
 (u'concerning', 38),
 (u'doubt', 38),
 (u'men', 37),
 (u'order', 37),
 (u'ideas', 37),
 (u'philosophers', 37),
 (u'might', 37),
 (u'evident', 37),
 (u'form', 36),
 (u'means', 36),
 (u'past', 36),
 (u'common', 36),
 (u'become', 36),
 (u'suppose', 35),
 (u'mental', 35),
 (u'nothing', 34),
 (u'point', 34),
 (u'instance', 34),
 (u'complex', 33),
 (u'given', 33),
 (u'consider', 33),
 (u'person', 33),
 (u'exists', 33),
 (u'works', 33),
 (u'much', 32),
 (u'life', 32),
 (u'merely', 32),
 (u'quite', 32),
 (u'desdemona', 32),
 (u'sun', 32),
 (u'found', 32),
 (u'certainty', 32),
 (u'yet', 31),
 (u'think', 31),
 (u'laws', 31),
 (u'science', 31),
 (u'idea', 31),
 (u'part', 31),
 (u'present', 31),
 (u'universe', 31),
 (u'logic', 30),
 (u'propositions', 30),
 (u'universal', 30),
 (u'said', 29),
 (u'either', 29),
 (u'call', 28),
 (u'seen', 28),
 (u'falsehood', 28),
 (u'least', 28),
 (u'cassio', 28),
 (u'great', 28),
 (u'use', 28),
 (u'although', 28),
 (u'actual', 28),
 (u'answer', 27),
 (u'foundation', 27),
 (u'electronic', 27),
 (u'important', 27),
 (u'far', 27),
 (u'b', 27),
 (u'questions', 27),
 (u'false', 27),
 (u'another', 26),
 (u'prove', 26),
 (u'future', 26),
 (u'argument', 26),
 (u'berkeley', 26),
 (u'always', 26),
 (u'particulars', 26),
 (u'mean', 25),
 (u'subject', 25),
 (u'except', 25),
 (u'regard', 25),
 (u'parts', 25),
 (u'often', 25),
 (u'body', 25),
 (u'kant', 25),
 (u'aware', 24),
 (u'shape', 24),
 (u'associated', 24),
 (u'necessary', 24),
 (u'datum', 23),
 (u'logical', 23),
 (u'memory', 23),
 (u'still', 23),
 (u'judgements', 23),
 (u'take', 23),
 (u'believing', 23),
 (u'seeing', 23),
 (u'light', 23),
 (u'difficult', 23),
 (u'immediately', 23),
 (u'give', 22),
 (u'tree', 22),
 (u'theory', 22),
 (u'namely', 22),
 (u'come', 22),
 (u'among', 22),
 (u'instances', 22),
 (u'supposed', 22),
 (u'follows', 22),
 (u'senses', 22),
 (u'consists', 21),
 (u'intuitive', 21),
 (u'number', 21),
 (u'immediate', 21),
 (u'understand', 21),
 (u'makes', 21),
 (u'private', 21),
 (u'value', 21),
 (u'states', 20),
 (u'sensations', 20),
 (u'various', 20),
 (u'else', 20),
 (u'othello', 20),
 (u'degree', 20),
 (u'probable', 20),
 (u'result', 19),
 (u'independent', 19),
 (u'thoughts', 19),
 (u'facts', 19),
 (u'agreement', 19),
 (u'inductive', 19),
 (u'definite', 19),
 (u'property', 19),
 (u'act', 19),
 (u'connexion', 19),
 (u'long', 19),
 (u'sensation', 19),
 (u'involved', 19),
 (u'contradiction', 19),
 (u'next', 19),
 (u'becomes', 19)]
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
                if x != 0:
                    rotate(-atan(float(y)/(x)))
                else:
                    rotate(-PI/2)
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
                dc = map(y, 0, lines+1, 0, 1) * 0.2
                fill(0.1+dc/2, 0.3+dc, 0.6+dc*2, 1)
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
            
    save('Knowledge.png')
    
