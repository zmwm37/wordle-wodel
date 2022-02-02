import model
import time

with open('../data/possible_wordle_words.txt') as f:
    pw = f.readlines()

with open('../data/wordle-answers-alphabetical.txt') as f:
    answers = f.readlines()

pw = [word.rstrip("\n") for word in pw]
answers = [word.rstrip("\n") for word in answers]

start = time.time()
results = []
for answer in answers:
    w = model.Wodel(answers, model = 'uni_letter')
    fb = ''
    while fb != 'ggggg':
        w.pick_word()
        fb = w.compare_answer(answer)
        w.filter_words(fb)
    results.append(w.rounds_completed)
    #print("Word '{}': answered in {} rounds".format(answer, w.rounds_completed))
end = time.time()
print('{} answered in {} seconds with average round of {}'.format(len(answers),end - start, np.mean(results)))

