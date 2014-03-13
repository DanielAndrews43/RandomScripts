def find_replace(word, find, replace):
    for char in xrange(len(word)):
        print char
        if word[char:char+1] == find:
            word = word[0:char] + replace + word[char+1:]
    print word
    
word = """
quality|breakfast||pancakes
five guys|lunch||burgers
pizza hut|dinner||pizza
dominoes|dinner||pizza
ihop|breakfast||pancakes
magnolia|dessert||cake
cpk|dinner||pizza
panda|dinner||chicken
wahoo's|lunch||mexican
jersey mike's|lunch||sandwhich
subway|lunch||sandwhich
starbucks|snack||drinks
the counter|dinner||burgers
chipotle|lunch||mexican
andres|dinner||pasta
momos|dinner||sushi
norms|breakfast||pancakes
"""

find_replace(word, '|', '~')