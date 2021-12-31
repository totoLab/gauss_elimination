import gauss_elimination

def product_determinant(matrix):
    determinant = 1

    scaled_matrix, row_switches, _ = gauss_elimination.main(matrix)
    sign = (-1)**row_switches
    
    minimum_dimension = len(matrix)
    if len(scaled_matrix) > len(scaled_matrix[0]):
        minimum_dimension = len(scaled_matrix[0])

    for i in range(minimum_dimension):
        determinant *= scaled_matrix[i][i]
    
    return sign * determinant

def laplace_expansion(matrix):
    pass #TODO

def cli_UI(algorithms):
    for i in range(len(algorithms)):
        print('{})'.format(i + 1), algorithms[i])
    
    choice = -1
    while choice not in range(len(algorithms)):
        choice = int(input("Insert the number of the algorithm you want to use: ")) - 1
    
    print('You chose {}'.format(algorithms[choice]))
    return choice

def main(matrix):
    algorithms = ['Laplace Expansion', 'Diagonal Product']
    choice = cli_UI(algorithms)
    if choice == 0:
        determinant = laplace_expansion(matrix)
    elif choice == 1:
        determinant = product_determinant(matrix)

    print("Determinant:", determinant)
    return determinant