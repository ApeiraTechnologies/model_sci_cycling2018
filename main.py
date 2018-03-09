import numpy as np
from utls.extract_data import extract_from_int
from model_perf.model_acd import est_wind
from model_perf.model_acd import inv_model_grappe_ACd
from model_perf.model_acd import inv_model_grappe_F
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
    # l_power_mean = [93, 187, 149, 269, 229, 327, 122, 200,
    # 144, 259, 196, 328]
    # l_speed_mean = [25.4, 25.4, 29.8, 28.7, 34.3, 32.9, 26.8,
    # 24.4, 30.2, 31.9,

    l_power_mean = [117, 139, 165, 212, 240, 283, 124, 146, 156, 214, 226, 278]
    l_speed_mean = [25.1, 25.5, 30.5, 30.6, 34.8, 34.3, 27.1, 26.9, 31.3, 30.3,
                    34.8, 34.7]
    l_speed_mean = np.array(l_speed_mean) / 3.6
    l_power_mean = np.array(l_power_mean) * 0.9
    l_ACd = []
    l_f_aero = []
    l_wind = []

    for i in range(len(l_power)):
        if i % 2 == 0:
            val_wind = est_wind(l_power_mean[i], l_power_mean[i+1],
                                l_speed_mean[i], l_speed_mean[i+1])
            l_wind.append(val_wind)

    np.array(l_wind)
    wind_mean = np.mean(l_wind)

    for i in range(len(l_power_mean)):
        val_acd = inv_model_grappe_ACd(l_power_mean[i], l_speed_mean[i],
                                       0, 10, 990, 0.004, 100)
        val_f_aero = inv_model_grappe_F(l_power_mean[i], l_speed_mean[i],
                                        0.004, 100)
        l_f_aero.append(val_f_aero)
        l_ACd.append(val_acd)

        l_ACd_f = []
    for i in range(len(l_power_mean)):
        if i % 2 == 0:
            moy_acd = (l_ACd[i] + l_ACd[i+1]) / 2
            moy_f = (l_f_aero[i] + l_f_aero[i+1]) / 2
            l_ACd_f.append([moy_acd, moy_f])

    print("Valeur main en haut : 25, 30, 35km/h / ACd - F")
    for i in range(3):
        print(l_ACd_f[i][0], " - ", l_ACd_f[i][1])

    print("Valeur main en bas : 25, 30, 35km/h / ACd - F")
    for i in range(3):
        print(l_ACd_f[i+3][0], " - ", l_ACd_f[i+3][1])
