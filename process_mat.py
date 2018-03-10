import pandas as pd
# import matplotlib.pyplot as plt
import numpy as np

name_file = ["forceCoeffs_25_3.csv", "forceCoeffs_34_55.csv",
             "forceCoeff_30_55.csv"]

path_dir = "/home/cedric/Documents/Ergocycle/data/DataEstACd/20180305/"

Cx = []

for fichier in name_file:

    df = pd.read_csv(path_dir + fichier)
    Cx.append([df['Cd'], fichier])


for elt_cx in Cx:
    data_cx = np.array(elt_cx[0])
    print(elt_cx[1], " : ", np.mean(data_cx[75:]))
