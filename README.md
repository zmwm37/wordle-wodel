# wordle-wodel
Building algorithm for Wordle

<a href = 'https://github.com/zmwm37/wordle-wodel.git'>Wordle</a> is an English word game developed by Josh Wardle that involves trying to guess a five letter word in 6 or fewer guesses. There are 12,972 accepted wordle answers that are English words with 5 letters. The game can be played once a day with a new answer each day.

My goal is to build an algorithm that can successfully guess the word in 6 or fewer attempts each day.

The file possible_wordle_words.txt was created by combining and alphabatizing the lists of accepted words and answer words posted by <a href = 'https://gist.github.com/cfreshman'>Cyrus Freshman</a> on his Github. 

## The Models
The current versions of the model are combinations of basic probabilities:
- The frequency that a given letter occurs in the all possible words.  
$$\sum_{n=1}^{5} l_{i}$$
- The frequency that a given letter occurs in all possible words in position $j$
$$\sum_{i=1}^{5} \mathrm(l_{ij} \mid j=i)$$
- The sum of the number of possible words that the $i^{th}$ letter occurs in.
$$\sum_{n=1}^{5} w_{i}$$

- The number of unique letters in a word, $\theta(l)$
$$\theta(l_{i}) = \{l_{i}\}_{i \in \{1,...5\}}$$

Model versions:
- Basic  
$$\sum_{n=1}^{5} l_{i} + {i=1}^{5} \mathrm(l_{ij} \mid j=i)$$

- Uni Letter  
$$\sum_{n=1}^{5} l_{i} + {i=1}^{5} \mathrm(l_{ij} \mid j=i) + \theta(l_{i})$$

- Word Count  
$$\sum_{n=1}^{5} w_{i}$$

- Word Count + Letter Position
$$\sum_{n=1}^{5} w_{i} + {i=1}^{5} \mathrm(l_{ij} \mid j=i)$$


## Dev Tasks
- Select start word or word after no matches  
- Pick word from exact matching list (greens only, no yellow)  
- Pick word from partial match (only yellows)  
- Pick word from combined partial-exact matching list (greens and yellows)  
- Interface for taking input and displaying guessed word  
