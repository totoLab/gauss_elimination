import gauss_elimination
import ulm

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

def two_by_two_determinant(matrix):
    first_term = matrix[0][0] * matrix[1][1]
    second_term = matrix[0][1] * matrix[1][0]
    return first_term - second_term

def find_most_zeros(matrix):
    best_row = (0, 0)
    for i in range(len(matrix)):
        zero_count = 0
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                zero_count += 1

        if zero_count > best_row[1]:
            best_row = i, zero_count

    return best_row[0] # if any, otherwise returns the first row index found

def find_sub_matrix(matrix, row, col):
    sub_matrix = []
    missing_one = 0
    for i in range(len(matrix)):
        if i != row:
            sub_matrix.append([])
            for j in range(len(matrix[0])):
                if j != col:
                    sub_matrix[i - missing_one].append(matrix[i][j])
        else:
            missing_one = 1

    return sub_matrix

def laplace_expansion(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return two_by_two_determinant(matrix)
    else:
        determinant = 0
        row = 0 # find_most_zeros(matrix)
        for col in range(len(matrix[0])):
            if matrix[row][col] != 0:
                sign = (-1)**(row + col)
                sub_matrix = find_sub_matrix(matrix, row, col)
                determinant += sign * matrix[row][col] * laplace_expansion(sub_matrix)

        return determinant

def cli_UI(algorithms, label):
    for i in range(len(algorithms)):
        print('{})'.format(i + 1), algorithms[i])
    
    choice = -1
    while not str(choice).isnumeric() or int(choice) - 1 not in range(len(algorithms)):
        choice = input(label)
    
    choice = int(choice) - 1
    print('You chose {}'.format(algorithms[choice]))
    return choice

def main(matrix):
    if not ulm.e_quadrata(matrix):
        return 'not a squared matrix'

    algorithms = ['Laplace Expansion', 'Diagonal Product']
    choice = cli_UI(algorithms, 'Insert the number of the algorithm you want to use: ')
    if choice == 0:
        determinant = laplace_expansion(matrix)
    elif choice == 1:
        determinant = product_determinant(matrix)

    return determinant