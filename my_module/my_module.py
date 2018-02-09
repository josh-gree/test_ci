import pandas as pd
import numpy as np


def random_df(N=100,columns=None):
    

    if columns is None:
        raise ValueError("Must pass a list of columns")

    k = len(columns)
    data = np.random.rand(N,k)

    return pd.DataFrame(data=data,columns=columns)

columns = list('ABCD')
df1 = random_df(columns=columns)
df2 = random_df(columns=columns)