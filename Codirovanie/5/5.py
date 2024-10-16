import random

#генерация входного сообщения
def generate_random_bits(n):
    return [random.randint(0, 1) for _ in range(n)]

def calculate_hamming_code(data_bits):
    # Рассчитываем код Хэмминга на основе входных данных
    n = len(data_bits)
    r = 0
    while (2**r) < (n + r + 1):
        r += 1
    total_bits = n + r
    hamming_code = [0] * total_bits

    # Располагаем информационные биты в коде Хэмминга
    j = 0
    for i in range(1, total_bits + 1):
        if i & (i - 1) != 0:
            hamming_code[i - 1] = data_bits[j]
            j += 1

    # Рассчитываем значения контрольных битов
    for i in range(r):
        control_bit_position = 2**i
        control_sum = 0
        for j in range(1, total_bits + 1):
            if j & control_bit_position != 0:
                control_sum ^= hamming_code[j - 1]
        hamming_code[control_bit_position - 1] = control_sum

    return hamming_code

# вводим ошибки в код Хэмминга
def introduce_errors(hamming_code, num_errors=1): 
    corrupted_code = hamming_code[:]
    error_indices = random.sample(range(len(hamming_code)), num_errors) # позиции ошибок
    for idx in error_indices:
        corrupted_code[idx] ^= 1  # Инвертируем бит
    return corrupted_code, error_indices

#вычисление синдрома ошибки
def calculate_syndrome(corrupted_code, r):
    syndrome = 0
    for i in range(r):
        control_bit_position = 2**i
        control_sum = 0
        for j in range(1, len(corrupted_code) + 1):
            if j & control_bit_position != 0: # проверка входит ли текущая позиция(j) в область проверки бита
                control_sum ^= corrupted_code[j - 1]
        syndrome |= (control_sum << i)
    return syndrome

#исправление ошибки в коде Хеминга
def correct_single_error(corrupted_code, syndrome):
    if syndrome > 0:
        error_position = syndrome - 1
        corrupted_code[error_position] ^= 1  # Исправляем ошибку
    return corrupted_code

# Извлечение исходной информационной комбинации из исправленного кода Хэмминга
def extract_information_bits(hamming_code):
    data = []
    n = len(hamming_code)
    for i in range(1, n + 1):
        if (i & (i - 1)) != 0:  # Пропускаем позиции степеней двойки
            data.append(hamming_code[i - 1])
    return data


def main():
    n = 11  # Количество информационных битов
    r = 4   # Количество контрольных битов

    for attempt in range(6):  # 6 попыток
        print(f"\nЭксперимент {attempt + 1}:")

        # 1. Генерация информационных битов
        data_bits = generate_random_bits(n)
        print("Сгенерированные информационные биты:", data_bits)

        # 2. Код Хэмминга
        hamming_code = calculate_hamming_code(data_bits)
        print("Код Хэмминга:", hamming_code)

        # 3. Введение ошибок (одной или двух)
        num_errors = random.choice([1, 2])
        corrupted_code, error_indices = introduce_errors(hamming_code, num_errors)
        print("Код с ошибками:", corrupted_code)
        print("Индексы ошибок:", error_indices)

        # 4. Вычисление синдрома
        if num_errors == 1:
            syndrome = calculate_syndrome(corrupted_code, r)
            print("Синдром ошибки:", syndrome)

        # 5. Исправление ошибки, если она однократная
        if  num_errors == 1:
            corrected_haming_code = correct_single_error(corrupted_code[:], syndrome)
            corrected_input_code = extract_information_bits(corrected_haming_code)
            print("Исправленный код Хемминга:", corrected_haming_code)
            print("Обнаружена однократная ошибка")
            print("Входное сообщение без проверочных битов:", corrected_input_code)
        elif num_errors == 2:
            print("Обнаружена двукратная ошибка")

main()