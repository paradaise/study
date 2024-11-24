import numpy as np
import random

#Функция generate_random_message(k) генерирует случайное бинарное сообщение длиной k.
def generate_random_message(k):
    return np.random.randint(0, 2, k)

#Функция polynomial_to_bits(p) преобразует полином в массив битов.
def polynomial_to_bits(p):
    return np.array([int(bit) for bit in bin(p)[2:]])

#Функция divide_polynomials(dividend, divisor) выполняет деление полиномов, возвращая остаток.
def divide_polynomials(dividend, divisor):
    while len(dividend) >= len(divisor):
        if dividend[0] == 1:
            dividend[:len(divisor)] ^= divisor
        dividend = dividend[1:]
    return dividend

#Функция encode_message(message, generator_polynomial) кодирует сообщение, добавляя проверочные биты.
def encode_message(message, generator_polynomial):
    padded_message = np.concatenate((message, np.zeros(len(generator_polynomial) - 1, dtype=int)))
    remainder = divide_polynomials(padded_message, generator_polynomial)
    return np.concatenate((message, remainder))

def introduce_error(encoded_message):
    error_position = random.randint(0, len(encoded_message) - 1)
    encoded_message[error_position] ^= 1
    return error_position, encoded_message

def detect_error(encoded_message, generator_polynomial):
    syndrome = divide_polynomials(encoded_message.copy(), generator_polynomial)
    if not any(syndrome):
        return -1, syndrome
    for i in range(len(encoded_message)):
        test_message = encoded_message.copy()
        test_message[i] ^= 1
        if not any(divide_polynomials(test_message.copy(), generator_polynomial)):
            return i, syndrome
    return -1, syndrome

def main():
    k = 12
    generator_polynomial_bits = polynomial_to_bits(0b1101)  # Пример полинома x^3 + x^2 + 1

    print("Образующий полином:", generator_polynomial_bits)

    for experiment in range(6):
        print(f"\nЭксперимент {experiment + 1}")
        message = generate_random_message(k)
        print("Исходное сообщение:", message)

        encoded_message = encode_message(message, generator_polynomial_bits)
        print("Закодированное сообщение:", encoded_message)

        error_position, erroneous_message = introduce_error(encoded_message.copy())
        print("Сообщение с ошибкой:", erroneous_message)
        print(f"Ошибка введена в позиции {error_position}")

        detected_error_position, syndrome = detect_error(erroneous_message.copy(), generator_polynomial_bits)
        print("Обнаруженная позиция ошибки:", detected_error_position)
        print("Синдром:", syndrome)

        if detected_error_position != -1:
            erroneous_message[detected_error_position] ^= 1
        print("Исправленное сообщение:", erroneous_message)
        print("Сообщение без проверочных разрядов:", erroneous_message[:-len(generator_polynomial_bits) + 1])
        print("Исходное сообщение совпадает с исправленным:",
              np.array_equal(message, erroneous_message[:-len(generator_polynomial_bits) + 1]))

if __name__ == "__main__":
    main()
