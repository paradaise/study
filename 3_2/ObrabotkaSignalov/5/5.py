import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.optimize import root_scalar


def calculate_energy(E_max, tau):
    """Вычисление энергии сигнала."""
    return E_max**2 * tau


def find_effective_bandwidth(target):
    """Поиск эффективной ширины спектра."""

    def integral_sinc_squared(x):
        result, _ = quad(
            lambda t: (np.sin(t) / t) ** 2 if t != 0 else 1.0, 0, x, limit=1000
        )
        return result

    def equation(x):
        return integral_sinc_squared(x) - target

    sol = root_scalar(equation, bracket=[0, 1000], method="brentq")
    return sol.root


def calculate_samples(tau, delta_tau):
    """Вычисление моментов отсчётов."""
    return np.arange(0, tau + delta_tau, delta_tau)


def restored_signal(t, valid_t_k, s_k_values, omega_eff):
    """Восстановление сигнала по отсчётам."""
    return sum(
        s_k * np.sinc(omega_eff / np.pi * (t - t_k))
        for t_k, s_k in zip(valid_t_k, s_k_values)
    )


def plot_results(
    t_continuous,
    original,
    restored,
    valid_t_k,
    s_k_values,
    tau,
    delta_tau,
    omega_eff,
    E,
):
    """Построение графиков с дополнительной информацией."""
    plt.figure(figsize=(14, 12))

    # Конвертация времени в микросекунды
    t_micro = t_continuous * 1e6
    tau_micro = tau * 1e6
    valid_t_k_micro = valid_t_k * 1e6
    delta_tau_micro = delta_tau * 1e6
    omega_eff_hz = omega_eff / (2 * np.pi)  # Перевод в Гц
    nyquist_freq = 1 / (2 * delta_tau)  # Частота Найквиста в Гц

    # Создаем форматированные строки с параметрами
    params_base = (
        f"Параметры сигнала:\n"
        f"Амплитуда: {E_max} В\n"
        f"Длительность: {tau_micro:.0f} мкс\n"
        f"Энергия: {E:.2f} В²·с"
    )

    params_sampling = (
        f"Параметры дискретизации:\n"
        f"Шаг выборки: {delta_tau_micro:.2f} мкс\n"
        f"Частота Найквиста: {nyquist_freq:.2f} Гц\n"
        f"Количество отсчётов: {len(valid_t_k)}"
    )

    params_spectrum = (
        f"Спектральные характеристики:\n"
        f"Эффективная ширина: {omega_eff_hz:.2f} Гц\n"
        f"Частота дискретизации: {1/delta_tau:.2f} Гц"
    )

    # График 1: Исходный и восстановленный сигнал
    plt.subplot(3, 1, 1)
    plt.plot(t_micro, original, label="Исходный сигнал", color="blue")
    plt.plot(t_micro, restored, label="Восстановленный", color="red", linestyle="--")
    plt.text(
        0.65,
        0.15,
        params_base,
        transform=plt.gca().transAxes,
        bbox=dict(facecolor="white", alpha=0.8),
    )
    plt.title("Исходный и восстановленный сигналы")
    plt.xlabel("Время (мкс)")
    plt.ylabel("Амплитуда (В)")
    plt.grid(True)
    plt.xlim(-50, tau_micro + 50)
    plt.legend(loc="upper right")

    # График 2: Отсчётные значения
    plt.subplot(3, 1, 2)
    markerline, stemlines, _ = plt.stem(
        valid_t_k_micro, s_k_values, linefmt="C1-", markerfmt="C1o"
    )
    plt.setp(stemlines, "linewidth", 1)
    plt.setp(markerline, "markersize", 4)
    plt.text(
        0.65,
        0.15,
        params_sampling,
        transform=plt.gca().transAxes,
        bbox=dict(facecolor="white", alpha=0.8),
    )
    plt.title("Дискретные отсчёты сигнала")
    plt.xlabel("Время (мкс)")
    plt.ylabel("Амплитуда (В)")
    plt.grid(True)
    plt.xlim(-50, tau_micro + 50)

    # График 3: Спектральная плотность мощности
    plt.subplot(3, 1, 3)
    omega = np.linspace(0, 2 * np.pi * 2e6, 1000)
    spectrum = (np.sinc(omega * tau / (2 * np.pi))) ** 2 * (E_max * tau) ** 2
    plt.plot(omega / (2 * np.pi), spectrum)  # Ось X теперь в Гц

    plt.axvline(omega_eff_hz, color="red", linestyle="--")
    plt.text(
        0.65,
        0.15,
        params_spectrum,
        transform=plt.gca().transAxes,
        bbox=dict(facecolor="white", alpha=0.8),
    )
    plt.title("Спектральная плотность мощности")
    plt.xlabel("Частота (Гц)")
    plt.ylabel("Мощность (В²·с²/Гц²)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# Основные параметры
E_max = 34  # Амплитуда (В)
tau = 700e-6  # Длительность импульса (с)
target = 0.99 * np.pi / 2

# Расчёты
E = calculate_energy(E_max, tau)
x_eff = find_effective_bandwidth(target)
omega_eff = 2 * x_eff / tau
delta_tau = np.pi / omega_eff

# Генерация отсчётов
valid_t_k = calculate_samples(tau, delta_tau)
s_k_values = E_max * np.ones_like(valid_t_k)

# Временная ось для графиков
t_continuous = np.linspace(-100e-6, tau + 100e-6, 10000)
original = np.where((t_continuous >= 0) & (t_continuous <= tau), E_max, 0)
restored = np.array(
    [restored_signal(t, valid_t_k, s_k_values, omega_eff) for t in t_continuous]
)

# Построение графиков
plot_results(
    t_continuous,
    original,
    restored,
    valid_t_k,
    s_k_values,
    tau,
    delta_tau,
    omega_eff,
    E,
)
