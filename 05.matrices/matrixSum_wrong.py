"""
@author: Fábio Mori
"""

#Escola Matriz - Class 17: Matrices in Python
#Wrong implemented code

def cria_matriz (lin, col, valor):
    matriz=[]
    for i in range(lin):
        linha=[]
        for j in range(col):
            linha.append(valor)
            matriz.append(linha)
        return matriz

def soma_matriz(A,B):
    n_lin=len(A)
    n_col=len(A[0])
    C=cria_matriz(n_lin, n_col, 0)
    for lin in range(n_lin):
        for col in range(n_col):
            C[lin][col]=(A[lin][col])+(B[lin][col])
    return C

A=[[1, 3, 4], [3, 5, 1], [0, 1, 4]]
B=[[5, 3, 1], [3, 2, 0], [4, 1, 5]]

C=soma_matriz(A, B)
print(C)
