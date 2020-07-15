"""Generate Markov text from text files."""

import sys
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    return open(file_path).read()


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # Creating a big list of all the words in the text
    words_list = text_string.split()

    n = 3

    # Going through list using its indices
    for i in range(len(words_list)-n):
        # make tuple
        # tuple made out of the words_list words at indices i to i+(n-1)
        ngram_as_list = []

        ngram_as_list = [words_list[num] for num in range(i,(i+n))]

        # recursively make a list
       # while counter < n:
       #      ngram_as_list.append(words_list[i])
       #      counter += 1 

        # create a tuple from that list
        ngram = tuple(ngram_as_list)

        # get next word after tuple
        next_word = [words_list[i+n]]
        
        # use get to check for if key is already present
        # add them as a pair to the dictionary, tuple as the key, list as value
        chains[ngram] = chains.get(ngram, []) + next_word

    return chains


def make_text(chains):
    """Return text from chains."""


    # start somewhere
    ngram = choice(list(chains.keys()))

    # start list with first two words
    words =list(ngram)

    while ngram in chains:        
        # use tuple as key to get list of next words
        # choose a next word with 'choice' (returns words as a string)
        next_word = choice(chains[ngram])
        
        # add chosen word to words list
        words.append(next_word) 

        # make new key from second tuple item and chosen word
        
        # make ngram from tuple to list
        ngram_list = list(ngram)

        # make slice from 1 to last
        ngram_slice = ngram_list[1:]
    
        # add our chosen word to the slice
        ngram_slice.append(next_word)

        # consciously re-tuple our list
        ngram = tuple(ngram_slice)

    return " ".join(words)



input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
