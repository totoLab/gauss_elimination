import gauss_elimination

def product_determinant(matrix):
    determinant = 1

    minimum_dimension = len(matrix)
    if len(matrix) > len(matrix[0]):
        minimum_dimension = len(matrix[0])

    for i in range(minimum_dimension):
        determinant *= matrix[i][i]

    return determinant

def cli_UI():
    algorithms = ['Laplace Expansion', 'Diagonal Product']
    for i in range(len(algorithms)):
        print('{})'.format(i + 1), algorithms[i])
    
    choice = -1
    while choice not in range(len(algorithms)):
        choice = int(input("Insert the number of the algorithm you want to use: ")) - 1
    
    print('You chose {}'.format(algorithms[choice]))
    return choice

def main(matrix):
    scaled_matrix, row_switches, pivot_list = gauss_elimination.main(matrix)
    sign = (-1)**row_switches
    determinant = sign * product_determinant(matrix)

    print("Determinant:", determinant)
    return determinant