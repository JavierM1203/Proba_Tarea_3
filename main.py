from scipy.stats import binom
import matplotlib.pyplot as plt

def calcular_media(array):
    sum = 0
    for i in range(len(array)):
        sum += array[i]
    return sum / len(array)

def calcular_mediana(array):
    if (len(array) % 2 != 0):
        return array[len(array)//2]
    else:
        valor1 = array[len(array) - 1]
        valor2 = array[len(array)]
        return (valor1 + valor2) / 2
    
def calcular_moda(array):
    max = 0
    current = 0
    results = []
    for i in range(len(array) - 1):
        if array[i] == array[i + 1]:
            current += 1
        if current > max:
            max = current
            results.clear()
        if array[i] != array[i + 1] or i + 1 == len(array) - 1:
            if current == max:
                results.append(array[i])
            current = 0
        if i + 1 == len(array) - 1 and max == 0:
            results.append(array[i + 1])
    return results
    
bin100 = binom.rvs(100, 0.35, size = 100)
bin1000 = binom.rvs(100, 0.35, size = 1000)
bin10000 = binom.rvs(100, 0.35, size = 10000)
bin100000 = binom.rvs(100, 0.35, size = 100000)

bin100.sort()
bin1000.sort()
bin10000.sort()
bin100000.sort()

print(bin100)

print(calcular_moda([1, 2, 3, 4]))
print(calcular_media(bin1000))
print(calcular_media(bin10000))
print(calcular_media(bin100000))

# data = [bin100, bin1000, bin10000, bin100000]

# plt.boxplot(data, vert=False, tick_labels=['BIN 100', 'BIN 1000', 'BIN 10000', 'BIN 100000'])
# plt.show()
