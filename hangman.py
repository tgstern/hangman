#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hangman game with words.txt

@author: tgstern
@author: MITx
"""

import random

WORDLIST_FILENAME = "words.txt"


def loadWords():
    '''
    Returns a list of valid words. Words are strings of lowercase letters.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    '''
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    '''
    return random.choice(wordlist)


# Load the list of words into the variable wordlist
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed; False otherwise
    '''
    for c in secretWord:
        if c in lettersGuessed:
            match = True
        else:
            match = False
            break
    return match


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents what letters in secretWord have been guessed so far.
    '''
    guess = []
    str1 = ''
    for c in secretWord:
        if c not in lettersGuessed:
            guess.append('_ ')
        else:
            guess.append(c)
    return str1.join(guess)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not yet been guessed.
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    remaining = list(alphabet)
    string = ''
    for c in lettersGuessed:
        remaining.remove(c)
    return string.join(remaining)
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    At the start of the game, lets the user know how many letters the secretWord contains.

    After each round, displays to the user the  partially guessed word so far, as well as letters that the user has not yet guessed.

    '''
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + " letters long.")
    print('-------------')
    lettersGuessed = []
    mistakesMade = 0
    while isWordGuessed(secretWord, lettersGuessed) is False and mistakesMade < 8:
        print(getGuessedWord(secretWord,lettersGuessed))
        print('You have ' + str(8 - mistakesMade) + ' guesses left.')
        print('Available letters: ' + getAvailableLetters(lettersGuessed))
        while True:
            guess = input('Please guess a letter: ')
            if guess.isalpha() and len(guess) == 1:
                break
        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter.")
        elif guess in secretWord:
            lettersGuessed.append(guess.lower())
            print('Good guess!')
        else:
            lettersGuessed.append(guess.lower())
            print('Sorry! That letter is not in my word.')
            mistakesMade += 1
        print('-------------')
    if mistakesMade == 8:
        print('Too bad, you ran out of guesses. The word was ' + secretWord)
    elif isWordGuessed(secretWord, lettersGuessed) is True:
        print('Congratulations, you won!')
        print('The word was ' + secretWord)


# executes the hangman game
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
