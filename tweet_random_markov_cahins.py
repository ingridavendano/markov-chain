#!/usr/bin/env python

# Program reads in a txt file to generate random text using Markov
# chains; the random text is used to produce a Twitter status

from sys import argv
from random import choice
from string import ascii_lowercase, punctuation, rstrip
import twitter 


# Twitter API keys go here :-)
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN_KEY = ""
ACCESS_TOKEN_SECRET = ""


def read_file_from_command_line():
    # return a string of text from a file given as an argument
    # in the command line 
    script, file_name = argv
    text = open(file_name)

    corpus = text.read()
    text.close()

    return corpus


def print_chains(chains):
    # prints each chain on a new line
    for key,value in chains.iteritems():
        print key,value


def make_chains(corpus):
    # takes an input text as a string and returns a dictionary 
    # of Markov chains
    corpus = corpus.split()
    chains = {}

    for i in range(len(corpus)-2):
        first_word = corpus[i]
        second_word = corpus[i+1]
        next_word = corpus[i+2]

        # create a bi-gram tuple of words as a key in a chain
        key = (first_word,second_word)

        # adds next_word to the list value of a chain 
        if key in chains:
            chains[key].append(next_word)
        else:
            chains[key] = [next_word]

    return chains


def make_text(chains):
    # takes a dictionary of Markov chains and returns random
    # text based off an original text
    random_text = ""
    tuple_key = choice(chains.keys())
    first_char = tuple_key[0][0][0]

    # checks to see if the starting first character of the chain is
    # capitalized, if it is not then a new starting word is picked
    while first_char in ascii_lowercase or first_char in punctuation:
        tuple_key = choice(chains.keys())
        first_char = tuple_key[0][0][0]

    # adds words from the chain to the sentence 
    while len(random_text + tuple_key[0]) <= 139:
        first_word = tuple_key[0]
        random_text += first_word + " "

        # swaps in tuple pair 
        second_word = tuple_key[1]
        third_word = choice(chains[tuple_key])
        tuple_key = (second_word,third_word)


    # goes through the random_text reversely to remove all characters 
    # until a period is found (denotes end of a sentence)
    for i in range(len(random_text))[::-1]:
        if random_text[i] in ['.', '?', '!']:
            random_text = random_text[:i+1]
            break
        # if there is no punctuation then slap on a period
        if i == 0:
            random_text = rstrip(random_text)
            random_text += '.'

    return random_text


def make_twitter_status(text):
    # creates a Twitter status from random text that has been generated
    api = twitter.Api(consumer_key=CONSUMER_KEY,
consumer_secret=CONSUMER_SECRET, access_token_key=ACCESS_TOKEN_KEY, access_token_secret=ACCESS_TOKEN_SECRET)

    status = api.PostUpdate(text)

    print "Status has been posted to Twitter!"


def main():
    corpus = read_file_from_command_line()
    chains = make_chains(corpus)

    print "Welcome, this program will generate random statuses that you can post to Twitter from the text file you provide."
    run = 'y'

    while run == 'y':
        random_text = make_text(chains)
        print "\n"
        print random_text
        print "\n"

        make_tweet = raw_input("Post status to Twitter? ('y' or 'n') ")
        if make_tweet == 'y':
            make_twitter_status(random_text)

        run = raw_input("Want to post another random status? ('y' or 'n') ")


if __name__ == "__main__":
    main()