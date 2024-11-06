# Importa a biblioteca NumPy, que contém funções matemáticas
import numpy as np

# Recebe um valor de matriz do usuário, valor do tipo inteiro
n = int(input("Informe o tamanho da matriz:"))

# Cria uma matriz de zeros de dimensão n x n
A = np.zeros((n,n))

# Preenche a matriz A com valores fornecidos pelo usuário
for i in range(n):
  for j in range(n):
    A[i,j] = float(input(f'A[{i+1},{j+1}]'))

# Calcula o determinante da matriz A
detA = np.linalg.det(A)

# Define os termos independentes
B = np.zeros(n)

# Preenche o vetor B com valores fornecidos pelo usuário
for i in range(n):
  B[i] = float(input(f'B[{i+1}]'))

# Cria uma cópia da matriz A
Ax = A.copy()

# Substitui a primeira coluna de Ax pelos valores de B
for i in range(n):
  Ax[i][0] = B[i]

# Calcula o determinante da matriz Ax
detAx = np.linalg.det(Ax)

# Verifica se o determinante de A é diferente de zero
if detA != 0:
  # Se for diferente de zero, resolve o sistema linear A * x = B
  S = np.linalg.solve(A,B)
  print(f'Sistema Possível Determinado: {S}')
else:
  # Se o determinante de A for zero, verifica o determinante de Ax
  if detA == 0 and detAx == 0:
    # Se ambos os determinantes forem zero, o sistema é possível e indeterminado
    print("Sistema Possível e Indeterminado")
  else:
    # Se apenas o determinante de A for zero, o sistema é impossível
    print("Sistema Impossível")
