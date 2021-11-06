import sys
import numpy as np
import pandas as pd
import argparse
from pathlib import Path

HEIGHT = 8
WIDTH = 1200

def trim(path, dest):
    files = (list)(path.glob('*.txt'))
    start = 0
    i = 0
    while start != 30 and i != len(files):
        dataframe = pd.read_csv(files[i], header=0, dtype=np.float64)
        if dataframe.shape[0] < WIDTH:
            print("Found file less than 1200 data, change file")
            i += 1
            continue
        dataframe = dataframe.drop(['class', 'time'], axis=1)
        dataframe = dataframe.iloc[:WIDTH, :]
        print(dataframe.shape)
        file_name = dest / f'trimmed_{start}.txt'
        dataframe.to_csv(file_name, header=False, index=False)
        start += 1
        i += 1

if __name__ == '__main__':
    p = Path('./EMG_data_ordered_by_class')
    dest = Path('./EMG_data_trimmed')
    if not dest.exists():
        dest.mkdir()
    for i in range(1, 6):
        pp = dest / str(i)
        if not pp.exists():
            pp.mkdir()
    for i in range(1, 6):
        trim(p / str(i), dest / str(i))
