""""
10/2021 - Código da resposta de um circuito RLC série, todos os casos são contemplados.
"""

import matplotlib.pyplot as plt
import numpy as np
import math

# Lista cujos elementos serão os segundos.
t = np.arange(start=0, stop=10, step=0.001)

# Lista vazia cujos elementos serão os valores de tensão a cada segundo.
v1 = []
v2 = []
v3 = []

# A função range gerará uma lista iterável com intervalo entre os tempos constante e igual a 1.
# O equacionamento de vc1 e vc2 fica a cargo do usuário

for i in range(len(t)):
    vt1 = 20 - 13.3333*math.e**(-t[i]) + 3.3333*math.e**(-4*t[i])
    v1.append(vt1)

for i in range(len(t)):
    vt2 = 20 + (-10-20*t[i])*math.e**(-2*t[i])
    v2.append(vt2)

for i in range(len(t)):
    vt3 = 20 + (-10*math.cos(1.9365*t[i]) - 2.5820*math.sin(1.9365*t[i]))*math.e**(-0.5*t[i])
    v3.append(vt3)

# A função x.append(y) preencherá um vetor x previamente criado com os valores da variável y.
# A variável tempo precisa ser abatida em ts para que este novo tempo seja considerado um novo zero.

# Formatação do plot gerado.
plt.style.use('seaborn-dark')

plt.xlabel('\nt, s')
plt.ylabel('Vc(t), V\n')
plt.title('Tensão Vc(t) para os três tipos de comportamento\n')
plt.plot(t, v1, label='Sobre-amortecido')
plt.plot(t, v2, label='Amortecido')
plt.plot(t, v3, label='Sub-amortecido')
plt.grid(True)

plt.legend(framealpha=1, frameon=True, facecolor='white')
plt.show()
