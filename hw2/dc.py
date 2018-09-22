"""  CMSC471 01 hw2 spring 2017
     Stephanie Tam, RU14618

     Description: Use the aima package and dictionaries to code converting an initial word to a goal word using
                  different cost measures (steps, scrabble, or frequency). 
"""

import gzip
import aima.search as a       # AIMA module for search problems

dict_file = "words34.txt.gz"

dictionary = {}

# dictionary of values
scrabble_values = { 
    'a':1, 'e':1, 'i':1, 'o':1, 'u':1, 'l':1, 'n':1, 's':1, 't':1, 'r':1,
    'd':2, 'g':2,
    'b':3, 'c':3, 'm':3, 'p':3,
    'f':4, 'h':4, 'v':4, 'w':4, 'y':4,
    'k':5,
    'j':6, 'x':6,
    'z':10, 'q':10
}

for line in gzip.open(dict_file):
    word, n = line.strip().split('\t')
    dictionary[word] = float(n)

class DC(a.Problem):

    # constructor for DC class
    def __init__(self, initial='dog', goal='cat', cost='steps'):
        self.initial=initial
        self.goal = goal
        self.cost = cost

    # decide next legal step to take
    def actions(self, state):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        legal_words = []

        # go through word and replace each character with a letter of the alphabet
        for i in range(len(state)):
            for j in range(len(alphabet)):
                word_chars = list(state)
                word_chars[i] = alphabet[j]  # swap characters
                new_word = "".join(word_chars) # join the words to make a word

                # check if the word exists in the dictionary, and if so, add it to the list of legal words
                if(new_word in dictionary and new_word != state):  # make sure the new word is not the original word too
                    legal_words.append(new_word)
                    
        return legal_words
#	return switchChar(state)

    # return the action chosen from actions function
    def result(self, state, action):
        return action

    # return true if goal is reached
    def goal_test(self, state):
        if(state == self.goal):
            return True
        else:
            return False

    # calculate and return cost for each cost measure
    def path_cost(self, c, state1, action, state2):
        action_cost = 0;

        # cost is 1 per change in character
        if(self.cost == "steps"):
            action_cost = 1

       # cost is value of each character, as specified in the scrabble_values dictionary
        elif(self.cost == "scrabble"):
            for i in range(len(state1)):
                if(state1[i] != state2[i]):
                    action_cost = scrabble_values[state2[i]]

       # cost is 1 per change in character and frequency of the word
        elif(self.cost == "frequency"):
            action_cost = dictionary[state2]
			
        return c + action_cost

    def h(self, node):
        """Heuristic: returns an estimate of the cost to get from the
        state of this node to the goal state.  The heuristic's value
        should depend on the Problem's cost parameter (steps, scrabble
        or frequency) as this will effect the estimate cost to get to
        the nearest goal. """

        h_value = 0
	char_changes = [] #array of characters to change

        # compare characters from current state to goal state and add them to the array if they are not the same in the same place
        for i in range(len(self.goal)):
            if(self.goal[i] != node.state[i]):
                char_changes.append(self.goal[i])
        
        # steps: how many letters changed
        if(self.cost == "steps"):
            h_value = len(char_changes)

        # scrabble: costs of the new letters needed
        if(self.cost == "scrabble"):
            for character in char_changes:
                h_value += scrabble_values[character]

	# frequency: how many letters changed and cost of that final word.
        if(self.cost == "frequency"):
            h_value = len(char_changes) * dictionary[self.goal]
        
        return h_value

    # basically overloaded printing
    def __repr__(self):
        """ returns a string to represent a dc problem """
        return "DogCat({},{},{})".format(self.initial, self.goal, self.cost)


# add more functions here as needed
# function that determines legal words in conversion
"""def switchChar(word):
        
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    legal_words = []
    
    # go through word and replace each character with a letter of the alphabet
    for i in range(len(word)):
        for j in range(len(alphabet)):
            word_chars = list(word)
            word_chars[i] = alphabet[j]  # swap characters
            new_word = "".join(word_chars) # join the words to make a word

            # check if the word exists in the dictionary, and if so, add it to the list of legal words
            if(new_word in dictionary and new_word != word):  # make sure the new word is not the original word too
                legal_words.append(new_word)
                
    return legal_words"""
