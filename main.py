from scipy.stats import binom
import matplotlib.pyplot as plt
import statistics as stat
import funciones as f

def generar_histograma_binomial(array):
    plt.hist(array)
    plt.ylabel(f"Veces que se obtuvo cada resultado al repetir el experimento {len(array)} veces")
    plt.xlabel("Cantidad de resultados exitosos con distribución binomial donde n = 100")
    plt.tight_layout()
    plt.gcf().set_size_inches(6, 6)
    plt.savefig(f"histograma_binomial_{len(array)}", dpi=150)
    plt.close()

# BINOMIAL
# a-) Genero muestras
bin100 = binom.rvs(100, 0.35, size = 100)
bin1000 = binom.rvs(100, 0.35, size = 1000)
bin10000 = binom.rvs(100, 0.35, size = 10000)
bin100000 = binom.rvs(100, 0.35, size = 100000)

data = [bin100, bin1000, bin10000, bin100000]

# b-) Genero diagrama de caja
plt.boxplot(data, vert=False, tick_labels=['100', '1000', '10000', '100000'])
plt.ylabel("Cantidad de repeticiones")
plt.xlabel("Resultados exitosos con distribución binomial donde n = 100 y p = 0.35")
plt.tight_layout()
plt.gcf().set_size_inches(8, 5)
plt.savefig("diagrama_caja_binomial", dpi=150)
plt.close()

# c-) Genero histogramas
generar_histograma_binomial(bin100)
generar_histograma_binomial(bin1000)
generar_histograma_binomial(bin10000)
generar_histograma_binomial(bin100000)


# d-) Calculo mediana y la moda
print(f"Mediana de las 100 muestras con distribición binomial: {stat.median(bin100)}")
print(f"Mediana de las 1000 muestras con distribición binomial: {stat.median(bin1000)}")
print(f"Mediana de las 10000 muestras con distribición binomial: {stat.median(bin10000)}")
print(f"Mediana de las 100000 muestras con distribición binomial: {stat.median(bin100000)}")

print(f"Moda de las 100 muestras con distribición binomial: {stat.mode(bin100)}")
print(f"Moda de las 1000 muestras con distribición binomial: {stat.mode(bin1000)}")
print(f"Moda de las 10000 muestras con distribición binomial: {stat.mode(bin10000)}")
print(f"Moda de las 100000 muestras con distribición binomial: {stat.mode(bin100000)}")

# e-) Calculo media
print(f"Media de las 100 muestras con distribición binomial: {stat.mean(bin100)}")
print(f"Media de las 1000 muestras con distribición binomial: {stat.mean(bin1000)}")
print(f"Media de las 10000 muestras con distribición binomial: {stat.mean(bin10000)}")
print(f"Media de las 100000 muestras con distribición binomial: {stat.mean(bin100000)}")


