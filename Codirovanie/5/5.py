import random

k = 8

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
        if (i & (i - 1)) == 0:  # Позиции степеней двойки
            continue
        hamming_code[i-1] = data[j]
        j += 1
    return hamming_code

# Рассчёт проверочных битов
def calculate_parity_bits(hamming_code, r):
    n = len(hamming_code)
    for i in range(r):
        parity_bit_position = 2**i
        parity = 0 #проверочная сумма
        for j in range(1, n + 1):
            if j & parity_bit_position and j != parity_bit_position:
                parity ^= hamming_code[j - 1]
        hamming_code[parity_bit_position - 1] = parity
    return hamming_code

# Введение ошибки в код
def introduce_error(code):
    error_position = random.randint(0, len(code) - 1)
    code_with_error = code.copy()
    code_with_error[error_position] ^= 1
    return code_with_error, error_position

# Проверка и определение синдрома ошибки
def calculate_syndrome(received_code, r):
    n = len(received_code)
    syndrome = 0
    for i in range(r):
        parity_bit_position = 2**i
        parity = 0 #проверочная сумма
        for j in range(1, n+1):
            if j & parity_bit_position:
                parity ^= received_code[j - 1]
        if parity:
            syndrome += parity_bit_position
    return syndrome

# Исправление ошибки
def correct_error(code, syndrome):
    if syndrome:
        code[syndrome - 1] ^= 1
    return code

# Основная функция программы
def main():
    message = generate_information_combination(k)
    print("Информационная комбинация:", message)
    
    r = calculate_parity_bits_count(k)
    print("Количество проверочных бит:", r)
    
    hamming_code = insert_parity_bits(message, r)
    hamming_code = calculate_parity_bits(hamming_code, r)
    print("Код Хэмминга без ошибки:", hamming_code)

    # Внесение ошибки
    code_with_error, error_position = introduce_error(hamming_code)
    print("Код с ошибкой:", code_with_error)
    print("Позиция ошибки:", error_position)

    # Вычисление синдрома и исправление ошибки
    syndrome = calculate_syndrome(code_with_error, r)
    print("Синдром ошибки:", syndrome)
    
    if syndrome:
        corrected_code = correct_error(code_with_error, syndrome)
        print("Исправленный код:", corrected_code)
    else:
        print("Ошибок нет")

if __name__ == "__main__":
    main()