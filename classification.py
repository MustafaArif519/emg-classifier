import numpy as np
import pandas as pd
from pathlib import Path

def load_data_into_feature_matrix(fname, row_size, path):
    data = pd.read_csv(fname, sep='\t', header=0, skiprows=1)
    data = data.iloc[:row_size].values.ravel() # one row of feature matrix
    print(data)





def main():
    arr = [1,2]
    arr2 = [2,3]
    comb = np.vstack((arr, arr2))
    print(comb)
    # arr = None
    # row = np.array([1,2])
    # comb = np.vstack((arr, row)) if (arr is not None) else row
    # print(comb)
    row_size = 3
    path = Path('.')
    load_data('testing.txt', row_size)



if __name__ == "__main__":
    main()