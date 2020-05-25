
#!/usr/local/bin/python3

#  20.05.2020 

ro = 8.80 * 430 * 12 # Rohertrag (Monatsmiete * WFL * Monate)
bw = 170000       # Bodenwert (Bodenrichtwert: 550€/m²)
n  = 30           # Restnutzungsdauer
bk = 0.20         # Bewirtschaftungskosten %/100
z  = 0.03     # Liegenschaftszinssatz %/100

# Ertragswertberechnung
ew = (ro - ro * bk - bw * z) * (pow(z + 1, n) - 1) / (z * pow(z + 1, n)) + bw

vf = ew / ro
print("\nDer Ertragswert beträgt ", ew, "€")
print("\nDas Vielfache beträgt das ", vf, "-fache")
