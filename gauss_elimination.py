import ulm
import gauss

def main(matrix):
    if ulm.e_nulla(matrix):
        print("Matrix is null.")
    else:
        pivot_list = []
        row_switches = 0
        gauss.convert_to_fractions(matrix)
        row_switches, pivot_list = flow(matrix, pivot_list, row_switches)

    return matrix, row_switches, pivot_list
        
def print_and_exit(matrix, row_switches, pivot_list):
    #ulm.stampa_matrice_incolonnata(matrix, 10)
    return row_switches, pivot_list

def flow(matrix, pivot_list, row_switches):
    #ulm.stampa_matrice_incolonnata(matrix, 10)
    pivot, row_switches = gauss.search_pivot(matrix, pivot_list, row_switches) # tuples unpacking
    pivot_list.append(pivot)
    if gauss.last_possible_pivot(matrix, pivot):
        return print_and_exit(matrix, row_switches, pivot_list)
    else:
        if not gauss.exists_null_sub_column(matrix, pivot):
            gauss.generate_new_row(matrix, pivot)
            
        if gauss.last_null_rows(matrix, pivot):
            return print_and_exit(matrix, row_switches, pivot_list)

        return flow(matrix, pivot_list, row_switches)