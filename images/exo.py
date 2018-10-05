# name, age = "theo", 38
# sentence = "Je suis {} et j ai {} ans".format(name, age)
#
# bubu = 5
# # print(bubu * 4)
#
# bubu /= 2
#
# a = 2
# b = 3
# a, b = b, a
#
# # 10 - Déclarer 2 variables prenant la meme valeur de 3 manières différentes au moins.
# c = d  = 7
# c,d = 8, 8
# c = 9
# d = 9

# 11 - Déclarer 1 variable "a" et lui affecter la valeur "10". Réaliser la suite dans l'ordre :
#
#     Afficher "a"
#     Afficher le résultat de la division de a par 2
#     Afficher le résultat entier de la division de a par 2
#     Afficher le reste de la division de a par 2
#     Afficher a puissance 3

# a = 10
# print(a, a / 2, a // 2, a % 2, a ** 3)

# 12 - Ecrire un programme qui lit le prix HT d’un article, le nombre d’articles et qui définit une variable contenant
# le taux de TVA à 20%, et qui fournit le prix total TTC correspondant.
# Se servir de la fonction "input()" pour demander a l'utilisateur de renseigner les informations.

# price = float(input("Quel est le prix de votre article ? "))
# qty = int(input("Combien d'articles souhaitez-vous acheter ?"))
# TVA = float(1.2)
# total = price * qty * TVA
# print(("Ces {} articles vous couteront : {} € TTC").format(qty, total))

# my_list = ["pouet", "bulle", 4, 5]
# print(my_list[0])
# print(type(my_list[2]))

# x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(x[3])
# print(x[2:8:2])
# print(len(x), min(x), max(x), sum(x))
# del x[3:5]
# print(x)

# x = ["ok", 4, 2, 78, "bonjour"]
# print(x[3])
# x[1] = "toto"
# print(x)

# my_list = [i for i in range(1, 6)]
# print(my_list)
# my_list2 = [1, 2, 3, 4, 5]
# print(my_list2)

# my_dict = {"key": "valeur", "key2": "valeur2"}
# print(my_dict)
# print(my_dict["key"])
# my_dict["titi"] = "toto"
# print(my_dict)
# my_dict["titi"] = "tata"
# print(my_dict)
# del my_dict["titi"]
# print(my_dict)
# print(my_dict.pop("key"))
# print(my_dict)
# y = my_dict.copy()
# print(y)

# my_list = [("a", "b"), ("c", "d"), ("e", "f"), ("g", "h")]
# # print(my_list)
# my_list.append("a")
# # print(my_list)
# my_list.extend(["b"])
# # print(my_list)
# my_list += ["c"]
# # print(my_list)
# y = ["1", "2", "3"]
# my_list = my_list + y
# # print(my_list)
# my_list.insert(4, "2")
# # print(my_list)
# my_list.remove("2")
# # print(my_list)
# print(y)
# z = y.copy()
# print((z))
# y[:] = []
# print(y)
# del z[:]
# print(z)

# nb1 = float(input("Saississez un premier nombre : "))
# nb2 = float(input("Saississez un deuxieme nombre : "))
# if nb1 * nb2 == 0:
#     print("Le produit de vos 2 nombres est nul")
# elif nb1 * nb2 > 0:
#     print("Le produit de vos 2 nombres est positif")
# else:
#     print("Le produit de vos 2 nombres est négatif")

# age = float(input("Quel est votre age ?"))
# if age >= 18:
#     print("Vous êtes majeur")
# else:
#     print("Vous êtes mineur")

# nb = int(input("Saississez un nombre : "))
# if nb in range(5, 10):
#     print("Vrai")
# else:
#     print("Faux")

                # nb = int(input("Saississez un nombre : "))
                # if nb in [5, 6, 7]:    COMMENT METTRE PLUSIEURS VALEURS DANS LE OU ?
                #     print("Vrai")
                # else:
                #     print("Faux")

# for i in range(6):
#     print(i)

# my_list = ["tarte", "saumon", "caracala", "zirgouflexpicpic"]
# for index in range(len(my_list)):
#     print(len(my_list[index]))

                # x = "anticonstitutionnellement"
                # for letter in range(len(x)):
                #     print(x[letter])          UNE STRING SE COMPORTE COMME UNE LISTE ?

# x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for list in x:
#     for index in range(len(list)):
#         print(list[index])

# 5 - Soit la liste suivante : x = [1,10,20,30,40,50]. Définissez a et b, 2 variables prenant chacune la sommu des
# nombres de la liste x. Les 2 sommes doivent être calculées différemment. Afficher a et b
# x = [1,10,20,30,40,50]
# a = sum(x)
# print(a)
# b = 0
# for index in range(len(x)):
#     b = b + x[index]
# print(b)

# my_list = []
# for nb in (range(0, 6)):
#     my_list.append(nb)
# print(sorted(my_list, reverse=True))

# 7 - Grâce à la fonction range(1, 10), afficher tous les nombres de 1 à 3. La boucle doit s'arrêter une fois
# que le chiffre 3 est affiché
# for nb in range(1, 10):
#     if nb <= 3:
#         print(nb)
      elif nb > 3:
          break

# 8 - Refaire le même exercice que le précédent, mais cette fois variabiliser tous les nombres. PAS COMPRIS


c = 3
a = 1
b = 10
for nb in range(a, b):
     
     if nb <= c:
        print(nb)
      elif nb > c:
        break

# for nb in range(1, 10):
#     if nb == 3:
#         pass
#     else:
#         print(nb)

# ordi = ["apple", "asus", "dell", "samsung"]
# index = 0
# while index <= len(ordi) - 1:
#     print(ordi[index])
#     index += 1

# saisie = input("Tapez n'importe quoi ou bien 'EXIT' pour sortir :")
# while saisie != "exit":
#     saisie = input("Tapez n'importe quoi ou bien 'EXIT' pour sortir ")

# nb = 0                            EST CE QU ON POURRAIT PAS FAIRE UN TRUC AVEC range(0, 100, 5) ?
# while nb <= 100:
#     print(nb)
#     nb += 5

# def multiplication(nb):         
#     print(nb * 5)
#
# multiplication(8)

# def parity(my_list):
#     
#     for i in my_list:
#         if i % 2 != 0:
#             my_list.remove(i)
#     			                   PEUT-ON FAIRE AUTREMENT ?
#     return my_list
#
# my_list = [0, 5, 8, 9, 45, 183, 4545, 44, 218, 48]
#
# parity(my_list)

# def fibo(max):                                        J'Y ARRIVE PAS ! SI MAX = 100 SUITE FIBO = 011 ET NON PAS 112
#     a,b = 0,1
#         while int(result) >= max:
#         result = str(result) + str(b)
#         c = a + b
#         a = b
#         b = c
#     print(result)
#     print(int(result))
# nb = int(input("Jusqu'où voulez-vous écrire la suite de Fibonacci ? "))
#
#
# fibo(nb)

# def count(word):
#     vowels = ["a", "e", "i", "o", "u", "y"]
#     nb_vowels = 0
#     for letter in word:
#         if letter in vowels:
#             nb_vowels += 1
#     print(nb_vowels)
#
#
# count(input("Tapez un mot pour rechercher le nombre de voyelles qu'il contient : "))


# def count(word):
#     vowels = ["a", "e", "i", "o", "u", "y"]
#     nb_vowels = 0
#     i = 0
#     while i < len(word):
#         if word[i] in vowels:
#             nb_vowels += 1
#         i += 1
#     print(nb_vowels)
#
#
# count(input("Tapez un mot pour rechercher le nombre de voyelles qu'il contient : "))

# En faire une troisième avec une string dans le "in" de la condition

# def count(word):
#     nb_vowels = 0
#     i = 0
#     while i < len(word):
#         if word[i] in "aeiouy":
#             nb_vowels += 1
#         i += 1
#     print(nb_vowels)
#
#
# count(input("Tapez un mot pour rechercher le nombre de voyelles qu'il contient : "))

# def facto(n):
#     if n == 1:
#         print(1)
#     else:
#         result = n
#         i = 1
#         while n >= 2:
#             result = result * (n-1)
#             n -= 1
#         print(result)
# facto(6)

# def facto(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * facto(n-1)
#
#
# print(facto(10))


# def funk(*args):
#     print(len(args))
#     print(sum(args))
#
# funk(1, 2, 3, 4, )

# def first_number(my_list):
#     list_first = []
#     for nb in range(len(my_list)):
#         list_first.append(str(my_list[nb])[0])      #PLUS ELEGANT ?
#     print(list_first)
#     return (list_first)
#
#
#
# def count(liste):
#     result = {}
#     for key in range(1,10):             # MERCI KEVIN. CT LA QUE CA MERDAIT
#         result[key] = 0
#     for item in (first_number(liste)):
#         temp = int(item)
#         result[temp] += 1                # YES!!!!
#     print(result)
#
#
# serie = [1, 4 ,9 ,16 ,25 ,36 ,49 ,64 ,100 ,121]
#
# count(serie)

class Carre(cote):
    
