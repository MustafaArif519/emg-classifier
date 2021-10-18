import numpy as np
import pandas as pd
import numpy as np

def load_data(fname):
    data = pd.read_csv(fname, sep='\t', header=0)
    data_comb = pd.DataFrame(columns=(list)(data.columns), dtype=float)
    for index, row in data.iterrows():
        d = row.to_dict()
        data_comb = data_comb.append(d, ignore_index=True)
        print(data_comb)



    dataframe_zero = data[data['class'] == 0].copy()
    dataframe_zero = dataframe_zero.drop(columns=['class', 'time'])
    np_arr = dataframe_zero.to_numpy().ravel()
    x = np_arr.reshape((1, np_arr.shape[0]))
    print(x)
    print(x.shape)

    dataframe_one = data[data['class'] == 1].copy()



def main():
    # arr = None
    # row = np.array([1,2])
    # comb = np.vstack((arr, row)) if (arr is not None) else row
    # print(comb)
    load_data('testing.txt')



if __name__ == "__main__":
    main()