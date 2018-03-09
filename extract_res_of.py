import numpy as np
import pandas as pd


if __name__ == '__main__':

    path_ex = '/home/cedric/Documents/Ergocycle/data/DataEstACd/20180222/Rlt_matt/forceCoeffs1.csv'

    df = pd.read_csv(path_ex)
    df.head()
