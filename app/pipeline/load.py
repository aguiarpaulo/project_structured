import os

import pandas as pd


def load_excel(
    data_frame: pd.DataFrame, output_path: str, file_name: str
) -> str:

    """
    Save in a excel file
    args:
    data_frame(pd.DataFrame): dataframe to be saved
    output_path(str): where the file should be saved
    file_name(str): file name to be saved
    """

    if not os.path.exists(output_path):
        os.makedirs(output_path)
    data_frame.to_excel(f'{output_path}/{file_name}.xlsx', index=False)
    return 'File saved successfully'
