k = 61

def find_i(k):
    for i in range(k, 2*k):  # Начнем с k и будем проверять до 2*k
        if (i + 1) <= (2**(i - k)):
            return i
    return None

i = find_i(k)
print(i)