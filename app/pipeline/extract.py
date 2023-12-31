import glob  # to list files
import os  # to manage files and folders
from typing import List

import pandas as pd

##Read files from data/input and bring a list of dataframes

# args: input_path (str): path of the folder with files
# return: list of dataframes


def extract_from_excel(path: str) -> List[pd.DataFrame]:
    all_files = glob.glob(os.path.join(path, '*.xlsx'))

    data_frame_list = []
    for file in all_files:
        data = pd.read_excel(file)
        data_frame_list.append(data)

    return data_frame_list


if __name__ == '__main__':
    data_frame_list = extract_from_excel('data/input')
    print(data_frame_list)
