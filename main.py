import numpy as np
from utls.extract_data import extract_from_int
from model_perf.model_acd import est_wind
from model_perf.model_acd import model_grappe
from skcycling.io import bikeread

if __name__ == '__main__':

    # défénition where interesting data are
    l_d_int = [[0, 31, 16],
               [0, 34, 41],
               [0, 38, 30],
               [0, 41, 9],
               [0, 44, 56],
               [0, 47, 30],
               [0, 52, 3],
               [0, 54, 25],
               [0, 58, 41],
               [1, 0, 50],
               [1, 4, 39],
               [1, 7, 29]]

    l_f_int = [[0, 32, 53],
               [0, 35, 52],
               [0, 39, 43],
               [0, 42, 55],
               [0, 45, 57],
               [0, 48, 13],
               [0, 53, 3],
               [0, 55, 56],
               [1, 0, 0],
               [1, 1, 46],
               [1, 5, 52],
               [1, 8, 9]]

    path_ex = '/home/cedric/Documents/Ergocycle/data/DataEstACd/20180222/'

    data = bikeread(path_ex + '2018-02-22-11-16-31.fit')
    p = data['power']
    s = data['speed']

    l_power, l_speed = extract_from_int(p, s, l_d_int, l_f_int)

    l_power_mean = []
    l_speed_mean = []
    # for i in range(len(l_power)):
    #     np.array(l_power[i])
    #     np.array(l_speed[i])

    #     l_power_mean.append(np.mean(l_power[i]))
    #     l_speed_mean.append(np.mean(l_speed[i]))

    l_power_mean = [93, 187, 149, 269, 229, 327, 122, 200, 144, 259, 196, 328]
    l_speed_mean = [25.4, 25.4, 29.8, 28.7, 34.3, 32.9, 26.8, 24.4, 30.2, 31.9,
                    34.6, 35.3]
    l_speed_mean = np.array(l_speed_mean) / 3.6
    l_ACd = []
    l_wind = []

    for i in range(len(l_power)):
        if i % 2 == 0:
            val_wind = est_wind(l_power_mean[i], l_power_mean[i+1],
                                l_speed_mean[i], l_speed_mean[i+1])
            l_wind.append(val_wind)

    np.array(l_wind)
    wind_mean = np.mean(l_wind)

    for i in range(len(l_power_mean)):
        # back wind
        if i % 2 == 0:
            val_acd = model_grappe(l_power_mean[i], l_speed_mean[i],
                                   l_wind[int(i/2)], 4, 1010, 0.0035, 100)
        # front wind
        else:
            val_acd = model_grappe(l_power_mean[i], l_speed_mean[i],
                                   -l_wind[int(i//2)], 4, 1010, 0.0035, 100)

        l_ACd.append(val_acd)
