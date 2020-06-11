# Iteration Liegenschaftszinssatz

import pandas as pd

erg = []
try:
    data = pd.read_csv('dummy.csv', sep=";", decimal=',',
                       dtype={'kp': float,
                              'bk': float,
                              'bw': float,
                              'n': float,})
                              
except FileNotFoundError:
    print('\n Die Datei konnte nicht gefunden werden …')
    print('… das Programm wurde daher beendet.\n')
    quit()

for i, row in data.iterrows():
    lage = data.lage[i]
    ro = data.ro[i]  # Jährl. Rohertrag
    bk = data.bk[i] / 100  # Bewirtschaftungskosten in %
    bw = data.bw[i]  # Bodenwert
    n = data.n[i]  # Restnutzungsdauer
    z = 0.001  # LZ-Iteration
    while True:
        kp = (ro - ro * bk - bw * z) * (pow(z + 1, n) - 1) / (z * pow(z + 1, n)) + bw
        z += 0.00001
        if kp <= data.kp[i]:
            break
    reihe = [lage, kp, ro, bk * 100, bw, n, z * 100]
    erg.append(reihe)

ausgabe = pd.DataFrame(erg)
ausgabe.columns = ['Lage','Kaufpreis', 'Rohertrag', 'BWK', 'Bodenwert', 'RND', 'LZ']
ausgabe.to_csv('dummy-iter.csv', sep=';', decimal=',')
