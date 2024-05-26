from scipy.stats import binom
import matplotlib.pyplot as plt

def ordenarArray(array): 
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                intercambiar(array, j, j + 1)

def intercambiar(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
    
def calcularMediana(array):
    if (len(array) % 2 != 0):
        return array[len(array)//2]
    else:
        valor1 = array[len(array) - 1]
        valor2 = array[len(array)]
        return (valor1 + valor2) / 2
    
def calcularModa(array):
    max = 0
    current = 0
    most_repeated = 0
    for i in range(len(array) - 1):
        if array[i] == array[i + 1]:
            current += 1
        else:
            if current > max:
                max = current
                most_repeated = array[i]
            current = 0
    return most_repeated
    
bin100 = binom.rvs(100, 0.35, size = 100)
bin1000 = binom.rvs(100, 0.35, size = 1000)
bin10000 = binom.rvs(100, 0.35, size = 10000)
bin100000 = binom.rvs(100, 0.35, size = 100000)

# print(bin1)
# print(bin2)
# print(bin3)
# print(bin4)

ordenarArray(bin100)
ordenarArray(bin1000)
ordenarArray(bin10000)
ordenarArray(bin100000)

data = [bin100, bin1000, bin10000, bin100000]

plt.boxplot(data, vert=False, tick_labels=['BIN 100', 'BIN 1000', 'BIN 10000', 'BIN 100000'])
plt.show()
