import numpy as np
def generate_sentence():
    nouns = ['Ente', 'Welt', 'Karotte', 'Wurst', 'Flasche','Wunderlampe','Langschläferin','Lügerin','Streberin','Lehrerin','Hexe']
    verbs = ['quakt', 'endet', 'schmeckt', 'zaubert','rennt','stöbert','findet','lehrt','stirbt','leugnet','findet','ist']
    adjectives = ['gruselig', 'sauer', 'süß', 'klein', 'toll','langsam','weich','hungrig','gelangweilt','glücklich']
    sentence = 'Die {} {} {},'.format(np.random.choice(nouns, 1)[0],
                               np.random.choice(verbs, 1)[0],
                                np.random.choice(adjectives, 1)[0])
    sentence2 = 'weil die {} {} {}'.format(np.random.choice(nouns, 1)[0],
                                    np.random.choice(adjectives, 1)[0],
                                     np.random.choice(verbs, 1)[0])
    sentence3 = ' und weil die {} {} {}.'.format(np.random.choice(nouns, 1)[0],
                                    np.random.choice(adjectives, 1)[0],
                                     np.random.choice(verbs, 1)[0])
    return sentence + sentence2 + sentence3

for i in range(0,10):
    print(generate_sentence())
