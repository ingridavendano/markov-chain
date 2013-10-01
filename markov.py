#!/usr/bin/env python

import sys
import random
import string

# read in a text file give from the command line
def read_in_file():
    args = sys.argv
    script, filename = args
    f = open(filename)
    corpus = f.read()
    f.close()

    return corpus


def print_dict(chain):
    for key,value in chain.iteritems():
        print key,value


# def make_uni_grams(corpus):
#     # create a dict with a value = word and key = list of words following it
#     chain = {}

#     # goes through list of words in corpos minus last one
#     for i in range(len(corpus)-1):
#         word = corpus[i]
#         next_word = corpus[i+1]

#         # adds following word to list of uni-grams
#         if word in chain:
#             chain[word].append(next_word)
#         else:
#             chain[word] = [next_word]

#     return chain



def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    # convert string corpus text into list of words without spaces
    # corpus = corpus.replace(',',' ').replace('?',' ').split()
    # corpus = corpus.replace(',',' ').replace('?',' ').replace('\t','').split(" ")
    corpus = corpus.split()
    # print corpus

    # create a dict with a value = word and key = list of words following it
    chains = {}

    for i in range(len(corpus)-2):
        first_word = corpus[i]
        second_word = corpus[i+1]
        next_word = corpus[i+2]

        key = (first_word,second_word)

        # adds the next word to the tuple key
        if key in chains:
            chains[key].append(next_word)
        else:
            chains[key] = [next_word]

    # print_dict(chains)

    return chains


def make_text(chain):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    starting_point = random.choice(chain.keys())
    first_char = starting_point[0][0][0]

    while first_char in string.ascii_lowercase or first_char in string.punctuation:
        starting_point = random.choice(chain.keys())
        first_char = starting_point[0][0][0]

    sentence = ""

    while len(sentence) < 200:
        first_word = starting_point[0]
        second_word = starting_point[1]
        third_word = random.choice(chain[starting_point])
        sentence += first_word + " " 

        starting_point = (second_word,third_word)

        if starting_point not in chain.keys():
            sentence += second_word + " " + third_word + " "
            break

    return sentence


def main():
    corpus = read_in_file()
    
    chain_dict = make_chains(corpus)
    random_text = make_text(chain_dict)
    print random_text


if __name__ == "__main__":
    main()