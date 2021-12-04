import ulm
import gauss

def gauss_elimination(matrix):
    if ulm.e_nulla(matrix):
        print("Matrix is null.")
    else:
        pivot_list = []
        row_switches = 0
        gauss.convert_to_fractions(matrix)
        flow(matrix, pivot_list, row_switches)
        

def flow(matrix, pivot_list, row_switches):
    ulm.stampa_matrice_incolonnata(matrix, 5)
    print()
    pivot, row_switches = gauss.search_pivot(matrix, pivot_list, row_switches) # tuples unpacking
    pivot_list.append(pivot)
    if gauss.last_possible_pivot(matrix, pivot) or gauss.last_null_rows(matrix, pivot):
        print(pivot_list)
    else:
        if not gauss.exists_null_sub_column(matrix, pivot):
            gauss.generate_new_row(matrix, pivot)
            
        return flow(matrix, pivot_list, row_switches)

# example
matrix = [
    [0, 1/2,-1, 0],
    [0, 1, 1/2, 2],
    [4, 5, 4, 0.3333]
]
gauss_elimination(matrix)