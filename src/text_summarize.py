#!/usr/bin/env python3

"""idk"""
# TODO: the data should be shipped with the app if possible
# nltk.download('punkt')

import re
import nltk

use_nltk_tokenization = True    # non nltk sentencization doesn't work yet


def do_stuff(input_text, number_of_sentences=-1):
    """Does stuff, but not good yet"""
    # TODO: use a class and make this the __init__

    remove_list = ["a", ".", ","]     # TODO: file with more data
    cleaned_text = clean(input_text)
    freq_dist = nltk.FreqDist(
        tokenize(remove_words(cleaned_text, remove_list)))
    sentence_list = sentencize(cleaned_text)
    sentence_value_dict = {}
    for sentence in sentence_list:
        value = 0
        tokens = tokenize(remove_words(sentence, remove_list))
        for token in tokens:
            value += freq_dist[token]
        sentence_value = value / len(tokens)
        sentence_value_dict[sentence] = sentence_value

    if number_of_sentences < 1:
        number_of_sentences = round(len(sentence_list)/3)+1

    print(sentence_value_dict)
    # TODO: using a dictionary and sorting it changes the sentence order. This should not happen, or should it?
    svd_sorted = dict(sorted(sentence_value_dict.items(), key=lambda x: x[1]))
    return " ".join(x for x in list(svd_sorted)[0:number_of_sentences])


def clean(input_text, clean_punctuation=False):
    """\"Cleans\" the text"""
    if clean_punctuation:
        input_text = input_text.replace('.', '')    # TODO
    return input_text.replace('\n', ' ').replace('\r', '').replace('  ', ' ')


def sentencize(input_text):
    """Turns a text into a list of sentences"""
    if use_nltk_tokenization:
        return nltk.tokenize.sent_tokenize(input_text)
    else:
        return re.findall(r".+[.!?]+ ", input_text)  # TODO


def tokenize(input_text):                            # TODO: better tokenization
    """Turns a text into a list of tokens"""
    if use_nltk_tokenization:
        return nltk.tokenize.word_tokenize(input_text)
    else:
        return input_text.split()


def remove_words(input_text, remove_list):
    """Removes all words in remove_list from input text."""
    word_list = input_text.split()
    cleaned_list = [word for word in word_list if word not in remove_list]
    return ' '.join(cleaned_list)
