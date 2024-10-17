import random
import numpy as np

def generate_information_combination(k):
    return [random.randint(0, 1) for _ in range(k)]

def calculate_parity_bits_count(k):
    r = 0
    while (2 ** r) < (k + r + 1):
        r += 1
    return r

def generate_polynomial(k):
    return [random.randint(0, 1) for _ in range(k)]

def create_cyclic_code(data, generator):
    data = data + [0] * (len(generator) - 1)
    for i in range(len(data) - len(generator) + 1):
        if data[i] == 1:
            for j in range(len(generator)):
                data[i + j] ^= generator[j]
    return data

def introduce_error(code, num_errors=1):
    corrupted_code = code[:]
    error_indices = random.sample(range(len(code)), num_errors)
    for idx in error_indices:
        corrupted_code[idx] ^= 1  # Инвертируем бит
    return corrupted_code, error_indices

def calculate_syndrome(received_code, generator):
    remainder = received_code[:]
    for i in range(len(received_code) - len(generator) + 1):
        if remainder[i] == 1:
            for j in range(len(generator)):
                remainder[i + j] ^= generator[j]
    return remainder[-len(generator)+1:]

def correct_error(corrupted_code, syndrome, generator):
    position = 0
    for i in range(len(generator) - 1):
        if np.array_equal(syndrome, np.roll(generator, i)[1:]):
            position = i
            break
    corrected_code = corrupted_code[:]
    if position:
        corrected_code[position - 1] ^= 1
    return corrected_code

def main():
    k = 8
    message = generate_information_combination(k)
    print("Информационная комбинация:", message)
    
    generator = generate_polynomial(k)
    print("Образующий полином:", generator)

    cyclic_code = create_cyclic_code(message, generator)
    print("Циклический код без ошибки:", cyclic_code)

    code_with_error, error_indices = introduce_error(cyclic_code, num_errors=random.randint(0, 2))
    print("Код с ошибкой:", code_with_error)
    print("Позиция ошибок:", error_indices)

    syndrome = calculate_syndrome(code_with_error, generator)
    print("Синдром ошибки:", syndrome)

    if syndrome:
        corrected_code = correct_error(code_with_error, syndrome, generator)
        print("Исправленный код:", corrected_code)
    else:
        print("Ошибок нет")

if __name__ == "__main__":
    main()
