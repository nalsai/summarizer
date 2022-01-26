#!/usr/bin/env python3

"""idk"""

import re


def do_stuff(input_text, number_of_sentences):
    """Does stuff, but not yet"""
    # TODO: should probably use a class and make this the __init__ instead

    remove_list = ["a"]     # TODO
    cleaned_text = clean(input_text)
    sentence_list = dissect(cleaned_text)
    for sentence in sentence_list:
        stopword_cleaned_sentence = remove_words(input_text, remove_list)
    # TODO
    return input_text

def clean(input_text):
    """Cleans the text (currently removes line breaks)"""
    return input_text.replace('\n', ' ').replace('\r', '')

def dissect(input_text):
    """Dissects the text into its sentences"""
    return re.findall(r".+[.!?]+ ", input_text)

def remove_words(input_text, remove_list):
    """Removes all words in remove_list from input text."""
    word_list = input_text.split()              # TODO: account for punctuation
    cleaned_list = [word for word in word_list if word not in remove_list]
    return ' '.join(cleaned_list)

def calculate_histogram():
    """Calculates word histogram"""
    pass

def sort_importance():
    """Sorts the sentences by \"importance\""""
    pass
