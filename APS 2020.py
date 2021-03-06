import math

"Dados para cálculo"
Diametro_da_engrenagem = d = 1.2
Espessura_da_engrenagem = L = 0.6
Distancia_dos_mancais = dm = 3
Densidade_do_aco = p = 7850
Torque_da_engrenagem = Teng = 965304      #(16.4e3 * 9.81) * 6
Tensao_de_escoamento = Sy = 530e6         #SAE AISI 5160
Tensao_limite = Srt = 960e6


"Kb para primeira estimativa = 0.9 pois o diâmetro é desconhecido"
Kb = 0.9
"Kc = 1 (torção + flexão)"
Kc = 1
"Kd para 150ºC = 1,025"
Kd = 1.025
"Ke para 90% de confiabilidade = 0.897"
Ke = 0.897
Kf = 1
"Adotando n = 1,5"
n = 1.5
dh = []


for counter in range(10):
    if counter != 0:
        if dh[counter-1] < 1:
            Kb = 1.51 * ((dh[counter-1] * 1000) ** -0.157)
    peso = ((((math.pi * (d ** 2)) / 4) * L) * p) * 9.81
    Ftang = Teng / (d/2)
    Ryb = Ftang / 2
    Rya = Ryb
    T = Ftang * (d/2)
    Mz = Ryb * (dm / 2)
    SnL = 0.5 * Srt / 1e6
    Ka = 4.51 * ((Srt / 1e6) ** -0.265)
    Sn = (Ka * Kb * Kc * Kd * Ke * SnL) * 1e6
    "Kts = 0.669 * (r/d) ** -0.357, foi adotado 0.02 para r/d"
    Kts = 0.669 * (0.02 ** -0.357)
    Kfs = Kts
    My = Ryb * (dm/2)
    Mz = Ftang * (dm / 2)
    Ma = ((My ** 2) + (Mz ** 2)) ** (1 / 2)
    a = ((16*n)/math.pi)
    b = (1/Sn) * ((4*((Kf*Ma)**2))**(1/2))
    c = (1/Sy) * (3 * ((Kfs * T / 0.59) ** 2)) ** (1/2)
    dh.append((a * (b + c)) ** (1/3))
    print(f"d{counter} = {dh[counter]}")
    if counter != 0:
        e = (dh[counter] - dh[counter-1]) / dh[counter-1]
        print(f"e = {e}")
        if e < 0.01:
            break
