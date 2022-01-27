# Wordle Algorithm
# Zandr Meitus

# test words
test_words = ['MODEL', 'COUNT', 'NYMPH', 'STAGE', 'TRANCE']

class Wodel(possible_words):
    '''

    '''

    def __init__(self, possible_words, letter_probs):
        self.possible_words = possible_words
        self.letter_probs = self._calc_lettter_probs(self.possible_words)
        self.black_letters = {}
        self.yellow_letters = {}
        self.green_lettesr = {}


    def __repr__(self):
        pass


    def calc_letter_probs(self, possible_words):
    #def calc_letter_probs(possible_words):
        
        word_arrays = []
        word_sets = []
        letter_counts = {}
        for i, word in enumerate(possible_words):
            word_array = []
            word_set = set()
            for j,letter in enumerate(word):
                word_set.add(letter)
                word_array.append(letter)
            
                if j == len(word) - 1:
                    word_arrays.append(word_array)
                    word_sets.append(word_set)

                if letter not in letter_counts:
                    letter_counts[letter] = 1
                else:
                    letter_counts[letter] = letter_counts[letter] + 1
        
        return (word_arrays, word_sets, letter_counts)
    

    def calc_word_score(self, word_tuple):
        word_arrays, word_sets, letter_counts = word_tuple
        scores = []
        for word in word_arrays:
            for letter 

    
    def 

                


