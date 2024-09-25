import random
import math

N = 10

def calculate_information(probs):
    information = 0
    for p in probs:
            information -= p * math.log2(p)
    return information


for i in range(1,7):
    N = N + 1
    print(f"-----------------ТЕСТ-{i}------------------")
    probabilities = [random.random() for _ in range(N)]
    normalize_probabilities = [p / sum(probabilities) for p in probabilities]

    max_entropy = math.log2(N)  # (Формула Шеннона)
    average_information = calculate_information(normalize_probabilities)
    
    print(f"N:{N}")
    print(f"Вероятности: {normalize_probabilities}")
    print(f"Максимальная энтропия: {max_entropy:.4f} бит")
    print(f"Среднее количество информации: {average_information:.4f} бит")

    print ("---------------------------------------------")
    
