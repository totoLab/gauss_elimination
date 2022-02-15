import random
import ulm
import gauss_elimination
import determinant
import inverse
import json
import fractions

class FractionEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, fractions.Fraction):
            fraction = f"{o.numerator}/{o.denominator}"
            return (str(fraction) for fraction in [fraction])

        return super(FractionEncoder, self).default(o)

def matrix_everything(matrix):
    info = {
        "Matrix": [],
        "Determinant": 0,
        "Gauss Reduction": [],
        "Inverse": []
    }
    det = determinant.product_determinant(matrix)
    gauss_reduction = gauss_elimination.main(matrix)
    inverse_matrix = inverse.main(matrix)
    info.update({
        "Matrix": matrix,
        "Determinant": det,
        "Gauss Reduction": gauss_reduction,
        "Inverse": inverse_matrix
    })

    return info


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

    inverse_matrix = inverse.main(matrix)
    if isinstance(inverse_matrix, list):
        print("Matrice inversa")
        ulm.stampa_matrice_incolonnata(inverse_matrix, max_length)
    else:
        print("Errore:", inverse_matrix)

def general_test(element_max_value):
    max_element_length = len(str(element_max_value))

    operations = ["Determinante", "Riduzione di Gauss", "Matrice Inversa"]
    label = "Inserire il numero corrispondente all'operazione da svolgere: "
    choice = determinant.cli_UI(operations, label)

    matrix = matrix_input(element_max_value)

    if choice == 0:
        determinant_test(matrix, max_element_length)
    elif choice == 1:
        gauss_elimination_test(matrix, max_element_length)
    elif choice == 2:
        inverse_matrix_test(matrix, max_element_length)

def main():
    max_value = 5000
    matrix = matrix_input(max_value)
    # general_test(max_value)
    info = matrix_everything(matrix)
    #with open("results.json", "w") as f:
    #    json.dump(info, f, cls=FractionEncoder)
    print(info) # write to file with shell (python3 test.py > output.txt)

main()