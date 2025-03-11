import numpy as np
import matplotlib.pyplot as plt


# параметры сигнала x
Emax1 = 1
ti1 = 4

# параметры сигнала y
Emax2 = 1
ti2 = 4

# Задаем значения времени
t = np.linspace(-ti2, ti2, num=1000)


def graf1(x):
    if 0 <= x <= ti1:
        return -Emax1
    else:
        return 0

def graf2(x):
    if (-ti2 / 2) <= x <= (ti2 / 2):
        y = -((x ** 2) / 4) + 1
        return y
    else:
        return 0


# Рассчитываем значения сигналов для всех значений времени
f1 = [graf1(x) for x in t]
f2 = [graf2(x) for x in t]
# задаем длину корреляционного окна
n = len(f1)
# Преобразуем сигналы в последовательности чисел
s1 = np.array(f1)
s2 = np.array(f2)


# Рассчитываем автокорреляцию как свертку последовательностей чисел
corr = np.correlate(s1, s2, mode='full')
# рассчитываем взаимную корреляцию
corr2 = np.correlate(s1, s2, mode='same')


# Находим максимальное значение взаимной корреляционной функции
Buv_max = np.max(corr)
# Определяем интервал корреляции
for i, B in enumerate(corr):
    if B < Buv_max:
        interval = t[i]
        break


# Создаем график и добавляем на него две функции
fig, ax = plt.subplots()
ax.plot(t, s1, label='f1')
ax.plot(t, s2, label='f2')
# Устанавливаем название графика и метки на осях
ax.set_title('Графики функций f1 и f2')
ax.set_xlabel('Время')
ax.set_ylabel('Амплитуда')
# Добавляем легенду на график
ax.legend()
plt.show()


plt.plot(corr)
plt.title('График автокорреляции')
plt.show()


plt.plot(corr2)
plt.title('График взаимной корреляции')
plt.show()


# Выводим результаты
print('Максимальное значение взаимной корреляционной функции: ', Buv_max)
print('Интервал корреляции: ', interval)