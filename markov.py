#!/usr/bin/env python

import sys

# read in a text file give from the command line
def read_in_file():
    args = sys.argv
    script, filename = args
    f = open(filename)
    corpus = f.read()
    # corpus = f.readline()

    return corpus


def print_dict(chain):
    for key,value in chain.iteritems():
        print key,value


def make_uni_grams(corpus):
    # create a dict with a value = word and key = list of words following it
    chain = {}

    # goes through list of words in corpos minus last one
    for i in range(len(corpus)-1):
        word = corpus[i]
        next_word = corpus[i+1]

        # adds following word to list of uni-grams
        if word in chain:
            chain[word].append(next_word)
        else:
            chain[word] = [next_word]

    return chain



def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    # convert string corpus text into list of words without spaces
    # corpus = corpus.replace(',',' ').replace('?',' ').split()
    corpus = corpus.replace(',',' ').replace('?',' ').replace('\t','').split(" ")
    print corpus

    # create a dict with a value = word and key = list of words following it
    chain = {}

    for i in range(len(corpus)-2):
        first_word = corpus[i]
        second_word = corpus[i+1]
        next_word = corpus[i+2]

        key = (first_word,second_word)

        # adds the next word to the tuple key
        if key in chain:
            chain[key].append(next_word)
        else:
            chain[key] = [next_word]

    print_dict(chain)

    return {}

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    return "Here's some random text."

def main():
    corpus = read_in_file()
    
    chain_dict = make_chains(corpus)
    # random_text = make_text(chain_dict)
    # print random_text

if __name__ == "__main__":
    main()