import ulm
import fractions
import to_fraction

def convert_to_fractions(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if type(matrix[i][j]) != int:
                matrix[i][j] = fractions.Fraction(to_fraction.main(matrix[i][j])) # converts imprecise decimals first to strings, then to fractions

def search_pivot(matrix, pivot_list, row_switches):
    # next pivot's row is always the length of the pivot list + 1, if the list doesn't have length zero
    starting_row = 0 if len(pivot_list) == 0 else len(pivot_list)
    # check from the first if there are no pivots, otherwise check from pivot's coloumn pivot + 1
    starting_coloumn = 0 if len(pivot_list) == 0 else pivot_list[len(pivot_list) - 1][1][1] + 1
    matrix_rows = len(matrix)
    matrix_coloumns = len(matrix[0])
    for j in range(starting_coloumn, matrix_coloumns):
        for i in range(starting_row, matrix_rows):    
            if matrix[i][j] != 0:
                if i != starting_row:
                    reposition_pivot(matrix, i, starting_row)
                    row_switches += 1
                    pivot = matrix[starting_row][j]
                    return (pivot, (starting_row, j)), row_switches
                else:
                    return (matrix[i][j], (i, j)), row_switches

def reposition_pivot(matrix, non_zero_element_row, correct_row):
    ulm.scambia_righe(matrix, non_zero_element_row, correct_row)

def last_possible_pivot(matrix, pivot):
    matrix_rows = len(matrix)
    matrix_coloumns = len(matrix[0])
    coordinates = pivot[1]
    pivot_row = coordinates[0]
    pivot_coloumn = coordinates[1]
    if pivot_row == matrix_rows - 1 or pivot_coloumn == matrix_coloumns - 1:
        return True
    
    return False

def last_null_rows(matrix, pivot):
    matrix_rows = len(matrix)
    matrix_coloumns = len(matrix[0])
    coordinates = pivot[1]
    pivot_row = coordinates[0]
    pivot_coloumn = coordinates[1]
    for i in range(pivot_row + 1, matrix_rows):
        for j in range(matrix_coloumns):
            if matrix[i][j] != 0:
                return False
    
    return True

def exists_null_sub_column(matrix, pivot):
    pivot_row = pivot[1][0]
    pivot_coloumn = pivot[1][1]
    for i in range(pivot_row + 1, len(matrix)):
        if matrix[i][pivot_coloumn] != 0:
            return False

    return True

def generate_new_row(matrix, pivot):
    pivot_coordinates = pivot[1]
    pivot_row = pivot_coordinates[0]
    pivot_coloumn = pivot_coordinates[1]
    for i in range(pivot_row + 1, len(matrix)):
        row_multiplicator = fractions.Fraction(matrix[i][pivot_coloumn]) / pivot[0] # multiplicator is the same for every element of the row
        for j in range(pivot_coloumn, len(matrix[0])):
            first_sub_matrix_element = matrix[pivot_row][j]
            matrix[i][j] -= row_multiplicator * first_sub_matrix_element