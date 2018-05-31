import numpy as np

temper = np.linspace(start=1, stop=8, num=8, dtype=float)
temp_layer = 2
temp_width = 2
temp_breadth = 2
temper = temper.reshape(temp_layer, temp_width, temp_breadth)

temper[0][0][0] = np.nan


def replace_miss(matrix):

    temp_matrix = np.zeros((temp_layer + 2, temp_width + 2, temp_breadth + 2))
    for index in range(1, len(temp_matrix) - 1):
        temp_matrix[index][1:-1, 1:-1] = matrix[index - 1]
    print temp_matrix
    for _i in range(temp_layer):
        for _j in range(temp_width):
            for _k in range(temp_breadth):
                if np.isnan(matrix[_i][_j][_k]):
                    _temp = np.nansum(temp_matrix[_i][_j + 1][_k + 1] + temp_matrix[_i + 2][_j + 1][_k + 1])
                    _temp += np.nansum(temp_matrix[_i + 1][_j][_k + 1] + temp_matrix[_i + 1][_j + 2][_k + 1])
                    _temp += np.nansum(temp_matrix[_i + 1][_j + 1][_k] + temp_matrix[_i + 1][_j + 1][_k + 2])
                    matrix[_i][_j][_k] = round(_temp * 1.0 / 6, 2)


replace_miss(temper)
print temper