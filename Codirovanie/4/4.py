import numpy as np

def generate_matrices(k, n):
    # Генерация случайной производящей матрицы Pn,k
    P = np.random.randint(0, 2, (k, n))
    
    # Построение проверочной матрицы H
    H = np.random.randint(0, 2, (n - k, n))
    
    # Убедимся, что H * P^T = 0
    while np.any(np.dot(H, P.T) % 2 != 0):
        H = np.random.randint(0, 2, (n - k, n))
    
    return P, H

k = 5  # Количество информационных бит
n = 6  # Общее количество бит в кодовом слове (пример)

P, H = generate_matrices(k, n)

print("Производящая матрица P:\n", P)
print("Проверочная матрица H:\n", H)

def generate_information_vector(k):
    return np.random.randint(0, 2, k)

def encode_information_vector(P, info_vector):
    return np.dot(info_vector, P) % 2

def introduce_error(codeword):
    error_position = np.random.randint(0, len(codeword))
    codeword[error_position] ^= 1  # Инвертируем бит
    return codeword, error_position

def calculate_syndrome(H, received_vector):
    return np.dot(H, received_vector.T) % 2

def correct_error(received_vector, syndrome, H):
    for i in range(H.shape[1]):
        if np.array_equal(H[:, i], syndrome):
            received_vector[i] ^= 1  # Инвертируем бит
            break
    return received_vector

# Генерация информационной кодовой комбинации
info_vector = generate_information_vector(k)
print("Информационная кодовая комбинация:\n", info_vector)

# Кодирование информационной комбинации
codeword = encode_information_vector(P, info_vector)
print("Систематический код:\n", codeword)

# Введение ошибки
received_vector, error_position = introduce_error(codeword.copy())
print("Принятый код с ошибкой (позиция ошибки {}):\n".format(error_position), received_vector)

# Вычисление синдрома ошибки
syndrome = calculate_syndrome(H, received_vector)
print("Синдром ошибки:\n", syndrome)

# Коррекция ошибки
corrected_vector = correct_error(received_vector, syndrome, H)
print("Откорректированный код:\n", corrected_vector)