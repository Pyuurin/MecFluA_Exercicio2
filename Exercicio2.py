# Código feito por: Mariana Lopes Camilo, RA: 2058804
# Primeiramente, definirei os valores do enunciado do problema e adicionarei as bibliotecas math, numpy e matplotlib
import numpy as np
import pandas

g = 9.81  # gravidade em m/s²
d = 5  # diâmetro interno em mm
D = 50  # diâmetro externo em mm
y0 = 0.4  # y inicial
t0 = 0  # t inicial


# Definirei também a função obtida analiticamente como uma função python.
def f(t, y):
    return -pow(d/D, 2)*pow(2*g*y, 0.5)


# para N = 1
t = range(0, 25)  # cria um vetor de t indo de 0 até 25
y = np.zeros(len(t))  # cria um vetor de y com 25 números "0", um vetor nulo.
y[0] = y0
for n in range(0, len(t)-1):
    y[n+1] = y[n] + f(t[n], y[n])*(t[n+1]-t[n])  # método de Euler de t=0 até t=24
N1 = [y[0], y[6], y[12], y[18], y[24]]  # insiro os valores de y nos tempos desejados no vetor N1 (vetor de N=1)

# para N = 2
t = range(0, 25)  # reinicializo t e y
y = np.zeros(len(t))
y[0] = y0
for n in range(0, len(t)-1):
    y[n+1] = y[n] + f(t[n], y[n])*(t[n+1]-t[n])/2  # dividindo por 2 pois N =2
N2 = [y[0], y[6], y[12], y[18], y[24]]

# para N = 3
t = range(0, 25)
y = np.zeros(len(t))
y[0] = y0
for n in range(0, len(t)-1):
    y[n+1] = y[n] + f(t[n], y[n])*(t[n+1]-t[n])/3
N3 = [y[0], y[6], y[12], y[18], y[24]]

# para N = 4
t = range(0, 25)
y = np.zeros(len(t))
y[0] = y0
for n in range(0, len(t)-1):
    y[n+1] = y[n] + f(t[n], y[n])*(t[n+1]-t[n])/4
N4 = [y[0], y[6], y[12], y[18], y[24]]

# para N = 5
t = range(0, 25)
y = np.zeros(len(t))
y[0] = y0
for n in range(0, len(t)-1):
    y[n+1] = y[n] + f(t[n], y[n])*(t[n+1]-t[n])/5
N5 = [y[0], y[6], y[12], y[18], y[24]]

# para N = 6
t = range(0, 25)
y = np.zeros(len(t))
y[0] = y0
for n in range(0, len(t)-1):
    y[n+1] = y[n] + f(t[n], y[n])*(t[n+1]-t[n])/6
N6 = [y[0], y[6], y[12], y[18], y[24]]
# Tabelas
# Esta é uma função para obter a transposta de uma matriz,
# fonte: https://www.codegrepper.com/code-examples/python/transpose+matrix+in+python+without+numpy


def transpose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    matrix_T = []
    for j in range(columns):
        row = []
        for i in range(rows):
            row.append(matrix[i][j])
        matrix_T.append(row)

    return matrix_T


# df é a tabela, N0 é o cabeçalho da tabela.
N0 = ['t=0s', 't=6s', 't=12s', 't=18s', 't=24s']
dados = [N0 ,N1, N2, N3, N4, N5, N6]
transpose(dados)
df = pandas.DataFrame(data= dados)
print(df)  # mostra a tabela com t e N
