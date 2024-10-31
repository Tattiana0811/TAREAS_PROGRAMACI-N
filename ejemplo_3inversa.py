import numpy as np 

A = [
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
]
B=np.linalg.inv(A)
print("La matriz original es: ")
print(A)
print("La inversa de A es: ")
print(B)


C=np.array([[1,2],[2,4]])

det= np.linalg.det(C)

D= np.linalg.inv(C)

print("Matriz C")
print(C)
print("Determinante de C", det)
print("Inversa", D)

