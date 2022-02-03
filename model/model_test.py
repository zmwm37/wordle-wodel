from model import Wodel
# Test filtering
# test words
test_words = ['MODEL', 'COUNT', 'NYMPH', 'STAGE', 'TRACE']
answer = 'COUNT'
w0 = Wodel(test_words)
w0.pick_word()

test_words = ['ABATE','BREAK', 'COUNT', 'DOUBT', 'EPOCH', 'FLINT', 'GLUED',
    'HINTS', 'IGLOO']
answer = 'COUNT'
w1 = Wodel(test_words)


