import matplotlib.pyplot as plt
import statistics as stat
import locale

def calcular_media(array):
    sum = 0
    for i in range(len(array)):
        sum += array[i]
    return sum / len(array)

def calcular_mediana(array):
    if (len(array) % 2 != 0):
        return array[len(array)//2]
    else:
        valor1 = array[(len(array)//2) - 1]
        valor2 = array[(len(array)//2)]
        return (valor1 + valor2) / 2
    
def calcular_moda(array):
    if len(array) == 1:
        return [array[0]]
    max = 0
    array.sort()
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

def calcula_varianza_empirica(array):
    sum = 0
    media = stat.mean(array)
    for elem in array:
        x = (elem - media)**2
        sum += x
    return sum / (len(array) - 1)

def generar_histograma_binomial(array):
    plt.hist(array)
    locale.setlocale(locale.LC_ALL, '')
    plt.title(f"Muestra binomial de tamaño {locale.format('%d', len(array), 1)}")
    plt.ylabel(f"Veces que se obtuvo el resultado")
    plt.xlabel("Resultados de la muestra")
    plt.tight_layout()
    plt.gcf().set_size_inches(6, 6)
    plt.savefig(f"histograma_binomial_{len(array)}", dpi=125)
    plt.close()
    
def generar_histograma_geometrica(array):
    plt.hist(array)
    locale.setlocale(locale.LC_ALL, '')
    plt.title(f"Muestra geométrica de tamaño {locale.format('%d', len(array), 1)}")
    plt.ylabel(f"Veces que se obtuvo el resultado")
    plt.xlabel("Resultados de la muestra")
    plt.tight_layout()
    plt.gcf().set_size_inches(6, 6)
    plt.savefig(f"histograma_geometrica_{len(array)}", dpi=125)
    plt.close()

def generar_histograma_poisson(array):
    plt.hist(array)
    locale.setlocale(locale.LC_ALL, '')
    plt.title(f"Muestra de Poisson de tamaño {locale.format('%d', len(array), 1)}")
    plt.ylabel(f"Veces que se obtuvo el resultado")
    plt.xlabel("Resultados de la muestra")
    plt.tight_layout()
    plt.gcf().set_size_inches(6, 6)
    plt.savefig(f"histograma_poisson_{len(array)}", dpi=125)
    plt.close()