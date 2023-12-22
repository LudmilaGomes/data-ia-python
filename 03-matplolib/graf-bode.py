from matplotlib import pyplot as plt
import numpy as np

# listas com valores de frequência e do ganho de tensão em decibel
freq = [10, 100, 200, 500, 1000, 10000, 100000, 1000000, 2000000, 10000000]
av_db = [6, 26, 31.4, 36, 38, 38, 38, 29, 23, 7.6]
# cria gráfico de pontos (freq, av_db)
plt.scatter(freq, av_db, color='red')
plt.xscale('log') # escala de x em log
plt.grid()

# listas com valores de frequência de corte e do ganho para frequência inferior e superior
av_db_corte = [35, 35]
freq_corte  = [400, 400000]
# exibe os pontos relativos às frequências de corte e um label com seus valores
plt.axhline(y=35, color='gray', linestyle=':')
plt.axvline(x=400, color='gray', linestyle=':')
plt.axvline(x=400000, color='gray', linestyle=':')
plt.scatter(freq_corte, av_db_corte, color='black')
labels = ['(400, 35)', '(400000, 35)']
for label, freq_c, av_db_c in zip(labels, freq_corte, av_db_corte):
    plt.annotate(label, xy=(freq_c, av_db_c), xytext=(0, -15), textcoords='offset points', ha='center')

# listas com valores para a curva teórica
freq_curva = [10, 100, 1000, 10000, 100000, 1000000, 2000000, 10000000]
av_db_curva = [6, 25.75, 38, 38, 38, 29.4, 24, 10]
# Realizar interpolação logarítmica
log_freq_curva = np.log10(freq_curva)
interp_func = np.poly1d(np.polyfit(log_freq_curva, av_db_curva, 7))  # Usando um polinômio de grau 6
# Criar pontos para a curva suave
log_freq_smooth = np.linspace(min(log_freq_curva), max(log_freq_curva), 500)
av_db_smooth = interp_func(log_freq_smooth)
freq_smooth = 10 ** log_freq_smooth
plt.plot(freq_smooth, av_db_smooth, label='modelo da curva teórica')

# título e labels do eixo x e y
plt.title("Gráfico de Bode - Amplificador")
plt.xlabel("f (Hz)")
plt.ylabel("Av(dB)")

plt.show()