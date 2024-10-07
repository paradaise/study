
import pandas as pd
import random
import numpy as np


k = 61


def calucalte_n(k):
    n = 1
    while(2**k > ((2**n) / (n + 1 ))):
        n+=1

    return n
def calucalte_p(k,n):
    return n - k

n = calucalte_n(k)
p = calucalte_p(k,n)


def generete_P_n_k(k,p):
    arr = [ [random.randint(0,1) for i in range(p)]  for j in range(k)]
    
    return arr

P_n_k = generete_P_n_k(k,p)

def generete_H(matrix,p):
    # Преобразуем матрицу в numpy array для удобства
    np_matrix = np.array(matrix)
    
    # Извлекаем последние 3 столбца
    last_three_columns = np_matrix[:, -p:]
    
    # Транспонируем их
    transposed = last_three_columns.T
    
    # Извлекаем первые 3 столбца из транспонированной матрицы
    first_three_columns_transposed = transposed[:, :p]
    
    # Инвертируем их
    inverted_columns = np.flip(first_three_columns_transposed, axis=1)
    
    # Добавляем инвертированные столбцы в конец транспонированной матрицы
    result = np.hstack((transposed, inverted_columns))
    
    return result

H = generete_H(P_n_k,p)

print((H))


