import numpy as np
import matplotlib.pyplot as plt
import sys

sys.stdout.reconfigure(encoding="utf-8")


# Параметры первого сигнала (прямоугольный импульс)
max1 = 4
duration1 = 20

# Параметры второго сигнала (треугольный импульс)
max2 = 4
duration2 = 20

# Временная шкала
time = np.linspace(-duration2, duration2, num=1000)


# Функция для прямоугольного импульса
def rect_pulse(x, amplitude, duration):
    if 0 <= x <= duration:
        return amplitude
    else:
        return 0


# Функция для треугольного импульса
def triangle_pulse(x, amplitude, duration):
    if 0 <= x <= duration:
        return amplitude * (1 - x / duration)
    else:
        return 0


# Расчет значений для временной шкалы
signal1 = [rect_pulse(x, max1, duration1) for x in time]
signal2 = [triangle_pulse(x, max2, duration2) for x in time]

# Преобразование в массивы NumPy
s1 = np.array(signal1)
s2 = np.array(signal2)


# Построение графиков для отдельного отображения
plt.figure()
plt.plot(time, s1, label="Прямоугольный импульс")
plt.title("График прямоугольного импульса")
plt.xlabel("Время")
plt.ylabel("Амплитуда")
plt.legend()
plt.grid(True)
plt.show()

plt.figure()
plt.plot(time, s2, label="Треугольный импульс")
plt.title("График треугольного импульса")
plt.xlabel("Время")
plt.ylabel("Амплитуда")
plt.legend()
plt.grid(True)
plt.show()

# Построение графика с наложением двух функций
plt.figure()
plt.plot(time, s1, label="Прямоугольный импульс")
plt.plot(time, s2, label="Треугольный импульс")
plt.title("Наложение функций прямоугольного и треугольного импульсов")
plt.xlabel("Время")
plt.ylabel("Амплитуда")
plt.legend()
plt.grid(True)
plt.show()

# Расчет корреляции
corr_full = np.correlate(s1, s2, mode="full")
corr_same = np.correlate(s1, s2, mode="same")

# Поиск максимального значения корреляции
max_corr = np.max(corr_full)

# Определение интервала корреляции
corr_interval = None
for i, value in enumerate(corr_full):
    if value == max_corr:
        corr_interval = time[i % len(time)]  # Расчет соответствующего времени
        break

# График полной корреляции
plt.figure()
plt.plot(corr_full)
plt.title("График полной корреляции")
plt.grid(True)
plt.show()

# График взаимной корреляции
plt.figure()
plt.plot(corr_same)
plt.title("График взаимной корреляции")
plt.grid(True)
plt.show()

# Вывод результатов
print("Максимальное значение корреляционной функции:", max_corr)
print("Интервал корреляции:", corr_interval)
