import pandas as pd
# import matplotlib.pyplot as plt
import numpy as np

Cx = []
df = pd.read_csv('./forceCoeff_grossier.csv')
df2 = pd.read_csv('./forceCoeef_fin.csv')

Cx.append(df['Cd'])
Cx.append(df2['Cd'])

for elt_cx in Cx:
    elt_cx = np.array(elt_cx)
    print(np.mean(elt_cx[75:]))
