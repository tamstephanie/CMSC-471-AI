from dcsolve import dcsolver

word_pairs = [('dog', 'cat'), ('kit', 'zap'),('ask', 'why'), ('face',
              'pill'), ('oozy', 'aqua'), ('icky', 'poop'), ('quiz',
              'kook'), ('quad','zoom')]

costs = ['steps', 'scrabble', 'frequency']

for w1, w2 in word_pairs:
    for cost in costs:
        dcsolver(w1, w2, cost)
    print
        
