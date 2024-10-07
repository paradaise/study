import math
import random
import pandas as pd

N = 5
#а)  сгенерировать  массив  вероятностей  появления  совокупности  дискретных сообщений на входе информационного устройства (P(X))
def generate_P_X(N):
    P_X = [random.random() for _ in range(N)]
    P_X = [p / sum(P_X) for p in P_X]
    return P_X

#б) cгенерировать матрицу вероятностей перехода со входа на выход (P(X/Y)) (матрица условных вероятностей)
def generate_matrix_P_X_Y(N):
    P_X_Y = []
    for i in range(N):
        row = [(random.random()) for _ in range(N)]  
        row[i] = (random.uniform(0.7, 1)) 

        total = sum(row) - row[i]
        if total > 0:
            for j in range(N):
                if j != i:
                    row[j] = row[j] / total * (1 - row[i])

        P_X_Y.append(row)
    return P_X_Y

#в)  рассчитать вероятности появления совокупности дискретных сообщений на выходе информационного устройства P(Y)

def calculate_P_Y(P_X_Y, P_X):
    P_Y = [0] * len(P_X_Y)
    for j in range(len(P_X_Y)):
        for i in range(len(P_X_Y)):
            P_Y[j] += P_X[i] * P_X_Y[i][j]
    return P_Y


#г) рассчитать матрицу вероятностей совместных событий (P(X,Y))
def calculate_matrix_P_XY(P_X,P_X_Y):
    P_XY = [[0] * len(P_X_Y) for _ in range(len(P_X))]
    for i in range(len(P_X)):
        for j in range(len(P_X_Y)):
            P_XY[i][j] = P_X[i] * P_X_Y[i][j]
    return P_XY

#д)определить энтропию на входе информационного устройства (H(X))
def calculate_entropy(P_X):
    entropy = 0
    for p in P_X:
            entropy -= p * math.log2(p)
    return entropy

#e)определить условную  энтропию  выходного  сообщения относительно входного (H(Х/Y));
def calculate_conditional_entropy(P_XY,P_X_Y):
    H_X_Y = 0
    for i in range(len(P_XY)):
        for j in range(len(P_XY[i])):
            H_X_Y -= P_XY[i][j] * math.log2(P_X_Y[i][j])
    return H_X_Y

#ж)определить количество информации при неполной достоверности сообщений (I(X,Y))
def calculate_count_inf(H_X,H_X_Y):
    return H_X-H_X_Y


I_avg = 0
experement_count = 6

for i in range(experement_count):
    
    print(f"-------------------------ТЕСТ-№{i+1}-------------------------------")
    P_X = generate_P_X(N)
    P_X_Y = generate_matrix_P_X_Y(N)
    P_Y = calculate_P_Y(P_X_Y, P_X)
    P_XY = calculate_matrix_P_XY(P_X,P_X_Y)
    H_X = calculate_entropy(P_X)
    H_X_Y = calculate_conditional_entropy(P_XY,P_X_Y)
    I_X_Y = calculate_count_inf(H_X,H_X_Y)

    print("вероятности входных сообщений\n",pd.DataFrame(P_X).to_string(index=False, header=False))
    print("матрица вероятностей перехода со входа на выход (P(X/Y))\n",pd.DataFrame(P_X_Y).to_string(index=False, header=False))
    print("вероятности появления совокупности дискретных сообщений на выходе информационного устройства P(Y)\n",pd.DataFrame(P_Y).to_string(index=False, header=False))
    print("матрица вероятностей совместных событий (P(X,Y))\n",pd.DataFrame(P_XY).to_string(index=False, header=False))
    print(f"Энтропия на входе информационного устройства(H(X)): {H_X:.2f} бит")
    print(f"Остаточная энтропия выходного сообщения относительно входного(H(Х/Y)): {H_X_Y:.2f} бит")
    print(f"Количество информации при неполной достоверности сообщения: {I_X_Y:.2f} бит")

    I_avg += I_X_Y/experement_count


print("---------------------------------------------------------------------------------------------------------------------")
print(f"Среднее  количество  информации,  получаемое  при  неполной достоверности сообщений в ходе {experement_count} экспериментов: {I_avg/experement_count:.2f} бит")
    


