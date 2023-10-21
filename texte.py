chaine = []

lettres = 0
ponctuations = 0
voyelles = 0
mots = 0
espaces = 0
phrases = 0

# La saisie du texte
print("Saisir un texte caractère par caractère:")
while True:
    caractere = input("> ")
    if len(caractere) > 0:
        if caractere[0] == "%":
            break
        chaine.append(caractere[0])

# ----- Nombre des lettres, voyelles, ponctuations et espaces -----
for c in chaine:
    if c.isalpha():
        lettres += 1
        if c.lower() in ["a", "e", "y", "u", "i", "o"]:
            voyelles += 1
    elif c in [":", ",", "!", "?", ".", ","]:
        ponctuations += 1
    elif c == " ":
        espaces += 1

# ----------------------- Nombre des phrases -----------------------
# Suppression des points et des espaces supplémentaires en cas de manipulation
# Exemple: ".. . . Lorem ipsum dolor sit amet. ... Consectetur adipiscing elit..."
# En fait, cet exemple contient 2 phrases. Mais les points supplémentaires poseront un problème
phrases = list(filter(lambda x: x != " ", chaine)) # Suppression des espaces

while (len(phrases) > 0 and phrases[0] == "."):
    phrases.pop(0)  # Suppression des points au début du texte
while (len(phrases) > 0 and phrases[-1] == "."):
    phrases.pop(-1) # Suppression des points au fin du texte

# Nous avons supprimé les points au début et au fin du texte ainsi que les espaces
# Maintenant nous avons: "Loremipsumdolorsitamet....Consecteturadipiscingelit"
# Nous voulons supprimer les points supplémentaires au milieu du texte et les remplacer par un seul point
i = 0
while len(phrases) > i:
    if phrases[i] == ".": # Lorsqu'on trouve un point,
        while phrases[i + 1] == ".": # Si des points le suivent...
            phrases.pop(i + 1) # Nous les effaçons.
    i += 1
if len(phrases) > 0:
    phrases.append(".") # Nous ajoutons un point à la fin car nous avons effacé tous les points à la fin du texte
# Nous avons: "Loremipsumdolorsitamet.Consecteturadipiscingelit."
# Nous filtrons les points pour en avoir: phrases = [".", "."]
phrases = list(filter(lambda x: x == ".", phrases))
phrases = len(phrases)

# ----------------------- Nombre des mots -----------------------
mots = []
while len(chaine) > 0:
    if chaine[0].isalpha():
        mot = ""
        while chaine[0].isalpha():
            mot += chaine.pop(0)
        mots.append(mot)
    else:
        chaine.pop(0)
mots = len(mots)

# ----------------------- Affichage -----------------------
print("Il y a:")
print(phrases, "phrase(s)")
print(mots, "mot(s)")
print(lettres, "lettre(s)")
print(voyelles, "voyelle(s)")
print(ponctuations, "ponctuation(s)")
print(espaces, "espace(s)")