import numpy as np
import matplotlib.pyplot as plt

# Константы
epsilon_0 = 8.85e-12  # Ф/м
mu_0 = 4 * np.pi * 1e-7  # Гн/м


def calculate_wave_length(f, epsilon_r, mu_r):
    v = 1 / np.sqrt(epsilon_0 * epsilon_r * mu_0 * mu_r)
    return v / f


def calculate_field_components(Im, l, f, epsilon_r, mu_r, r, theta):
    omega = 2 * np.pi * f
    epsilon_a = epsilon_0 * epsilon_r
    k = 2 * np.pi / calculate_wave_length(f, epsilon_r, mu_r)

    E_r = (
        (Im * l * k**3 / (2 * np.pi * omega * epsilon_a))
        * (1 / r**2 - 1j / (k * r**3))
        * np.cos(theta)
        * np.exp(-1j * k * r)
    )
    E_theta = (
        (Im * l * k**3 / (4 * np.pi * omega * epsilon_a))
        * (1 / r - 1j / (k * r**2) - 1 / (k**2 * r**3))
        * np.sin(theta)
        * np.exp(-1j * k * r)
    )
    H_phi = (
        (1j * Im * l * k**2 / (4 * np.pi * r))
        * (1 / r - 1j / (k * r**2))
        * np.sin(theta)
        * np.exp(-1j * k * r)
    )

    return E_r, E_theta, H_phi


def plot_radiation_pattern(theta, E_theta, zone):
    plt.figure()
    ax = plt.subplot(111, projection="polar")
    ax.plot(theta, np.abs(E_theta))
    ax.set_title(f"Radiation Pattern in {zone} Zone")
    plt.show()


def main():
    # Пример для таблицы 3: l=1, Im=0.01, epsilon_r=1, mu_r=1, f=1000e6
    l = 0.7
    Im = 0.04
    epsilon_r = 2
    mu_r = 4
    f = 850e6

    lambda_ = calculate_wave_length(f, epsilon_r, mu_r)
    print(f"Длина волны: {lambda_:.2f} м")

    r = lambda_  # расстояние наблюдения
    theta = np.linspace(0, 2 * np.pi, 360)

    E_r, E_theta, H_phi = calculate_field_components(
        Im, l, f, epsilon_r, mu_r, r, theta
    )

    plot_radiation_pattern(theta, E_theta, "Far")

    # Границы зон излучения
    k = 2 * np.pi / lambda_
    print(f"Ближняя зона: k*r < 1 -> r < {1/k:.2f} м")
    print(f"Промежуточная зона: 1 < k*r < 10 -> {1/k:.2f} м < r < {10/k:.2f} м")
    print(f"Дальняя зона: k*r > 10 -> r > {10/k:.2f} м")


if __name__ == "__main__":
    main()
