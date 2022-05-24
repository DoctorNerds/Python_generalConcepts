"""
@author: Fábio Mori
"""

#Escola Matriz - Class 17: Matrices in Python
#Fixed implemented code

def mult_matriz(A,B):
    n_lin_A, n_col_A = len(A), len(A[0])
    n_lin_B, n_col_B = len(B), len(B[0])
    C=[]
    for linha in range(n_lin_A):
        C.append([])
        for coluna in range(n_col_B):
            C[linha].append(0)
            for k in range(n_col_A):
                C[linha][coluna]+=(A[linha][k])*(B[k][coluna])
    return C

A=[[1, 3, 4], [3, 5, 1], [0, 1, 4]]
B=[[5, 3, 1], [3, 2, 0], [4, 1, 5]]

C=mult_matriz(A, B)
print(C)
