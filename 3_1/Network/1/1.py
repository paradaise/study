import math

# Входные данные вариант №4
p_vh = -6  # дБ, уровень мощности на входе передатчика
S_per = 13  # дБ, коэффициент усиления передатчика
L = 160  # км, длина канала
a = 1.6  # дБ/км, затухание на 1 километр дистанции
S = 23  # дБ, коэффициент усиления промежуточного усилителя
S_pr = 7  # дБ, коэффициент усиления приемника
p_pom = -18  # дБ, уровень помехи
A = 4  # дБ, защищенность от помех
p_vyh = -8  # дБ, уровень мощности на выходе приемника

# 1. Уровень передачи(p_per)
p_per = p_vh + S_per
print(f"Уровень передачи (P_per): {p_per} дБ")
# 7. Количество промежуточных усилителей(N)
N = math.ceil(((p_vyh - p_vh + a * L) - (S_per + S_pr))/S)

# 2. Минимальный уровень сигнала на входе i-го усилителя (pпрi):
print(f"Минимальный уровень сигнала на входе i-го усилителя (P_pr)): {p_pom + A } дБ")

# 3. Затухание на участке длиной l (Ai):
Ai = a * L / (N + 1)
print(f"Затухание на каждом участке (A): {Ai:.2f} дБ")

# 4. Длина i-го участка (li):
li = L / (N + 1)
print(f"Длина каждого участка (l): {li:.2f} км")

# 5. Уровень сигнала на входе приемника (pпр):
print(f"Уровень сигнала на входе приемника (P_pr): {p_vyh - S_pr} дБ")

# 6. Длина оконечного участка канала передачи данных:
L_last = L - (N*li)
print(f"Длина оконечного участка канала передачи данных: {L_last:.2f} км")

print(f"Количество промежуточных усилителей (N): {N}")