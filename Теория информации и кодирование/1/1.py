import random
import math
import pandas as pd



def calculate_information(probs): #Формула Шеннона
    information = 0
    for p in probs:
            information -= p * math.log2(p)
    return information


def generate_array(N):
    probabilities = [random.random() for _ in range(N)]
    normalize_probabilities = [p / sum(probabilities) for p in probabilities]
    return normalize_probabilities

avg_inf = 0
experement_count = 6

for i in range(experement_count):

    N = 11
    print(f"-----------------ТЕСТ-{i+1}------------------")

    normalize_probabilities = generate_array(N)
    max_entropy = math.log2(N)
    average_information = calculate_information(normalize_probabilities)
    
    print(f"Вероятности:\n{pd.DataFrame(normalize_probabilities).to_string(header=False)}")
    print(f"Максимальная энтропия: {max_entropy:.4f} бит")
    print(f"Количество информации: {average_information:.4f} бит")
    
    avg_inf += average_information

print("---------------------------------------------------------------------------------------------")
print(f"Среднее кол-во информации за {experement_count} эксперементов:{avg_inf/experement_count} бит")

