import gauss_elimination
import ulm
import gauss
import determinant
import fractions

def aside_matrix(m1, m2):
    matrix = []
    for row1, row2 in zip(m1, m2):
        new_row = row1 + row2
        matrix.append(new_row)

    return matrix

def half_matrix_rows(matrix):
    m1 = []
    m2 = []
    half_length = int(len(matrix[0])/2)
    for row in matrix:
        first = row[:half_length]
        m1.append(first)

        second = row[half_length:]
        m2.append(second)

    return m1, m2

def setup_inversion(matrix):
    ordine = len(matrix)
    identita = ulm.costruisci_matrice_identita(ordine)
    matrix_plus_identity = aside_matrix(matrix, identity)
    return matrix_plus_identity

def mirror_matrix(matrix):
    mirrored = []
    for i in range(len(matrix), 0, -1):
        mirrored.append(matrix[i - 1][::-1])

    return mirrored

def mirror_and_glue(matrix):
    halfed_matrices = half_matrix_rows(matrix)
    matrices = []
    for matrix in halfed_matrices:
        matrices.append(mirror_matrix(matrix))

    matrix = aside_matrix(matrices[0], matrices[1])
    return matrix, matrices[0]

def fix_diagonal(matrix, diagonal_original):
    for i in range(len(diagonal_original)):
        element = diagonal_original[i][i]
        if element != 1:
            multiplicator = fractions.Fraction(1/element)

            for j in range(len(matrix[i])):
                matrix[i][j] *= multiplicator

    return matrix

def main(matrix):
    gauss.convert_to_fractions(matrix)

    matrix_plus = setup_inversion(matrix)
    scaled, _, _ = gauss_elimination.main(matrix_plus) # whole gauss reduction

    matrix, first_matrix = mirror_and_glue(scaled) # returns a mirrored version of the same individual matrices
    det = determinant.product_determinant(first_matrix) 
    if det != 0: # invertibility check on the original matrix
        scaled, _, _ = gauss_elimination.main(matrix) # gauss-jordan last step

        matrix, scaled_original = mirror_and_glue(scaled) # re-mirroring to have the correct reduced matrix

        matrix = fix_diagonal(matrix, scaled_original) # fix diagonal with row multiplication
        identity, inverted = half_matrix_rows(matrix) # splitting to return only the inverted
        return inverted
    else:
        return "matrix is not invertible"