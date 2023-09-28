"""
Вычисление средних в большой матрице с помощью NumPy
с. 220
"""
import numpy as np
import time

data_points = 3000000000
rows = 50
columns = int(data_points / rows)

matrix = np.arange(data_points).reshape(rows, columns)

s = time.time()

res = np.mean(matrix, axis=1)

e = time.time()
print(e - s)
