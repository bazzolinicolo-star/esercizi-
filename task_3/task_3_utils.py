"""Modulo Task 3"""

import numpy as np
def fun_esercizio_1(L:np.array)-> int:
    mass_valore = L[0, 0]
    for i in range (L.shape[0]):
        for j in range (L.shape[1]):
            if L[i, j] > mass_valore:
                mass_valore = L[i, j]
    return mass_valore



def fun_esercizio_2(matrice: int):
    a = len(matrice)
    for i in range(a):
        for j in range(i + 1, a):
            if matrice [i][j] != matrice [j][i]:
                return False 
    return True 



import numpy as np
def fun_esercizio_3(a, b):
    return a + b


 
def fun_esercizio_4(L):
    A = np.array(L, dtype = float)
    for i in range(len(A)):
        riga = A[i]
        s_riga = np.sum(riga)
        if s_riga!= 0:
            A[i] = riga / s_riga 
    return A



def fun_esercizio_5(L):
    B = np.array(L, dtype = float)
    somma_elementi = 0 
    N = len(B)
    for i in range(N):
        somma_elementi += B[i][i]
    return somma_elementi



if __name__ == "__main__":
    print("Modulo Task 3")