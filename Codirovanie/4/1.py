import random
import numpy as np

# Генерация случайной информационной комбинации
def generate_information_combination(k):
    return [random.randint(0, 1) for _ in range(k)]

# Генерация производящей матрицы P(n,k)
def build_generator_matrix(k, p):
    Uk = np.identity(k, dtype=int)
    H = np.random.randint(0, 2, size=(p, k))
    G = np.concatenate((Uk, H.T), axis=1)
    return G

# Вычисление n
def calculate_n(k):
    n = k
    while (2**n < n + k + 1):
        n += 1
    return n

# Кодирование информации
def encode_information(information_bits, G):
    return np.dot(information_bits, G) % 2

# Введение ошибки в код
def introduce_error(code):
    error_position = random.randint(0, len(code) - 1)
    code_with_error = code.copy()
    code_with_error[error_position] ^= 1
    return code_with_error, error_position

# Создание проверочной матрицы
def build_parity_check_matrix(G):
    k = G.shape[0]
    p = G.shape[1] - k
    H = np.concatenate((G[:, k:].T, np.identity(p, dtype=int)), axis=1)
    return H

# Обнаружение и исправление ошибки
def detect_and_correct_error(received_code, H):
    syndrome = np.dot(H, received_code.T) % 2
    print("Синдром ошибки:", syndrome)  # Вывод синдрома для отладки
    if np.any(syndrome):
        error_position = int(''.join(map(str, syndrome)), 2)
        if 0 <= error_position < len(received_code):
            print(f"Ошибка обнаружена в позиции: {error_position}")
            received_code[error_position] ^= 1
        else:
            print("Ошибка: некорректная позиция ошибки")
    else:
        print("Ошибки нет.")
    return received_code

# Основной код
k = 61
information_bits = generate_information_combination(k)
print("Информационная комбинация:", information_bits)

n = calculate_n(k)
p = n - k

generator_matrix = build_generator_matrix(k, p)
print("Производящая матрица P(n,k):\n", generator_matrix)

systematic_code = encode_information(information_bits, generator_matrix)
print("Систематический код:", systematic_code)

# Имитация передачи систематического кода и проверочной матрицы на приёмник
code_with_error, error_position = introduce_error(systematic_code)
print("Код с ошибкой:", code_with_error)
print("Позиция ошибки:", error_position)

parity_check_matrix = build_parity_check_matrix(generator_matrix)
print("Проверочная матрица H:\n", parity_check_matrix)

if parity_check_matrix.size == 0:
    print("Ошибка: проверочная матрица пустая")
else:
    corrected_code = detect_and_correct_error(code_with_error, parity_check_matrix)
    print("Исправленный код:", corrected_code)

    if np.array_equal(systematic_code, corrected_code):
        print("Ошибка успешно исправлена!")
    else:
        print("Ошибка не исправлена.")
