import locale
import numpy as np
import matplotlib.pyplot as plt

locale.setlocale(locale.LC_NUMERIC, 'de_De')

fl = locale.atof(input('Wohn/-Nutzfläche [m²]: '))
miete_min = locale.atof(input('minimale Miete [€]: '))
miete_max = locale.atof(input('maximale Miete [€]: '))
bwk_min = locale.atof(input('minimale Bewirtschaftungskosten [%]: '))
bwk_max = locale.atof(input('maximale Bewirtschaftungskosten [%]: '))
bw_min = locale.atof(input('minimaler Bodenwert [€]: '))
bw_max = locale.atof(input('maximaler Bodenwert[€]: '))
rnd_min = locale.atof(input('minimale Restnutzungsdauer[Jahre]: '))
rnd_max = locale.atof(input('maximale Restnutzungsdauer [Jahre]: '))
lz_min = locale.atof(input('minimaler Liegenschaftszins [%]: '))
lz_max = locale.atof(input('maximaler Liegenschaftszins [%]: '))

mu_miete = (miete_min + miete_max) / 2
sd_miete = (miete_max - miete_min) / 3.29
s_miete = np.random.normal(mu_miete, sd_miete, 10000)

mu_bwk = (bwk_min + bwk_max) / 2
sd_bwk = (bwk_max - bwk_min) / 3.29
s_bwk = np.random.normal(mu_bwk, sd_bwk, 10000)

mu_bw = (bw_min + bw_max) / 2
sd_bw = (bw_max - bw_min) / 3.29
s_bw = np.random.normal(mu_bw, sd_bw, 10000)

mu_rnd = (rnd_min + rnd_max) / 2
sd_rnd = (rnd_max - rnd_min) / 3.29
s_rnd = np.random.normal(mu_rnd, sd_rnd, 10000)

mu_lz = (lz_min + lz_max) / 2
sd_lz = (lz_max - lz_min) / 3.29
s_lz = np.random.normal(mu_lz, sd_lz, 10000)

ro = s_miete * fl * 12

ew = (ro - ro * s_bwk / 100 - s_bw * s_lz / 100) * ((s_lz / 100 + 1) ** s_rnd - 1) / \
     (s_lz / 100) / (s_lz / 100 + 1) ** s_rnd + s_bw
mu = float(np.mean(ew))
sd = float(np.std(ew))
print('Verkehrswert, arithm. Mittel (€): {:.0f}'.format(round(mu, -3)))
print('Standardabweichung: ±{:.0f}'.format(round(sd, -3)))
count, bins, ignored = plt.hist(ew, 100, density=True)
plt.plot(bins, 1 / (sd * np.sqrt(2 * np.pi)) * np.exp(- (bins - mu) ** 2 / (2 * sd ** 2)), linewidth=1, color='r')
plt.show()
