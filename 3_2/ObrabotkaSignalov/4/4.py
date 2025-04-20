# Импортируем необходимые библиотеки
import numpy as np
import matplotlib.pyplot as plt


# Функция для прямоугольного импульса
def rect_pulse(t, amplitude, duration):
    return np.where((t >= 0) & (t <= duration), amplitude, 0)


# Заданные параметры
E_max = 34  # В
t_duration = 700e-6  # 700 мкс
omega = 2 * np.pi / t_duration
f_v = omega / (2 * np.pi)

# Временная шкала и генерация сигнала
t = np.linspace(0, t_duration * 2, 1000)  # Временные отсчёты
signal = rect_pulse(t, E_max, t_duration)

# Расчет эффективной ширины спектра
spectrum = np.abs(np.fft.fft(signal)) ** 2
frequencies = np.fft.fftfreq(len(t), d=(t[1] - t[0]))
total_energy = np.sum(spectrum)
effective_energy = total_energy * 0.99  # 99% энергии
cumulative_energy = np.cumsum(spectrum)
effective_width_index = np.where(cumulative_energy >= effective_energy)[0][0]
effective_width = np.abs(frequencies[effective_width_index])

# Дискретизация сигнала
sampling_interval = 1 / (2 * f_v)
sample_indices = np.arange(0, len(t), int(sampling_interval / (t[1] - t[0])))
sampling_points = t[sample_indices]
sampled_signal = rect_pulse(sampling_points, E_max, t_duration)

# Восстановление сигнала через ряд Котельникова
reconstructed_signal = np.zeros_like(t)
for k, sample in enumerate(sampled_signal):
    reconstructed_signal += sample * np.sinc(
        (t - k * sampling_interval) / sampling_interval
    )

# Графики
plt.figure(figsize=(12, 8))

# Оригинальный сигнал
plt.subplot(3, 1, 1)
plt.plot(t, signal, label="Оригинальный сигнал")
plt.title("Оригинальный сигнал")
plt.legend()

# Дискретизированный сигнал с линией
plt.subplot(3, 1, 2)
plt.plot(
    sampling_points,
    sampled_signal,
    linestyle="--",
    marker="o",
    label="Дискретизированный сигнал",
)
plt.title("Дискретизированный сигнал")
plt.legend()

# Восстановленный сигнал
plt.subplot(3, 1, 3)
plt.plot(t, reconstructed_signal, label="Восстановленный сигнал", linestyle="--")
plt.title("Восстановленный сигнал")
plt.legend()

plt.tight_layout()
plt.show()

# Вывод результатов
print(f"Эффективная ширина спектра: {effective_width:.3f} Гц")
print(f"Количество отсчётных значений: {len(sampled_signal)}")
print("Сигнал успешно дискретизирован и восстановлен.")
