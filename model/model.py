# Wordle Algorithm
# Zandr Meitus

import numpy as np
# test words
test_words = ['MODEL', 'COUNT', 'NYMPH', 'STAGE', 'TRANCE']

class Wodel(object):
    '''

    '''

    def __init__(self, possible_words):
        self.possible_words = possible_words
        self.letter_probs = self.calc_letter_probs(self.possible_words)
        self.word_scores = self.calc_word_scores(self.letter_probs)
        self.black_letters = {}
        self.yellow_letters = {}
        self.green_lettesr = {}



    def __repr__(self):
        pass


    def calc_letter_probs(self, possible_words):
        '''
        '''
    #def calc_letter_probs(possible_words):
        
        word_arrays = []
        word_sets = []
        letter_counts = {}
        for word in possible_words:
            word_array = []
            word_set = set()
            for i,letter in enumerate(word):
                word_set.add(letter)
                word_array.append(letter)
            
                if i == len(word) - 1:
                    word_arrays.append(word_array)
                    word_sets.append(word_set)

                if letter not in letter_counts:
                    letter_counts[letter] = 1
                else:
                    letter_counts[letter] = letter_counts[letter] + 1
        
        return (word_arrays, word_sets, letter_counts)
    

    def calc_word_scores(self, word_tuple):
        word_arrays, word_sets, letter_counts = word_tuple
        scores = []
        for word in word_arrays:
            word_score = 0
            for letter in word:
                word_score += letter_counts[letter]
            scores.append(word_score)
        
        return scores

    
    def pick_word(self):
        '''
        Pick a word with the highest score
        '''
        max_score_index = np.argmax(self.word_scores)
        self.last_picked_word = self.possible_words[max_score_index]
        
        return self.last_picked_word

    
    #def filter_words(self,...):
    #    '''
    #    Filter possible words by Wordle feedback of black/yellow/green
    #    '''
    #    pass


                


