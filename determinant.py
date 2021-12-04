import gauss_elimination

def calc_determinant(pivot_list):
    det = 1 # neutral value of the multiplication
    for pivot in pivot_list:
        det *= pivot[0]

    return det

def main(matrix):
    scaled_matrix, row_switches, pivot_list = gauss_elimination.main(matrix)
    sign = (-1)**row_switches
    determinant = sign * calc_determinant(pivot_list)

    print("Determinant:", determinant)
    return determinant

# example
# matrix = [
#     [0, 3, 6],
#     [1, 4, 7],
#     [2, 6, 8]
# ]
# main(matrix)