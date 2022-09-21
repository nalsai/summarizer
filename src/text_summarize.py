"""
Summarizes a text, maybe
"""

import nltk

def do_stuff(input_text, number_of_sentences=-1):
    """ Does stuff, but not good yet """

    remove_list = ["a", ".", ","]
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

    #print(sentence_value_dict)
    svd_sorted = dict(sorted(sentence_value_dict.items(), key=lambda x: x[1]))
    return " ".join(x for x in list(svd_sorted)[0:number_of_sentences])


def clean(input_text):
    """ \"Cleans\" the text """
    clean_text = input_text.replace('\n', ' ').replace('\r', '') # remove line breaks
    clean_text = ' '.join(clean_text.split())                     # replace multiple spaces with one
    return clean_text


def sentencize(input_text):
    """ Turns a text into a list of sentences """
    return nltk.tokenize.sent_tokenize(input_text)


def tokenize(input_text):
    """ Turns a text into a list of tokens """
    return nltk.tokenize.word_tokenize(input_text)


def remove_words(input_text, remove_list):
    """ Removes all words in remove_list from input text """
    word_list = input_text.split()
    cleaned_list = [word for word in word_list if word not in remove_list]
    return ' '.join(cleaned_list)
