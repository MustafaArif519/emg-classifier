import pandas as pd
import os

def get_ring_dataset():
    fileList = []
    personNum = ""
    for i in range (1, 37):
        if i < 10:
            personNum = "0" + str(i)
        else:
            personNum = str(i)
        smallList = os.listdir("EMG_data_for_gestures-master/" + personNum)
        for i in range(2):
            smallList[i] = "EMG_data_for_gestures-master/" + personNum + "/" + smallList[i]

    fileList.extend(smallList)
    df_list = [pd.read_table(file) for file in fileList]
    raw_df = pd.concat(df_list)
    return raw_df