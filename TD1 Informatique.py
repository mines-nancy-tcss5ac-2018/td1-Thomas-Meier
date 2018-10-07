#TD1 d'Informatique / Thomas MEIER




#Problème 16 : What is the sum of the digits of the number 2**1000?

def solve_16(n):
    somme = 0
    for chiffre in [int(c) for c in str(2**n)]: #transforme le nombre en la liste de ses chiffres
        somme += chiffre
    return somme
    
assert solve_16(15) == 26
print(solve_16(1000))



#Problème 22 : Names scores

def solve_22():
    liste_noms = []
    somme = 0
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    f = open("/Users/ThomasM/Documents/Travail/Mines Nancy/Informatique/TDs/p022_names.txt", "r") #emplacement à modifier en fonction de l'ordinateur
    f_real = f.read().split('","')
    for i in range(len(f_real)):
        liste_noms.append(f_real[i])
    liste_noms[0] = liste_noms[0].split('"')[1] #enlève le guillemet de début du premier nom
    liste_noms[-1] = liste_noms[-1].split('"')[0] #enlève le guillemet de fin du dernier nom
    liste_noms = sorted(liste_noms) #trie alphabétiquement la liste des noms
    for element in liste_noms:
        valeur = 0
        for lettre in element:
            valeur += alphabet.index(lettre) + 1 #calcule la somme des valeurs de chaque lettre du nom
        somme += (liste_noms.index(element) + 1) * valeur #calcule le produit de cette somme avec le placement du nom dans la liste des noms
    return somme
    
print(solve_22())

    
    
#Problème 55 : Nombres de Lychrel en dessous de 10.000

def palindromique(nombre): #permet de savoir si un nombre est 'palindromique' ou non
    compteur = 0
    L = [str(c) for c in str(nombre)] #transforme le nombre en la liste de ses chiffres
    for i in range(len(L)//2):
        if L[i] == L[len(L)-i-1]:
            compteur += 1
    if compteur == len(L)//2: #si tous les nombres symétriquement répartis par rapport au centre du nombre sont égaux, le nombre est 'palindromique'
        return True
    else:
        return False

def solve_55(n):
    compteur = 0 #comptons le nombre de nombre de Lychrel
    for nombre in range(1,n+1): #entre 1 et n compris
        for i in range(50): #si au bout de 50 itérations du processus aucun palindrome n'est trouvé, le nombre est de Lychrel (fonctionne en dessous de 10000)
            L = [str(c) for c in str(nombre)] #transforme le nombre en la liste de ses chiffres
            L.reverse() #inverse le nombre
            lettres = L[0]
            for j in range(1,len(L)): #permet de reconstituer le nombre inversé grâce à la liste de ses chiffres (sous forme str)
                lettres += L[j]
            nombre2 = int(lettres) #permet d'avoir le nombre inversé en tant que nombre (int)
            if palindromique(nombre + nombre2): 
                compteur -= 1
                break #si le nombre est palindromique, on stoppe le processus et on compte 0 (-1+1)
            else:
                nombre = nombre + nombre2 #s'il n'est pas palindromique, le processus continue à partir de la somme des deux nombres
        compteur += 1
    return compteur

assert solve_55(700) == 7
print(solve_55(10000))




#Problème des n-reines

import random

def factorielle(n): #défini la fonction factorielle pour tout entier supérieur ou égal à 0
    if n == 0:
        return 1
    elif n == 1:
        return n
    else:
        return n*factorielle(n-1)

def probleme_reines(n):
    compteur = 0 #compteur d'échiquiers où les reines ne peuvent s'attraper
    liste_echiquier = [] #liste tous les échiquiers où les reines sont placées sur des colonnes différentes
    while len(liste_echiquier) != factorielle(n): #tant que la liste ne contient pas tous les échiquiers possibles
        liste_num = [i for i in range(n)] #liste les colonnes disponibles pour placer des reines
        echiquier = []
        for i in range(n):
            colonne = random.choice(liste_num) #choisit une colonne au hasard
            echiquier.append(colonne) #place la reine de la première ligne sur cette colonne
            liste_num.remove(colonne) #cette colonne n'est plus disponible pour cet échiquier
        if echiquier not in liste_echiquier:
            liste_echiquier.append(echiquier) #si cet échiquier n'était pas déjà dans la liste, on le rajoute
    for echiquier in liste_echiquier:
        compteur2 = -n
        for i in range(n): #prenons les reines de l'échiquier successivement 
            for j in range(n): #comparons cette reine aux autres reines de l'échiquier
                if abs(echiquier[i]-echiquier[j]) == abs(i-j): #si ces deux différences sont égales, alors les reines peuvent s'attaquer en diagonal
                    compteur2 += 1
        if compteur2 == 0 : #si les seules reines qui peuvent s'attaquer entre elles sont les deux-mêmes à chaque fois (n fois), l'échiquier est valide
            compteur += 1
    return compteur
    
assert probleme_reines(4) == 2
'''print(probleme_reines(8))''' #cela prend un peu de temps mais le résultat est bien 92