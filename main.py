from scipy.stats import binom
import matplotlib.pyplot as plt
import statistics as stat
import numpy as np
import funciones as f

def generar_histograma_binomial(array):
    plt.hist(array)
    plt.ylabel(f"Veces que se obtuvo cada resultado al repetir el experimento {len(array)} veces")
    plt.xlabel("Cantidad de resultados exitosos con distribución binomial donde n = 100")
    plt.tight_layout()
    plt.gcf().set_size_inches(6, 6)
    plt.savefig(f"histograma_binomial_{len(array)}", dpi=150)
    plt.close()

bin100 = binom.rvs(100, 0.35, size = 100)
bin100.sort()
bin1000 = binom.rvs(100, 0.35, size = 1000)
bin1000.sort()
bin10000 = binom.rvs(100, 0.35, size = 10000)
bin10000.sort()
bin100000 = binom.rvs(100, 0.35, size = 100000)
bin100000.sort()

data = [bin100, bin1000, bin10000, bin100000]

plt.boxplot(data, vert=False, tick_labels=['100', '1000', '10000', '100000'])
plt.ylabel("Cantidad de repeticiones")
plt.xlabel("Resultados exitosos con distribución binomial donde n = 100 y p = 0.35")
plt.tight_layout()
plt.gcf().set_size_inches(8, 5)
plt.savefig("diagrama_caja_binomial", dpi=150)
plt.close()

generar_histograma_binomial(bin100)
generar_histograma_binomial(bin1000)
generar_histograma_binomial(bin10000)
generar_histograma_binomial(bin100000)

print(f"Media de las 100 muestras con distribición binomial: {np.mean(bin100)}")
print(f"Media de las 1000 muestras con distribición binomial: {np.mean(bin1000)}")
print(f"Media de las 10000 muestras con distribición binomial: {np.mean(bin10000)}")
print(f"Media de las 100000 muestras con distribición binomial: {np.mean(bin100000)}")
