# pip
import pandas as pd
import numpy as np
from numpy.linalg import norm  # euclidean distance

# standard lib
from typing import List, Optional, Tuple, Dict
import os

PHRASES_FILENAME = 'phrases.csv'
VECTORS_FILENAME = 'vectors.csv'
NORMALIZED_PHRASES = 'normalized_phrases.npy'
PHRASE_DISTANCES = 'phrase_distances.npy'

# windows default txt encoding
# some words are still not read correctly (why not utf-8 though?)
ENCODING = 'cp1252'

def load_phrases() -> List[List[str]]:
    phrases: List[List[str]] = list()
    with open(PHRASES_FILENAME, 'r', encoding=ENCODING) as phrases_file:
        for i, line in enumerate(phrases_file):
            # print(line)
            if i == 0:  # skip first line (header)
                continue
            phrase_words = list(map(lambda x: x.lower(), line.strip('\n').split()))
            if phrase_words[-1][-1] == '?':
                phrase_words[-1] = phrase_words[-1][:-1]

            phrases.append(phrase_words)
    return phrases

def load_normalized_phrases() -> np.ndarray:
    if NORMALIZED_PHRASES in os.listdir():
        normalized_phrases = np.load(NORMALIZED_PHRASES)
        return normalized_phrases
    
    normalized_sums = list()
    for phrase in phrases:
        ## skip words not found in vectors.csv
        vecs = np.array([ master_arr[word_to_index[word]] for word in phrase if word in word_to_index])
        summed = np.sum(vecs, axis=0)  # sum columns
        normalized_sums.append(summed / norm(summed))
    print("Phases summed and normalized.")
    normalized_phrases = np.array(normalized_sums)
    np.save(NORMALIZED_PHRASES, normalized_phrases)
    return normalized_phrases

def load_vectors() -> Tuple[Dict[str, int], np.ndarray]:
    # assign vector to each word
    master_arr = None
    word_to_index = dict()
    #print("Loading vectors...")
    words_amount, vec_size = None, None
    with open(VECTORS_FILENAME, 'r', encoding='utf-8') as vecs_file:
        for i, line in enumerate(vecs_file):
            if i % 1_000 == 0:
                print(f"{i * 100 / words_amount :.1f} %" if words_amount is not None else " ", end='\r')
                pass

            if i == 0:
                words_amount, vec_size = list(map(int, line.strip('\n').split()))
                # preallocatte matrix for words
                # print(words_amount, vec_size)
                master_arr = np.empty(shape=(words_amount, vec_size))
                continue
            line_parts = line.strip('\n').split()
            word = line_parts[0]
            try:
                try:
                    temp = float(word)
                    continue  #! word cannot be a number
                except:
                    # print(len(line_parts))
                    assert len(line_parts) == 1 + vec_size
                    index = i - 1
                    word_to_index[word] = index
                    master_arr[index] = np.array(list(map(float, line_parts[1:])))
            except:
                print(i, line)
                exit()
    return word_to_index, master_arr