# Ex 1
# def calc_nombre(nombre):        # Fonction calcul d'un nombre * 5
#     print("Votre nombre multiplié par 5 :\n", nombre * 5)       # Afficher le calcul

# calc_nombre(int(input("Saisissez un nombre :\n")))      # Appeler la fonction avec le nombre à multiplier

# Ex 2
# def nombre_pairs(liste):        # Fonction trouver les nombres pairs
#     for i in range(len(liste)):     # Boucle jusqu'à atteindre la dernière valeur de la liste
#         if liste[i] % 2 == 0:       # Modulo 2 des nombres de ma liste
#             print(liste[i])     # Afficher les nombres pairs

# liste = [1, 4, 8, 12, 23, 27, 30]       # Liste de nombres
# nombre_pairs(liste)     # Appeler la fonction avec la liste


# def nombre_pairs(liste):
#     pairs = []      # Liste pour contenir les nombres pairs
#     for i in range(len(liste)):
#         if liste[i] % 2 == 0:
#             pairs.append(liste[i])      # Ajout des valeurs pairs dans la liste
#     return pairs        # Renvoie la liste pairs

# liste = [1, 4, 8, 12, 23, 27, 30]
# print(nombre_pairs(liste))      # Afficher le résultat de la fonction


# def nombre_pairs(liste):
#     pairs = []
#     print("Saisissez un nombre :")
#     for i in range(lim):
#         liste.append(int(input("")))
#     print("Les nombres pairs sont :")
#     for i in range(lim):
#         if liste[i] % 2 == 0:
#             pairs.append(liste[i])
#     return pairs

# lim = int(input("Saisissez une limite de nombres :\n"))     # Nombre maximum de valeurs
# liste = []
# print(nombre_pairs(liste))

# Ex 3
# def fibonacci(n):       # Fonction suite Fibonacci
#     print("La suite Fibonacci est :")
#     f = [0, 1]      # Les deux premiers termes de la suite
#     for i in range(2, n+1):     # Boucle du 3e termes à l'infini
#         fn = f[i-1] + f[i-2]        # Calcul de la suite
#         f.append(fn)        # Ajout des valeurs de fn dans f
#     return f        # Renvoie f

# n = 5       # Limite de la suite
# print(fibonacci(n))     # Afficher le résultat de la fonction

# Ex 4
# def fonction_for(mot):      # Fonction nombre de voyelles avec for
#     nb_voyelle = 0
#     voyelle = ["a", "e", "i", "o", "u", "y"]        # Liste des voyelles
#     for i in range(len(mot)):       # Boucle jusqu'à la fin du mot
#         for j in range(len(voyelle)):       # Boucle jusqu'à la dernière voyelle
#             if mot[i] == voyelle[j]:        # Condition si lettre = voyelle
#                 nb_voyelle = nb_voyelle + 1     # voyelle = +1 sinon suivant
#     return nb_voyelle       # Renvoie le nombre de voyelles

# mot = "abeille"     # Le mot
# print(fonction_for(mot))        # Afficher le résultat de la fonction


# def fonction_while(mot):        # Fonction nombre de voyelles avec while
#     nb_voyelle = 0
#     i = 0
#     voyelle = ["a", "e", "i", "o", "u", "y"]
#     while i != len(mot):        # Boucle tant que i différent de la taille du mot
#         j = 0
#         while j != len(voyelle):        # Boucle tant que j différent de la taille du mot
#             if mot[i] == voyelle[j]:
#                 nb_voyelle = nb_voyelle + 1
#                 j = j + 1       # Passage à la voyelle suivante
#             else:
#                 j = j + 1
#         i = i + 1       # Passage à la lettre suivante
#     return nb_voyelle     # Renvoie le nombre de voyelles

# mot = "ruche"
# print(fonction_while(mot))        # Afficher le résultat de la fonction


# def fonction_voyelle(mot):      # Fonction nombre de voyelles compacte
#     nb_voyelle = 0
#     voyelle = ["a", "e", "i", "o", "u", "y"]
#     for i in range(len(mot)):
#         if mot[i] in voyelle:       # Condition si lettre = voyelle
#             nb_voyelle = nb_voyelle + 1     # voyelle = +1 sinon suivant
#     return nb_voyelle       # Renvoie le nombre de voyelles

# mot = "miel"
# print(fonction_voyelle(mot))        # Afficher le résultat de la fonction

# Ex 5
# def factorielle(nombre):        # Fonction factorielle d'un nombre
#     resultat = 1
#     for i in range(1, nombre+1):        # Boucle factorielle
#         resultat = resultat*i       # Calcul factorielle
#     return resultat     # Renvoie le resultat

# nombre = 5      # Nombre pour la fonction
# print(factorielle(nombre))      # Afficher le résultat de la fonction

# Ex 6
# def factorielle(nombre):
#     if nombre < 2:
#         return 1
#     else:
#         return nombre * factorielle(nombre-1)

# nombre = 5
# print(factorielle(nombre))

# Ex 7
# def fonction(*n):       # Fonction avec arguments variables
#     print("Les valeurs sont :", *n)
#     somme = 0
#     nb_argument = 0
#     for i in n:     # Boucle calcul valeurs variables
#         somme = somme + i       # Calcul somme des valeurs
#         nb_argument = nb_argument + 1       # Calcul somme des arguments
#     print("La somme des valeurs est", end=" ")
#     return str(somme) + " avec " + str(nb_argument) + " arguments."     # Renvoie la somme et le nombre d'arguments

# print(fonction(1, 2, 5, 28))        # Afficher le résultat de la fonction

# Ex 8
# def maFonction(liste):
#     chiffre = []
#     for i in liste:
#         if i <= 9:
#             chiffre.append(i)
#         else:
#             i = str(i)
#             chiffre.append(int(i[0]))

#     return chiffre

# def autreFonction(chiffre):
#     resultat = {}
#     for j in range(len(chiffre)):
#         if j != 0:
#             compteur = {str(k): chiffre.count(k)}
#             resultat.update(compteur)

#     return resultat

# liste = [1, 4, 9, 16, 25, 36, 49, 64, 100, 121]

# print(autreFonction(maFonction(liste)))