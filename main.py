from scipy.stats import binom
from scipy.stats import geom
from scipy.stats import poisson
import matplotlib.pyplot as plt
import statistics as stat
import numpy as np
import funciones as f

# BINOMIAL
# a-) Genero muestras
bin100 = binom.rvs(100, 0.35, size = 100)
bin1000 = binom.rvs(100, 0.35, size = 1000)
bin10000 = binom.rvs(100, 0.35, size = 10000)
bin100000 = binom.rvs(100, 0.35, size = 100000)

data = [bin100, bin1000, bin10000, bin100000]

# b-) Genero diagrama de caja
plt.boxplot(data, vert=False, tick_labels=['100', '1000', '10000', '100000'])
plt.ylabel("Tamaño de la muestra")
plt.xlabel("Resultado de la muestra")
plt.tight_layout()
plt.gcf().set_size_inches(8, 5)
plt.savefig("diagrama_caja_binomial", dpi=150)
plt.close()

# c-) Genero histogramas
f.generar_histograma_binomial(bin100)
f.generar_histograma_binomial(bin1000)
f.generar_histograma_binomial(bin10000)
f.generar_histograma_binomial(bin100000)

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

# f-) Calculo varianza teorica
print(f"Varianza teórica de las 100 muestras con distribición binomial: {np.var(bin100)}")
print(f"Varianza teórica de las 1000 muestras con distribición binomial: {np.var(bin1000)}")
print(f"Varianza teórica de las 10000 muestras con distribición binomial: {np.var(bin10000)}")
print(f"Varianza teórica de las 100000 muestras con distribición binomial: {np.var(bin100000)}")


# GEOMTRICA
# a-) Genero muestras
geo100 = geom.rvs(0.08, size = 100)
geo1000 = geom.rvs(0.08, size = 1000)
geo10000 = geom.rvs(0.08, size = 10000)
geo100000 = geom.rvs(0.08, size = 100000)

data = [geo100, geo1000, geo10000, geo100000]

# b-) Genero diagrama de caja
plt.boxplot(data, vert=False, tick_labels=['100', '1000', '10000', '100000'])
plt.ylabel("Tamaño de la muestra")
plt.xlabel("Resultado de las muestra")
plt.tight_layout()
plt.gcf().set_size_inches(8, 5)
plt.savefig("diagrama_caja_geometrica", dpi=150)
plt.close()

# c-) Genero histogramas
f.generar_histograma_geometrica(geo100)
f.generar_histograma_geometrica(geo1000)
f.generar_histograma_geometrica(geo10000)
f.generar_histograma_geometrica(geo100000)

# d-) Calculo mediana y la moda
print(f"Mediana de las 100 muestras con distribición geométrica: {stat.median(geo100)}")
print(f"Mediana de las 1000 muestras con distribición geométrica: {stat.median(geo1000)}")
print(f"Mediana de las 10000 muestras con distribición geométrica: {stat.median(geo10000)}")
print(f"Mediana de las 100000 muestras con distribición geométrica: {stat.median(geo100000)}")

print(f"Moda de las 100 muestras con distribición geométrica: {stat.mode(geo100)}")
print(f"Moda de las 1000 muestras con distribición geométrica: {stat.mode(geo1000)}")
print(f"Moda de las 10000 muestras con distribición geométrica: {stat.mode(geo10000)}")
print(f"Moda de las 100000 muestras con distribición geométrica: {stat.mode(geo100000)}")

# e-) Calculo media
print(f"Media de las 100 muestras con distribición geométrica: {stat.mean(geo100)}")
print(f"Media de las 1000 muestras con distribición geométrica: {stat.mean(geo1000)}")
print(f"Media de las 10000 muestras con distribición geométrica: {stat.mean(geo10000)}")
print(f"Media de las 100000 muestras con distribición geométrica: {stat.mean(geo100000)}")

# f-) Calculo varianza teorica
print(f"Varianza teórica de las 100 muestras con distribición geométrica: {np.var(geo100)}")
print(f"Varianza teórica de las 1000 muestras con distribición geométrica: {np.var(geo1000)}")
print(f"Varianza teórica de las 10000 muestras con distribición geométrica: {np.var(geo10000)}")
print(f"Varianza teórica de las 100000 muestras con distribición geométrica: {np.var(geo100000)}")


# POISSON
# a-) Genero muestras
pois100 = poisson.rvs(30, size = 100)
pois1000 = poisson.rvs(30, size = 1000)
pois10000 = poisson.rvs(30, size = 10000)
pois100000 = poisson.rvs(30, size = 100000)

data = [pois100, pois1000, pois10000, pois100000]

# b-) Genero diagrama de caja
plt.boxplot(data, vert=False, tick_labels=['100', '1000', '10000', '100000'])
plt.ylabel("Tamaño de la muestra")
plt.xlabel("Resultado de la muestra")
plt.tight_layout()
plt.gcf().set_size_inches(8, 5)
plt.savefig("diagrama_caja_poisson", dpi=150)
plt.close()

# c-) Genero histogramas
f.generar_histograma_poisson(pois100)
f.generar_histograma_poisson(pois1000)
f.generar_histograma_poisson(pois10000)
f.generar_histograma_poisson(pois100000)

# d-) Calculo mediana y la moda
print(f"Mediana de las 100 muestras con distribición poisson: {stat.median(pois100)}")
print(f"Mediana de las 1000 muestras con distribición poisson: {stat.median(pois1000)}")
print(f"Mediana de las 10000 muestras con distribición poisson: {stat.median(pois10000)}")
print(f"Mediana de las 100000 muestras con distribición poisson: {stat.median(pois100000)}")

print(f"Moda de las 100 muestras con distribición poisson: {stat.mode(pois100)}")
print(f"Moda de las 1000 muestras con distribición poisson: {stat.mode(pois1000)}")
print(f"Moda de las 10000 muestras con distribición poisson: {stat.mode(pois10000)}")
print(f"Moda de las 100000 muestras con distribición poisson: {stat.mode(pois100000)}")

# e-) Calculo media
print(f"Media de las 100 muestras con distribición poisson: {stat.mean(pois100)}")
print(f"Media de las 1000 muestras con distribición poisson: {stat.mean(pois1000)}")
print(f"Media de las 10000 muestras con distribición poisson: {stat.mean(pois10000)}")
print(f"Media de las 100000 muestras con distribición poisson: {stat.mean(pois100000)}")

# f-) Calculo varianza teorica
print(f"Varianza teórica de las 100 muestras con distribición poisson: {np.var(pois100)}")
print(f"Varianza teórica de las 1000 muestras con distribición poisson: {np.var(pois1000)}")
print(f"Varianza teórica de las 10000 muestras con distribición poisson: {np.var(pois10000)}")
print(f"Varianza teórica de las 100000 muestras con distribición poisson: {np.var(pois100000)}")
