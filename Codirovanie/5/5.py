import random
import numpy as np
k = 11

# Генерация случайной информационной комбинации
def generate_information_combination(k):
    return [random.randint(0, 1) for _ in range(k)]

# Рассчёт количества проверочных битов
def calculate_parity_bits_count(k):
    r = 0
    while (2**r) < (k + r + 1):
        r += 1
    return r

# Вставка проверочных битов
def insert_parity_bits(data, r):
    n = len(data) + r
    hamming_code = [0] * n
    j = 0
    for i in range(1, n+1):
        if (i & (i - 1)) == 0:  # Пропускаем позиции степени двойки
            continue
        hamming_code[i-1] = data[j]
        j += 1
    return hamming_code

# Рассчёт проверочных битов
def calculate_parity_bits(hamming_code, r):
    n = len(hamming_code)
    for i in range(r):
        parity_bit_position = 2**i # позиция проверочного бита
        parity = 0 #проверочная сумма 
        for j in range(1, n + 1):
            if j & parity_bit_position and j != parity_bit_position:
                parity ^= hamming_code[j - 1]
        hamming_code[parity_bit_position - 1] = parity
    return hamming_code

# Введение ошибок в код
def introduce_errors(code, num_errors):
    positions = random.sample(range(len(code)), num_errors)
    code_with_errors = code.copy()
    for pos in positions:
        code_with_errors[pos] ^= 1
    return code_with_errors, positions

# Проверка и определение синдрома ошибки
def calculate_syndrome(received_code, r):
    n = len(received_code)
    syndrome = 0
    for i in range(r):
        parity_bit_position = 2**i # позиция проверочного бита
        parity = 0 #проверочная сумма
        for j in range(1, n+1):
            if j & parity_bit_position:
                parity ^= received_code[j - 1]
        if parity:
            syndrome += parity_bit_position
    return syndrome

# Исправление ошибки
def correct_errors(code, syndrome):
    if syndrome:
        code[syndrome - 1] ^= 1
    return code

# Извлечение исходной информационной комбинации из исправленного кода Хэмминга
def extract_information_bits(hamming_code, r):
    data = []
    n = len(hamming_code)
    for i in range(1, n + 1):
        if (i & (i - 1)) != 0:  # Пропускаем позиции степеней двойки
            data.append(hamming_code[i - 1])
    return data

def main():
    message = generate_information_combination(k)
    print("Информационная комбинация:", message)
    
    r = calculate_parity_bits_count(k)
    print("Количество проверочных бит:", r)
    
    hamming_code = insert_parity_bits(message, r)
    hamming_code = calculate_parity_bits(hamming_code, r)
    print("Код Хэмминга без ошибки:", hamming_code)

    # Внесение ошибок
    num_errors = random.randint(0, 2)
    code_with_errors, error_positions = introduce_errors(hamming_code, num_errors)
    print("Код с ошибками:", code_with_errors)
    print("Позиции ошибок:", error_positions)

    # Вычисление синдрома и исправление ошибок
    syndrome = calculate_syndrome(code_with_errors, r)
    print("Синдром ошибки:", syndrome)
    
    if syndrome:
        corrected_code = correct_errors(code_with_errors, syndrome)
        print("Исправленный код:", corrected_code)
    else:
        corrected_code = code_with_errors
        print("Ошибок нет")

    # Извлечение исходной информационной комбинации
    extracted_message = extract_information_bits(corrected_code, r)
    print("Извлеченная информационная комбинация:", extracted_message)

    if np.array_equal(hamming_code, corrected_code):
        print('Код Хэмминга без ошибок и исправленный код совпадают')

    if np.array_equal(extracted_message, message):
        print('Входная комбинация и выходные информационные биты совпадают')

if __name__ == "__main__":
    main()
