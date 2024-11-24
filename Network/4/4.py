import math

# Константы
A_ns = 0.05  # Потери на неразъемных соединениях, дБ
A_ps = 0.2  # Потери на разъемных соединениях, дБ
A_eza = 3  # Эксплуатационный запас для аппаратуры, дБ
A_ezk = 3  # Эксплуатационный запас для кабеля, дБ
DPMD = 0.5  # Коэффициент поляризационной модовой дисперсии, пс/км^1/2
S0 = 0.092  # Максимальная величина крутизны нулевой дисперсии, пс/(нм^2*км)
lambda_0_min = 1301.5e-9  # Минимальная длина волны с нулевой дисперсией, м


def calculate_pmd(L):
    """Расчет поляризационной модовой дисперсии"""
    return DPMD * math.sqrt(L)


def calculate_chromatic_dispersion(L, lambda_, delta_lambda):
    """Расчет хроматической дисперсии"""
    D = S0 * ((lambda_ - lambda_0_min) / lambda_0_min**4)
    return D * delta_lambda * L


def calculate_total_dispersion(tau_pmd, tau_chr):
    """Расчет результирующего уширения импульса"""
    return math.sqrt(tau_pmd**2 + tau_chr**2)


def calculate_impulse_duration(tau_0, tau_res):
    """Расчет конечной длительности импульсов"""
    return math.sqrt(tau_0**2 + tau_res**2)


def calculate_max_impulse_duration(T0):
    """Максимально возможное уширение импульса"""
    return T0 / math.sqrt(2)


def calculate_energy_budget(P_vyh, P_fpr, L, alpha, n_ns, n_ps):
    """Расчет энергетического бюджета"""
    A = A_ns * n_ns + alpha * L + A_ps * n_ps
    return P_vyh - P_fpr - A_eza - A_ezk - A


def main():
    # Пример данных
    L = 56  # Протяженность ВОЛС, км
    n = 1.467  # Показатель преломления сердцевины
    lambda_ = 1.78e-6  # Рабочая длина волны, м
    n_ns = 21  # Количество муфт (сростков)
    alpha = 0.26  # Километрическое затухание, дБ/км
    n_ps = 4  # Количество разъемных соединений
    P_vyh = 15  # Мощность источника оптического излучения, дБм
    P_fpr = -23  # Чувствительность приемника, дБм
    delta_lambda = 0.02e-9  # Максимальная ширина спектра излучения источника, м
    B0_4 = 623e6  # Скорость передачи при STM-4, бит/с
    tau_0_4 = 414e-12  # Начальная длительность импульса для STM-4, с
    B0_16 = 9930e6  # Скорость передачи при STM-64, бит/с
    tau_0_16 = 23e-12  # Начальная длительность импульса для STM-16, с

    # Расчет дисперсий и уширения импульса
    tau_pmd = calculate_pmd(L)
    tau_chr = calculate_chromatic_dispersion(L, lambda_, delta_lambda)
    tau_res = calculate_total_dispersion(tau_pmd, tau_chr)
    tau_final_4 = calculate_impulse_duration(tau_0_4, tau_res)
    tau_final_16 = calculate_impulse_duration(tau_0_16, tau_res)
    T0_4 = 1 / B0_4
    T0_16 = 1 / B0_16
    max_tau_4 = calculate_max_impulse_duration(T0_4)
    max_tau_16 = calculate_max_impulse_duration(T0_16)
    energy_budget = calculate_energy_budget(P_vyh, P_fpr, L, alpha, n_ns, n_ps)

    # Вывод результатов
    print(f"Поляризационная модовая дисперсия: {tau_pmd:.4f} пс")
    print(f"Хроматическая дисперсия: {tau_chr:.4f} пс")
    print(f"Результирующее уширение импульса: {tau_res:.4f} пс")
    print(f"Конечная длительность импульсов для STM-4: {tau_final_4:.4f} пс")
    print(f"Конечная длительность импульсов для STM-16: {tau_final_16:.4f} пс")
    print(f"Максимально возможное уширение импульса для STM-4: {max_tau_4:.4f} пс")
    print(f"Максимально возможное уширение импульса для STM-16: {max_tau_16:.4f} пс")
    print(f"Энергетический бюджет: {energy_budget:.2f} дБ")


if __name__ == "__main__":
    main()
