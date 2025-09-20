# Showcasing two dimensional array - Slicing
import numpy as np

matrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(matrix)

second_row = matrix[1, :]
print("second row is \n", second_row)

third_column = matrix[:, 2]
print("third column is \n", third_column)

sub_matrix = matrix[:2, 1:3]
print("sub matrix is \n", sub_matrix)
