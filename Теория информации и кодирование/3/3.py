import math
import random

N = 11
q = 1 / (2 * N)

#a)сгенерировать массив вероятностей появления совокупности сообщений на входе дискретного канала;

def generate_P_X(N):
    P_X = [random.random() for _ in range(N)]
    P_X = [p / sum(P_X) for p in P_X]
    return P_X

#б)сгенерировать длительности каждого символа сообщения;

def generate_time(N):
    message_times = [ random.uniform(0, q) for _ in range(N)]

    return message_times

'''#в)сгенерировать матрицу переходов со входа на выход в канале передачи информации 
с помехами с учетом технического задания, используя счетчик случайных чисел;'''

def generate_matrix_P_X_Y(N,q):
    P_X_Y_noise = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                P_X_Y_noise[i][j] = 1 - q
            else:
                P_X_Y_noise[i][j] = q / (N - 1)

    return P_X_Y_noise

def create_var(N,q):
    P_X_Y = generate_matrix_P_X_Y(N,q) # матрица переходов
    P_X = generate_P_X(N) # входные сообщения
    time = generate_time(N) # список длительности сообщений
    H_X = -sum([p * math.log2(p) for p in P_X]) # энтропия на входе в канал

    return P_X_Y,P_X,time,H_X

P_X_Y,P_X,time,H_X = create_var(N,q)

#г) рассчитать пропускную способность и скорость передачи при использовании канала без помех;

def calucalte_data_without_noise(H_X, time):
    capacity_no_noice = math.log2(N)/ sum(time)  # пропускная способность 
    speed_no_noise = H_X/ sum(time)  #  скорость В бит/с

    return {'Скорость': speed_no_noise,
        'П/с': capacity_no_noice}

#д) д) рассчитать пропускную способность и скорость передачи при использовании канала с помехами.
def calculate_data_with_noise(P_X,P_X_Y_noise,time):
    H_X_Y = 0 # 
    for i in range(N):
        for j in range(N):
                H_X_Y -= P_X[i] * P_X_Y_noise[i][j] * math.log2(P_X_Y_noise[i][j])
    
    speed_noise = (H_X - H_X_Y) / sum(time)
    capacity_noise = (math.log2(N) - H_X_Y) / sum(time)

    return {'Скорость':speed_noise,
            'П/с': capacity_noise}


no_noise = calucalte_data_without_noise(H_X,time)
noise = calculate_data_with_noise(P_X, P_X_Y, time)

print(round(no_noise['Скорость'],2),"- скорость без помех(бит/c)")
print(round(no_noise['П/с'],2),"- пропускная способность без помех (бит/c)")
print("----------------------------------------------------------")
print(round(noise['Скорость'],2),"- скорость c помехами (бит/c)")
print(round(noise['П/с'],2),"- пропускная способность c помехами (бит/c)\n")
print("----------------------------------------------------------")

avg_speed_noise = 0
avg_speed_no_noise = 0
avg_capacity_noise = 0
avg_capacity_no_noise = 0
k = 6

for i in range(k):
    P_X_Y,P_X,time,H_x = create_var(N,q)
    no_noise = calucalte_data_without_noise(H_X,time)
    noise = calculate_data_with_noise(P_X, P_X_Y, time)
    avg_speed_no_noise += no_noise['Скорость']
    avg_capacity_no_noise += no_noise['П/с']
    avg_speed_noise += noise['Скорость']
    avg_capacity_noise += noise['П/с']

print(f"Средняя скорость за {k} тестов без помех:{(avg_speed_no_noise/k):.2f} бит/c")
print(f"Средняя П/с за {k} тестов без помех:{(avg_capacity_no_noise/k):.2f} бит/c")
print('-------------------------------------------------------------')
print(f"Средняя скорость за {k} тестов с помехами:{(avg_speed_noise/k):.2f} бит/c")
print(f"Средняя П/с за {k} тестов с помехами:{(avg_capacity_noise/k):.2f} бит/c")

