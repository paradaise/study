import numpy as np
import random

def create_verification_matrix(P, K, d_min):
    verification_matrix = np.zeros((K + P, P), dtype=int)
    decrescent = P + K
    for i in range(K):
        matrix_line = decrescent
        one_counter = 0
        for j in range(P - 1, -1, -1):
            verification_matrix[i, j] = matrix_line % 2
            one_counter += matrix_line % 2
            matrix_line //= 2
        if one_counter + 1 < d_min:
            i -= 1
        decrescent -= 1
    for i in range(K, K + P):
        for j in range(P - 1, -1, -1):
            verification_matrix[i, j] = 1 if i - K == j else 0
    return verification_matrix

def create_systemic_code(P, d_min, info_array):
    K = len(info_array)
    systemic_code = np.zeros(P + K, dtype=int)
    systemic_code[:K] = info_array 
    verification_matrix = create_verification_matrix(P, K, d_min)
    for i in range(P):
        systemic_code[K + i] = np.sum(info_array * verification_matrix[:K, i]) % 2 #выбираем какое значение будет у проверочного бита 0 или 1
    return systemic_code, verification_matrix

def search_error(P, d_min, systemic_code):
    verification_matrix = create_verification_matrix(P, len(systemic_code) - P, d_min)
    syndrom = np.array([(np.sum(systemic_code * verification_matrix[:, i]) % 2) for i in range(P)]) #определяем синдром ошибки
    for i in range(len(systemic_code)):
        if np.array_equal(syndrom, verification_matrix[i]):
            return i + 1, i+2
    return -1, i

def main():
    num_experiments = 6
    
    for experiment in range(1, num_experiments + 1):
        # Генерация случайного входного сообщения
        K = 13 #длинна сообщения
        input_str = ''.join(random.choice('01') for _ in range(K))
        info_array = np.array([int(bit) for bit in input_str])
        
        print(f"Эксперимент {experiment}")
        print("Входное сообщение:", input_str)
        
        # Создание систематического кода

        N = K#K-информационные разряды
        d_min = 2 * 1 + 1 #d_min-минимальное растояние ошибок
        while 2**K > (2**N / (N + 1)): #из методички считаем N
            N += 1
        P = N - K #P-кол-во проверочных разрядов
        
        systemic_code, verification_matrix = create_systemic_code(P, d_min, info_array)
        print("Систематический код:", ''.join(map(str, systemic_code)))
        print("Проверочная матрица (Pn,k):\n", verification_matrix)
        
        # Внесение ошибки в случайный бит систематического кода
        error_index = random.randint(0, N - 1)
        systemic_code_with_error = systemic_code.copy()
        systemic_code_with_error[error_index] = 1 - systemic_code_with_error[error_index]
        print("Систематический код с ошибкой:", ''.join(map(str, systemic_code_with_error)))
        
        # Обнаружение и исправление ошибки
        error_position, error_syndrom = search_error(N - K, d_min, systemic_code_with_error)
        print("Позиция ошибки:", error_position)
        print("Синдром ошибки:", error_syndrom)
        systemic_code_with_error[error_position - 1] = 1 - systemic_code_with_error[error_position - 1]
        print("Исправленный систематический код:", ''.join(map(str, systemic_code_with_error)))
        
        # Вывод исходного сообщения
        output_str = ''.join(map(str, systemic_code_with_error[:K]))
        print("Исходное сообщение:", output_str)
        print("Совпадает ли с входным:", input_str == output_str)
        print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    main()
