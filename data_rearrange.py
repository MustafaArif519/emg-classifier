from pathlib import Path
import pandas as pd
import numpy as np

def write_to_csv(dest_path, dataframe, which_class):
    pass

def collect(file_path, which_class, dest_path):
    data = pd.read_csv(file_path, sep='\t', header=0)
    header = (list)(data.columns)
    data_comb = pd.DataFrame(columns=(list)(data.columns), dtype=float)
    start_file = 1
    dest = dest_path / which_class / f'training_{start_file}.txt'
    for index, row in data.iterrows():
        if row['class'] == which_class and index % 2 == 0:
            data_comb.append(row.to_dict(), ignore_index=True)
        else:
            write_to_csv(dest, data_comb, which_class)
            data_comb = pd.DataFrame(columns=header)
            start_file = start_file + 1
            dest = dest_path / which_class / f'training_{start_file}.txt'
    return data


def main():
    dir = Path('.')
    dest = dir / 'EMG_data_ordered_by_class'
    all_dirs = [x for x in dir.iterdir() if x.is_dir()]
    all_test_file_paths = []
    for each in all_dirs:
        all_txt_files = (list)(each.glob('*.txt'))
        all_test_file_paths.append(all_txt_files)
    for i in range(0, 6):
        dataframe = pd.





if __name__ == "__main__":
    main()