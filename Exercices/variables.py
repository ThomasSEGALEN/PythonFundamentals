# Ex 1
# a = 123

# Ex 2
# age = 19
# prenom = "Thomas"
# print("Je suis", prenom, "et j'ai", age, "ans.")

# Ex 3
# age, prenom = 19, "Thomas"
# print("Je suis", prenom, "et j'ai", age, "ans.")

# Ex 4
# b = 4
# print(b * 4

# Ex 5
# c = 7
# print(c + 1)
# d = 7 + 1
# print(d)

# Ex 6
# c = 7
# print(c - 1)
# d = 7 - 1
# print(d)

# Ex 7
# c = 7
# print(c * 2)
# d = 7 * 2
# print(d)

# Ex 8
# c = 7
# print(c / 2)
# d = 7 / 2
# print(d)

# Ex 9
# a = 1
# b = 2
# c = a
# a = b
# b = c
# print(a)
# print(b)

# Ex 10
# a = 3
# b = 3
# print (a, b)
# a, b = 3, 3
# print (a, b)
# a = 3
# b = a
# print (a, b)

# Ex 11
# a = 10
# print(a)
# print(a / 2)
# print(a // 2)
# print(a % 2)
# print(a ** 3)

# Ex 12
# prix_HT = int(input())
# nb_articles = int(input())
# TVA = 0.2
# prix_TTC = prix_HT * nb_articles * TVA
# print(prix_TTC)

# Ex 13
# chiffres = [4, 5]     Liste de deux chiffres
# print(chiffres)

# Ex 14
# liste = ["abeille", 1, "miel", 2]     Liste de deux chiffres et deux chaînes caractères
# print(liste)
# print(liste[0])
# print(type(liste))        Afficher le type de la fonction liste

# Ex 15
# x = [1, 3]
# y = [2, 4]
# z = x + y         Concaténation de x et y
# print(z)

# Ex 16
# x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(x[3])
# print(x[3:5])       Afficher entre 3 et 4
# print(x[2:8:2])     Afficher entre 2 et 7 avec un pas de 2
# print(list(range(2, 8, 2)))     Afficher entre 2 et 7 avec un pas de 2
# print(len(x))       Afficher la taille
# print(min(x))       Afficher la valeur minimum
# print(max(x))       Afficher la valeur maximale
# print(sum(x))       Afficher la somme
# x[3:5] = []         Supprimer les valeurs entre 3 et 4
# del x[3:5]          Supprimer les valeurs entre 3 et 4
# print(x)

# Ex 17
# x = ["ok", 4, 2, 78, "bonjour"]       Liste de chiffres + chaînes de caractères
# print(x[3])       Afficher la 4e valeur
# x[1] = "toto"     Remplacer la 1ere valeur par "toto"
# print(x)

# Ex 18
# liste = [0, 1, 2, 3, 4, 5]    Liste de 0 à 5
# print(liste)
# print(liste[0:6:1])       Liste de 0 à 5

# Ex 19
# x = {"key": "valeur", "key2": "valeur2"}
# print(x)
# print(x["key"])
# x.update({"key": "valeur", "key2": "valeur2", "titi": "toto"})
# print(x)
# x["titi"] = "tata"
# print(x)
# del x["titi"]
# print(x)
# del x["key"]

# y = x
# print(y)

# Ex 20
# tuple1 = (1, 2)
# tuple2 = (3, 4)
# tuple3 = (5, 6)
# tuple4 = (7, 8)
# x = [tuple1, tuple2, tuple3, tuple4]
# print(x)
# z = ["a"]
# x = x + z
# print(x)
# x.append("b")
# print(x)
# y = [1, 2, 3]
# x = x + y
# print(x)
# x[3] = x[3] + (2,)
# print(x)
# x[0] = (2)
# print(x)
# z = y
# print(z)
# del y[0:3]
# print(y)
# y = y[0:0]
# print(y)