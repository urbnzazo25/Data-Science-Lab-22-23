import csv
import string
from math import log
import copy


def file_open(name: str, glt: list):
    n = -1
    with open(name, encoding='utf-8') as f:
        for cols in csv.reader(f):
            if n == -1:
                n += 1
                continue
            elif cols:
                glt.append(cols)
                n += 1
    return n


def tokenize(docs):
    """Compute the tokens for each document.
    Input: a list of strings. Each item is a document to tokenize.
    Output: a list of lists. Each item is a list containing the tokens of the
    relative document.
    """
    tokens = []
    for doc in docs:
        for punct in string.punctuation:
            doc = doc.replace(punct, " ")
        split_doc = [token.lower() for token in doc.split(" ") if token]
        tokens.append(split_doc)
    return tokens


def tf(token_reviews: list, tf_list: list, idf_dict: dict):
    review = {}
    for rev in token_reviews:
        for tok in rev:
            if tok not in review.keys():
                review[tok] = 1
            else:
                review[tok] += 1
            if tok not in idf_dict:
                idf_dict[tok] = 0
        tf_list.append(copy.deepcopy(review))
        review.clear()


def idf(token_reviews: list, idf_dict: dict, n: int):
    for tok in idf_dict.keys():
        for rev in token_reviews:
            if tok in rev:
                idf_dict[tok] += 1
    for tok, num in idf_dict.items():
        idf_dict[tok] = log(n / num)
    return dict(sorted(idf_dict.items(), key=lambda x: x[1], reverse=True))


def td_idf(td_idf_list: list, tf_list: list, idf_dict: dict):
    td_idf_dict = {}
    i = 0
    for rev in tf_list:
        for tok in rev.keys():
            if tok in idf_dict:
                td_idf_dict[tok] = rev[tok] * idf_dict[tok]
        td_idf_list.append(copy.deepcopy(td_idf_dict))
        td_idf_list[i] = dict(sorted(td_idf_dict.items(), key=lambda x: x[1], reverse=True))
        td_idf_dict.clear()
        i += 1

if __name__ == '__main__':
    imdb = []
    reviews = []
    num = file_open("imdb1", imdb)
    for line in imdb:
        reviews.append(line[0])
    token_reviews = tokenize(reviews)
    tf_list = []
    idf_dict = {}
    td_idf_list = []
    tf(token_reviews, tf_list, idf_dict)
    idf_dict = idf(token_reviews, idf_dict, num)
    td_idf(td_idf_list, tf_list, idf_dict)
    print(td_idf_list)
