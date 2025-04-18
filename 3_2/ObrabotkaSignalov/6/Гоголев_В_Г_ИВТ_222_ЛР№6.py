# импортируем библиотеки
import numpy as np
import matplotlib.pyplot as plt

x = np.array([2, 1, 1, 0, 2, 1, 1, 0])

# рассчитываем ряд Фурье
a0 = np.mean(x)
a = np.zeros(4)
b = np.zeros(4)

#рассчёт коэффициентов
for k in range(1, 5):
    a[k-1] = (2.0 / len(x)) * np.sum([x[n] * np.cos(2 * np.pi * k * n / len(x)) for n in range(len(x))])
    b[k-1] = (2.0 / len(x)) * np.sum([x[n] * np.sin(2 * np.pi * k * n / len(x)) for n in range(len(x))])

t = np.arange(0, len(x))
x_reconstructed = np.zeros(len(x))
x_reconstructed += a0

#вычисление приближенного исходного сигнала
for k in range(1, 5):
    x_reconstructed += a[k-1] * np.cos(2 * np.pi * k * t / len(x)) + b[k-1] * np.sin(2 * np.pi * k * t / len(x))


# Коэффициенты ДПФ (DFT)
DFT_coef = np.fft.fft(x)
#DFT_coef = np.array([8., 0.47140452, 0., 0.47140452, 0., 0.47140452, 0., 0.47140452])

# Обратное преобразование Фурье (IDFT)
x_restored = np.real(np.fft.ifft(DFT_coef))

plt.bar(t, x, width=0.4)
plt.stem(x)
plt.plot(x_reconstructed, 'r')
plt.title('Дискретный сигнал')
plt.xlabel('Время, с')
plt.ylabel('Амплитуда')
plt.show()
