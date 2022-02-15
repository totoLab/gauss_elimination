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
            results['equal'] += 1
        elif laplace != diagonal:
            results['different'] += 1
        else:
            print('error')

    print(results)

def test():
    max_value = 50000

    choices = ["Matrix from user input", "Casual Matrix"]
    choice = determinant.cli_UI(choices, "Number of type of matrix you want to use: ")
    if choice == 0:
        matrix = ulm.leggi_matrice_int()
    elif choice == 1:
        choices = ["Squared", "No boundaries"]
        choice = determinant.cli_UI(choices, "Number of type of matrix you want to use: ")
        if choice == 0:
            ordine = random.randint(1, 5)
            matrix = ulm.costruisci_matrice_valori_casuali(ordine, ordine, max_value)
        elif choice == 1:
            matrix = ulm.costruisci_matrice_valori_casuali(random.randint(1, 15), random.randint(1, 15), max_value)

    ulm.stampa_matrice_incolonnata(matrix, len(str(max_value)))
    print("Determinant:", determinant.main(matrix))

test()