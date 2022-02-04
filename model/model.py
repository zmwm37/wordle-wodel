# Wordle Algorithm
# Zandr Meitus

import numpy as np


class Wodel(object):
    '''

    '''

    def __init__(self, possible_words, model = 'basic',round_limit = None):
        self.possible_words = possible_words
        self.model_type = model
        self.letter_probs = self.calc_letter_probs()
        self.word_scores = self.calc_word_scores()
        self.black_letters = {}
        self.yellow_letters = {}
        self.green_lettesr = {}
        self.last_picked_word = None
        self.rounds_completed = 0
        self.round_fb = {}
        self.picked_words = []


    def __repr__(self):
        pass


    def calc_letter_probs(self):
        '''
        '''
        letter_index = {}
        letter_position_index = {}
        letter_word_counts = {}
        letter_counts = {}
        lp_counts = {}
        for i, word in enumerate(self.possible_words):
            unique_letters = set()
            for j,letter in enumerate(word):
                if letter not in letter_index:
                    letter_index[letter] = {i}
                    letter_counts[letter] = 1
                    letter_word_counts[letter] = 1
                else:
                    letter_index[letter].add(i)
                    letter_counts[letter] += 1
                    if letter not in unique_letters:
                        letter_word_counts[letter] += 1
                unique_letters.add(letter)
                    
                
                lp = letter + str(j)
                if lp not in letter_position_index:
                    letter_position_index[lp] = {i}
                    lp_counts[lp] = 1
                else:
                    letter_position_index[lp].add(i)
                    lp_counts[lp] += 1
        
        return (letter_index, letter_position_index,letter_word_counts,
            lp_counts, letter_counts)


    def calc_word_scores(self):
        #_, _, lw_counts, lp_counts, letter_counts = self.letter_probs
        match_counts = {}
        scores = {}
        for i, word in enumerate(self.possible_words):
            for answer_word in self.possible_words[(i + 1):]:
                uni_letters = set()
                for letter in word:
                    if letter in answer_word and letter not in uni_letters:
                        if match_counts.get(word) is None:
                            match_counts[word] = 1
                        else:
                            match_counts[word] += 1
                        
                        matches = match_counts[word]
                        scores[word] = matches * (len(self.possible_words) - matches)
                            
                        if match_counts.get(answer_word) is None:
                            match_counts[answer_word] = 1
                        else:
                            match_counts[answer_word] += 1
                        
                        aw_matches = match_counts[answer_word]
                        scores[answer_word] = aw_matches * (len(self.possible_words) - aw_matches)
                            
                        break
                    uni_letters.add(letter)
                    
        return scores
                ## score on letter frequency and position letter frequency
                #if self.model_type == 'basic':
                #    word_score += letter_counts[letter] + lp_counts[letter + str(i)]
                ## same as basic with small weight added for number of unique letters
                #elif self.model_type == 'uni_letter':
                #    word_score += letter_counts[letter] + lp_counts[letter + str(i)]
                #    if letter not in uni_letters:
                #        word_score += 1
                #    uni_letters.add(letter)
                ## instead of total letter frequency, use words that letter appears in
                #elif self.model_type == 'word_count':
                #    word_score += lw_counts[letter]
                ## word count plus letter position frequnecy
                #elif self.model_type == 'wc + lp':
                #    word_score += lw_counts[letter] + lp_counts[letter + str(i)]
            #scores.append(word_score)
        
        #return scores

    
    def pick_word(self):
        '''
        Pick a word with the highest score
        '''
        if len(self.possible_words) ==  1:
            self.last_picked_word = self.possible_words[0]
        else:
            self.last_picked_word = max(self.word_scores, 
                key = self.word_scores.get)
        self.picked_words.append(self.last_picked_word)
        self.rounds_completed += 1
        
        return self.last_picked_word


    def compare_answer(self, answer):
        '''
        Compare the last picked word to the answer.
        '''
        fb = ''
        for i, letter in enumerate(self.last_picked_word):
            if letter not in answer:
                fb += 'b'
            elif letter != answer[i]:
                fb += 'y'
            else:
                fb += 'g'
        self.round_fb[self.rounds_completed] = fb
        #if fb == 'ggggg':
            #print('Winning word', self.last_picked_word)
            #print('Won in {} rounds'.format(self.rounds_completed))
            #print('All words selected:', self.picked_words)
        
        return fb

    
    def filter_words(self, feedback):
        '''
        Filter possible words by Wordle feedback of black/yellow/green

        Inputs:
            feedback: string of length 5 consisting of 'b', 'y', and 'g':
                'b': letter not in word
                'y': letter in word, but not in correct position
                'g': letter in word and in correct position
        '''
    #    Create two dictionaries: one of letter keys and list of word index values,
    #    the other of letter-position keys(e.g. S2, A0) and list of word index values.
    #    These can be used to more quickly filter possible words.
        letter_index, letter_position_index, _, _, _ = self.letter_probs
        remaining_index = range(len(self.possible_words)) 
       # print('remaining words', remaining_index)
        for i, letter in enumerate(feedback):
            picked_letter = self.last_picked_word[i]
            picked_lp = picked_letter + str(i)
            if letter == 'b':
                #print(i, 'B GATE', letter)
                exclude = letter_index[picked_letter]
                remaining_index = \
                    [i for i in remaining_index if i not in exclude]
                #print('remaining words', remaining_index)
            elif letter == 'y':
                #print(i, 'Y GATE', letter)
                exclude = letter_position_index[picked_lp]
                include = letter_index[picked_letter]
                remaining_index = [i for i in remaining_index \
                    if i in include and i not in exclude]
                #print('remaining words', remaining_index)
            elif letter == 'g':
                #print(i, 'G GATE', letter)
                include = letter_position_index[picked_lp]
                remaining_index = [i for i in remaining_index if i in include]
                #print('remaining words', remaining_index)
        
        self.possible_words = [self.possible_words[i] for i in remaining_index]
        self.letter_probs = self.calc_letter_probs()
        self.word_scores = self.calc_word_scores()




                


