# pip
import pandas as pd
import numpy as np
from numpy.linalg import norm  # euclidean distance

# custom
from custom_lib import PHRASES_FILENAME, VECTORS_FILENAME, NORMALIZED_PHRASES, PHRASE_DISTANCES
from custom_lib import load_phrases, load_vectors, load_normalized_phrases

# standard lib
from typing import List, Optional, Tuple, Dict
import os


def get_closest_phrases(any_str: str,
        phrases: Optional[List[List[str]]] = None,
        normalized_phrases: Optional[np.ndarray] = None,
        word_to_index: Optional[Dict[str, int]] = None,
        master_arr: Optional[np.ndarray] = None) -> List[float]:
    if phrases is None:
        phrases = load_phrases()
    
    if normalized_phrases is None:
        normalized_phrases = load_normalized_phrases()
    
    if word_to_index is None or master_arr is None:
        word_to_index, master_arr = load_vectors()

    user_words = list(map(lambda x: x.lower(), any_str.split()))
    ## skip words not found in vectors.csv
    user_vecs = np.array([ master_arr[word_to_index[word]] for word in user_words if word in word_to_index])
    user_summed = np.sum(user_vecs, axis=0)  # sum columns
    user_normalized_vec = user_summed / norm(user_summed)

    distances_to_phrases = [
        norm(user_normalized_vec - normalized_phrases[i])
        for i in range(len(phrases))
    ]
    return distances_to_phrases

def main() -> None:
    user_input = input("Input your phrase: ")
    phrases = load_phrases()
    phrase_distances = get_closest_phrases(user_input, phrases=phrases)
    print(f"Closes original phrase to your phrase: {' '.join(phrases[np.argmin(phrase_distances)])}")
    print(f"Distance: {min(phrase_distances)}")


if __name__ == '__main__':
    main()
