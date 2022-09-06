import numpy as np
import scipy.linalg as linalg

############################ (a) ############################

# A = np.array([[3,1],
#              [9,5]])
# print("A:", A)

# P, L, U = linalg.lu(A)

# print("P:", P)
# print("L:", L)
# print("U:", U)

# ALU = np.dot(L,U)
# print("LU:", ALU)

############################ (b) ############################
B = np.array([[1, 1, 1],
             [3, 5, 6],
             [-2, 2, 7]])
print("B:\n", B)

P, L, U = linalg.lu(B)

print("P:\n", P)
print("L:\n", L)
print("U:\n", U)

ALU = np.dot(L, U)
print("LU:\n", ALU)

# using doolittle algorithm

# [L][U] = LUdecomp([A])


def LUdecomp(a):
    n = len(a)
    for k in range(0, n-1):
        for i in range(k+1, n):
            if a[i, k] != 0.0:
                lam = a[i, k]/a[k, k]
                a[i, k+1:n] = a[i, k+1:n] - lam*a[k, k+1:n]
                a[i, k] = lam
    return a


B_doo = LUdecomp(B)
print("B using doolittle:\n", B_doo)

L_doo = np.array([[1, 0, 0],
                 [B_doo[1, 0], 1, 0],
                 [B_doo[2, 0], B_doo[2, 1], 1]])
print("L:\n", L_doo)

U_doo = np.array([[B_doo[0, 0], B_doo[0, 1], B_doo[0, 2]], [
                 0, B_doo[1, 1], B_doo[1, 2]], [0, 0, B_doo[2, 2]]])
print("U:\n", U_doo)
