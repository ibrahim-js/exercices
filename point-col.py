tableau = []

M = int(input("Saisir le nombre des lignes: "))
N = int(input("Saisir le nombre des colonnes: "))

for i in range(M):
    ligne = []
    for j in range(N):
        ligne.append(int(input("Saisir un nombre: ")))
    tableau.append(ligne)

for i in range(M):
    for j in range(N):
        # On compare chaque valeur du tableau si elle est le:
        # Max de sa ligne et Min de sa colonne...
        max = True
        min = True
        # Si la valeur est max de sa ligne
        for c in range(N):
            if tableau[i][j] < tableau[i][c]:
                max = False
        # Si la valeur est min de sa colonne
        for c in range(M):
            if tableau[i][j] > tableau[c][j]:
                min = False
        # Si la valeur est max et min en même temp, donc point col
        if max and min:
            print("Point col:", tableau[i][j], ". Max de la ligne", i + 1, ". Min de la colonne", j + 1)

        # On compare chaque valeur du tableau si elle est le:
        # Min de sa ligne et Max de sa colonne...
        max = True
        min = True
        # Si la valeur est min de sa ligne
        for c in range(N):
            if tableau[i][j] > tableau[i][c]:
                min = False
        # Si la valeur est max de sa colonne
        for c in range(M):
            if tableau[i][j] < tableau[c][j]:
                max = False
        # Si la valeur est min et max en même temp, donc point col
        if max and min:
            print("Point col:", tableau[i][j], ". Min de la ligne", i + 1, ". Max de la colonne", j + 1)