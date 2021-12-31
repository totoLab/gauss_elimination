import gauss_elimination

def product_determinant(matrix):
    determinant = 1

    minimum_dimension = len(matrix)
    if len(matrix) > len(matrix[0]):
        minimum_dimension = len(matrix[0])

    for i in range(minimum_dimension):
        determinant *= matrix[i][i]

    return determinant

def main(matrix):
    scaled_matrix, row_switches, pivot_list = gauss_elimination.main(matrix)
    sign = (-1)**row_switches
    determinant = sign * product_determinant(matrix)

    print("Determinant:", determinant)
    return determinant