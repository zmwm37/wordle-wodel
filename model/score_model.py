import model
import time
import numpy as np

with open('../data/possible_wordle_words.txt') as f:
    pw = f.readlines()

with open('../data/wordle-answers-alphabetical.txt') as f:
    answers = f.readlines()

pw = [word.rstrip("\n") for word in pw]
#answers = [word.rstrip("\n") for word in answers[0:10]]
#answers = ['pleat']
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

# 2/8/22 OUTPUT
#basic: 2315 answered in 187.59355878829956 seconds with average round of 4.377969762419006
#uni_letter: 2315 answered in 201.57207489013672 seconds with average round of 4.380993520518358
#word_count: 2315 answered in 171.2969229221344 seconds with average round of 4.567170626349892
#wc + lp: 2315 answered in 206.07487106323242 seconds with average round of 4.377105831533477
