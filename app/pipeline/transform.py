from typing import List

import pandas as pd

"""
Function for concating all dataframes
"""


def concat_data_frames(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame:
    return pd.concat(data_frame_list, ignore_index=True)
