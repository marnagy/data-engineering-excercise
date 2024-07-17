# pip
import pandas as pd
import numpy as np
from numpy.linalg import norm  # euclidean distance

# custom
from custom_lib import PHRASES_FILENAME, VECTORS_FILENAME, NORMALIZED_PHRASES, PHRASE_DISTANCES
from custom_lib import load_phrases, load_vectors, load_normalized_phrases

# standard lib
from typing import List

def main() -> None:
    # load distinct words from file
    phrases: List[List[str]] = load_phrases()
    
    # assign number to each word
    word_to_index, master_arr = load_vectors()

    # compute normalized sum for each phrase
    normalized_sums = load_normalized_phrases()

    # compute distances of phrases
    distances = np.zeros(shape=(len(phrases), len(phrases)))
    for i in range(len(phrases)):
        for j in range(i+1, len(phrases) - (i+1)):
            dist = norm(normalized_sums[i] - normalized_sums[j])
            distances[i,j] = dist
            distances[j,i] = dist
    
    print("distance computed.")

    np.save(PHRASE_DISTANCES, distances)


if __name__ == '__main__':
    main()
