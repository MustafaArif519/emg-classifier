from pathlib import Path
import pandas as pd
import numpy as np

def write_to_csv(dest_path, dataframe):
    # n = len([f for f in dest_path.glob('*')])
    dataframe.to_csv(dest_path, index=False)

def collect(file_path, which_class, dest_path, num):
    data = pd.read_csv(file_path, sep='\t', header=0) # read txt file
    header = (list)(data.columns)
    data_comb = pd.DataFrame(columns=header, dtype=np.float64)
    # I iterate through it manually because the classes are mixed up and you don't know 
    # when class changes
    for index, row in data.iterrows():
        if row['class'] == np.float64(which_class):
            data_comb = data_comb.append(row.to_dict(), ignore_index=True)
        elif len(data_comb) != 0: # write to file whenever there's change in class
            # print(num)
            dest = dest_path / f'training_{num}.txt'
            write_to_csv(dest, data_comb)
            data_comb = pd.DataFrame(columns=header, dtype=np.float64)
            num = num + 1
    return num


def main():
    dir = Path('.')
    dest = dir / 'EMG_data_ordered_by_class'
    if not dest.exists():
        dest.mkdir()
    # create output folders
    for i in range(1, 6):
        p = dest / str(i)
        if not p.exists():
            p.mkdir()
    source = dir / 'EMG_training_raw'
    all_folders = [x for x in source.iterdir() if x.is_dir()]
    all_training_files = []
    # get all txt file from all training folders
    for each in all_folders:
        all_txt_files = (list)(each.glob('*.txt'))
        all_training_files.extend(all_txt_files)
    # print(all_training_files)
    for i in range(1, 6):
        dest_path = dest / str(i)
        num = 1
        for file in all_training_files:
            num = collect(file, i, dest_path, num)


if __name__ == "__main__":
    main()