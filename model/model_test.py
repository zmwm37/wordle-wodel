from model import Wodel
# Test filtering
# test words
test_words = ['MODEL', 'COUNT', 'NYMPH', 'STAGE', 'TRACE']
answer = 'COUNT'
w0 = model.Wodel(test_words)
w0.pick_word()

test_words = ['ABATE','BREAK', 'COUNT', 'DOUBT', 'EPOCH', 'FLINT', 'GLUED',
    'HINTS', 'IGLOO']
scores = []
for answer in test_words:
    w1 = model.Wodel(test_words)
    print('answer', answer)
    fb = ''
    while fb != 'ggggg':
        print('WORD SCORES', w1.word_scores)
        w1.pick_word()
        fb = w1.compare_answer(answer)
        print('WORD-ANSWER fb',w1.last_picked_word, answer, fb)
        if fb == 'ggggg':
            scores.append(w1.rounds_completed)
        else:
            w1.filter_words(fb)
print('scores:', scores)



test_words = ['BREAK', 'COUNT', 'TREAD']
# expected result {'BREAK':1, 'COUNT': 1, 'TREAD': 2}


