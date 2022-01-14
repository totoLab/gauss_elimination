import gauss_elimination
import ulm
import determinant
import random

def verify_results():
    results = {'equal': 0, 'different': 0}
    for i in range(10):
        matrix = ulm.costruisci_matrice_valori_casuali(10,10,305239463467)
        #ulm.stampa_matrice(matrix)
        laplace = determinant.laplace_expansion(matrix)
        diagonal = determinant.product_determinant(matrix)

        if laplace == diagonal:
            results['uguali'] += 1
        elif laplace != diagonal:
            results['diversi'] += 1
        else:
            print('errore')

    print(results)

def test():
    max_value = 50000

    choices = ["Matrice inserita dall'utente", "Matrice casuale"]
    choice = determinant.cli_UI(choices, "Numero corrispondente al tipo di matrice: ")
    if choice == 0:
        matrix = ulm.leggi_matrice_int()
    elif choice == 1:
        matrix = ulm.costruisci_matrice_valori_casuali(random.randint(1, 15), random.randint(1, 15), max_value)

    ulm.stampa_matrice_incolonnata(matrix, len(str(max_value)))
    print("Determinante:", determinant.main(matrix))

test()