import model
import time
import numpy as np

with open('../data/possible_wordle_words.txt') as f:
    pw = f.readlines()

with open('../data/wordle-answers-alphabetical.txt') as f:
    answers = f.readlines()

pw = [word.rstrip("\n") for word in pw]
answers = [word.rstrip("\n") for word in answers]
#answers = ['shard']
for type in ['basic','uni_letter','word_count','wc + lp']:
    start = time.time()
    results = []
    for answer in answers:
        w = model.Wodel(pw, model = type) # 'basic', 'word_count', 'wc + lp', 'uni_letter'
        fb = ''
        while fb != 'ggggg':
            #print('rds completed', w.rounds_completed)
            w.pick_word()
            #print('rds completed', w.rounds_completed)
            #print('picked word',w.last_picked_word)
            fb = w.compare_answer(answer)
            #print(fb)
            w.filter_words(fb)
        results.append(w.rounds_completed)
        #print("Word '{}': answered in {} rounds".format(answer, w.rounds_completed))
    end = time.time()
    print('{}: {} answered in {} seconds with average round of {}'.format(type, len(answers),end - start, np.mean(results)))

# 2/3/22 OUTPUT
#basic: 2315 answered in 126.25859212875366 seconds with average round of 5.374946004319654
#uni_letter: 2315 answered in 131.40263509750366 seconds with average round of 5.352051835853132
#word_count: 2315 answered in 116.50977516174316 seconds with average round of 5.729157667386609
#wc + lp: 2315 answered in 128.64878106117249 seconds with average round of 5.32829373650108
