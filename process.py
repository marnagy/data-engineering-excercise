import pandas as pd
import numpy as np

PHRASES_FILENAME = 'phrases.csv'

def main() -> None:
    # load distinct words from file
    words = dict()
    with open(PHRASES_FILENAME, 'r') as phrases_file:
        for i, line in enumerate(phrases_file):
            if i == 0:  # skip first line (header)
                continue
            # line_parts = line.strip('\n')
            # if line_parts[-1] == '?':
            #     line_parts = line_parts[:-1] + ' ?'
            for word in line.strip('\n').split():
                words[word] = None
    
    # assign number to each word
    with open(VECTORS_FILENAME, 'r') as vecs_file:
        words_amount, vec_size = -1, -1
        for i, line in enumerate(vecs_file):
            if i == 0:
                # preallocatte matrix 


if __name__ == '__main__':
    main()
