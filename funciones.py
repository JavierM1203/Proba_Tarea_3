
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