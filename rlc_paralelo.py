""""
09/2021 - Código da resposta de um circuito RLC paralelo, todos os casos são contemplados.
"""

import matplotlib.pyplot as plt
import numpy as np
import math

R = float(input('Valor de R [ohm]: '))  #80
L = float(input('Valor de L [H]: '))  #200 * 10 ** -3
C = float(input('Valor de C [F]: '))  #5 * 10 ** -6

vc0 = float(input('Tensão armazenada no capacitor [V]: '))  #10
il0 = float(input('Corrente armazenada no indutor [A]: '))  #-0.6
ts = float(input('Tempo de simulação [s]: '))  #0.05

# Fator de amortecimento.
a = 1/(2*R*C)

# Frequência natural não amortecida.
w = 1/math.sqrt(L*C)

# Lista cujos elementos serão os segundos.
t = np.arange(start=0, stop=ts, step=ts/1000)

# Lista vazia cujos elementos serão os valores de tensão a cada segundo.
v = []

# A função range gerará uma lista iterável com intervalo entre os tempos constante e igual a 1.
# O equacionamento de vc1 e vc2 fica a cargo do usuário

for i in range(len(t)):
    if a > w:
        # Raízes do sistema
        s1 = -a + math.sqrt(a**2 - w**2)
        s2 = -a - math.sqrt(a**2 - w**2)
        # Condições iniciais
        ic0 = -(vc0/R) - il0
        dvc0 = ic0/C
        # Coeficientes da equação de comportamento
        A1 = ((vc0*s2)-dvc0)/(s2-s1)
        A2 = (dvc0-(vc0*s1))/(s2-s1)
        vt = A1*math.e**(s1*t[i]) + A2*math.e**(s2*t[i])
        v.append(vt)
    elif a == w:
        s1 = -a
        s2 = -a
        ic0 = -(vc0/R) - il0
        dvc0 = ic0/C
        B1 = vc0
        B2 = dvc0 - (s1*B1)
        vt = B1*math.e**(s1*t[i]) + B2*t[i]*math.e**(s2*t[i])
        v.append(vt)
    elif a < w:
        s1 = complex(-a, math.sqrt(-(a**2 - w**2)))
        s2 = complex(-a, -math.sqrt(-(a**2 - w**2)))
        wd = s1.imag
        ic03 = -(vc0/R) - il0
        dvc03 = ic03/C
        C1 = vc0
        C2 = (dvc03+(-s1.real*C1))/wd
        vt = (C1*math.cos(wd*t[i]) + C2*math.sin(wd*t[i])) * math.e**(s1.real*t[i])
        v.append(vt)

# A função x.append(y) preencherá uma lista x previamente criada com os valores da variável y.

# Formatação do plot gerado.
plt.style.use('seaborn-dark')

plt.xlabel('\nt, s')
plt.ylabel('Vc(t), V\n')
plt.title('Tensão Vc(t)\n')
plt.plot(t, v)
plt.grid(True)

plt.tight_layout()
plt.show()
