import random
import ulm
import gauss_elimination
import determinant

def matrix_input(max_value):
    choices = ["Matrice inserita dall'utente", "Matrice casuale"]
    choice = determinant.cli_UI(choices, "Numero corrispondente al tipo di matrice: ")
    if choice == 0:
        matrix = ulm.leggi_matrice_int()
    elif choice == 1:
        choices = ["Quadrata", "No limitazioni"]
        choice = determinant.cli_UI(choices, "Numero corrispondente al tipo di matrice: ")
        if choice == 0:
            ordine = random.randint(1, 5)
            matrix = ulm.costruisci_matrice_valori_casuali(ordine, ordine, max_value)
        elif choice == 1:
            matrix = ulm.costruisci_matrice_valori_casuali(random.randint(1, 15), random.randint(1, 15), max_value)

    return matrix

def determinant_test(matrix, max_length):
    ulm.stampa_matrice_incolonnata(matrix, max_length)
    print("Determinante:", determinant.main(matrix))

def gauss_elimination_test(matrix, max_length):
    print("Matrice da ridurre")
    ulm.stampa_matrice_incolonnata(matrix, max_length)

    reduced_matrix, _, _ = gauss_elimination.main(matrix)
    print("Matrice ridotta")
    ulm.stampa_matrice_incolonnata(reduced_matrix, max_length)

def inverse_matrix_test(matrix, max_length):
    print("Matrice da invertire")
    ulm.stampa_matrice_incolonnata(matrix, max_length)

    inverted_matrix = inverted.main(matrix)
    if isinstance(inverted_matrix, list):
        print("Matrice inversa")
        ulm.stampa_matrice_incolonnata(inverted_matrix, len(str(max_value)))
    else:
        print("Errore:", inverted_matrix)

def general_test():
    element_max_value = 500
    max_element_length = len(str(element_max_value))

    operations = ["Determinante", "Riduzione di Gauss"]
    label = "Inserire il numero corrispondente all'operazione da svolgere: "
    choice = determinant.cli_UI(operations, label)

    matrix = matrix_input(element_max_value)

    if choice == 0:
        determinant_test(matrix, max_element_length)
    elif choice == 1:
        gauss_elimination_test(matrix, max_element_length)
    elif choice == 2:
        inverse_matrix_test(matrix, max_length)
general_test()