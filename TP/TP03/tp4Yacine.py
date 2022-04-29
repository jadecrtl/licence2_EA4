#!/usr/bin/env python3

from calendar import leapdays
import sys

version = sys.version_info
if version.major < 3:
    sys.exit(
        "Python2 n'est PLUS supporté depuis le 1er Janvier 2020, merci d'installer Python3"
    )

import random
from time import process_time as clock

try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    sys.exit("Le module matplolib est nécessaire pour ce TP.")



from tp3 import triInsertionEchange, triInsertionRotation, triFusion, triShell, randomPerm, testeQueLaFonctionTrie, randomTab, derangeUnPeu



############################################################
# Exercice 1.1
#
# Tri rapide avec mémoire auxiliaire et en place
#

def triRapide(T) :
    # À COMPLETER
    if len(T) < 2 : return T
    pivot, gauche, droite = partition(T)
    return triRapide(gauche) + [pivot] + triRapide(droite)

def partition(T) :
    pivot = T[0]
    gauche = [ elt for elt in T if elt < pivot ]
    droite = [ elt for elt in T if elt > pivot ]
    return pivot, gauche, droite

def triRapideEnPlace(T, debut=0, fin=None):
    # À COMPLETER
    if fin is None : fin = len(T)
    if fin - debut < 2 : return T
    indice_pivot = partitionEnPlace(T, debut, fin)
    triRapideEnPlace(T, debut, indice_pivot)
    triRapideEnPlace(T, indice_pivot + 1, fin)
    return T

def partitionEnPlace(T, debut, fin) :
    pivot, gauche, droite = T[debut], debut + 1, fin - 1
    while gauche <= droite :
        if T[gauche] < pivot : gauche += 1
        elif T[droite] > pivot : droite -= 1
        else : T[gauche], T[droite] = T[droite], T[gauche]
    T[debut], T[droite] = T[droite], pivot
    return droite

############################################################
# Exercice 1.2
#
# Tri rapide avec mémoire auxiliaire et en place avec pivot
# aléatoire
#

def triRapideAleatoire(T) :
    # À COMPLETER
    if len(T) < 2 : return T
    pivot, gauche, droite = partitionAlea(T)
    return triRapide(gauche) + [pivot] + triRapide(droite)

def partitionAlea(T) :
    alea = random.randint(0,len(T)-1)
    pivot = T[alea]
    gauche = [ elt for elt in T if elt < pivot ]
    droite = [ elt for elt in T if elt > pivot ]
    return pivot, gauche, droite

def triRapideEnPlaceAleatoire(T,debut=0, fin=None):
    # À COMPLETER
    if fin is None : fin = len(T)
    if fin - debut < 2 : return T
    indice_pivot = partitionEnPlaceRandom(T, debut, fin)
    triRapideEnPlaceAleatoire(T, debut, indice_pivot)
    triRapideEnPlaceAleatoire(T, indice_pivot + 1, fin)
    return T

def partitionEnPlaceRandom(T, debut, fin) :
    alea = random.randint(debut, fin - 1)
    T[debut], T[alea] = T[alea], T[debut]
    pivot, gauche, droite = T[debut], debut + 1, fin - 1
    while gauche <= droite :
        if T[gauche] < pivot : gauche += 1
        elif T[droite] > pivot : droite -= 1
        else : T[gauche], T[droite] = T[droite], T[gauche]
    T[debut], T[droite] = T[droite], pivot
    return droite


############################################################
# Exercice 2.1
#
# les tableaux de taille < 15 sont triés par insertion, le
# reste avec l'algo de tri rapide usuel.
#

def triRapideAmeliore(T) :
    # À COMPLETER
    if(len(T) < 15):
        return triInsertionEchange(T)
    else :
        return triRapide(T)

############################################################
# Exercice 2.2
#
# Tri rapide seulement pour les tableaux de taille >= 15 et
# ne fait rien pour les tableaux de taille < 15
#

def triRapideIncomplet(T) :
    # À COMPLETER
    if(len(T) >= 15):
        return triRapide(T)
    return

############################################################
# Exercice 2.3
#
# Trie par insertion le résultat de triRapideIncomplet(T).
#
def triSedgewick(T) :
    # À COMPLETER
    return triInsertionEchange(triRapideIncomplet(T))


############################################################
# Exercice 3.1
#
# Tris drapeau. Attention, les éléments du tableau ne peuvent pas
# avoir d'autres valeurs que 1, 2 ou 3.
#

BLEU, BLANC, ROUGE = 1, 2, 3

def triDrapeau(T) :
    # A compléter
    bleu = []
    blanc = []
    rouge = []
    for i in T :
        if i == BLEU :
            bleu += [i]
        if i == BLANC :
            blanc += [i]
        if i == ROUGE :
            rouge += [i]
    return bleu + blanc + rouge

def triDrapeauEnPlace(T) :
    # A compléter
    i = 0
    while i < len(T)-1 :
        if T[i] > T[i+1] :
            T[i],T[i+1] = T[i+1],T[i]
        i += 1
    return T


############################################################
# Exercice 3.3
#
# Tris rapide, pivot drapeau pour amélioration si le tableau en entrée
# est très répété.
#

def triRapideDrapeau(T) :
    # A compléter
    return T


############################################################
# Exercice 3.3
#
# Effectue un tri drapeau par rapport au pivot.
# Retourne le nombre d'éléments dans chaque catégorie (inférieur au pivot,
# pivot, supérieur au pivot)
#

def partitionDrapeau(T, debut, fin) :  # suppose fin-dev >= 2
    # A compléter
    return 0, 0, 0

############################################################
# Exercice 3.3
#
# Tri rapide en place utilisant un partitionnement drapeau
#

def triRapideDrapeauEnPlace(T, debut=0, fin=None) :
    # A compléter
    return T




from tp3 import mesure, mesureMoyenne, courbes, affiche, compareAlgos


def testTriNonPermutation(tri, maxVal=3):
    for size in range(2,101):
        T = randomTab(size, 1, maxVal)
        T2 = tri(T)
        for i in range(1, len(T2)):
            if T2[i-1] > T2[i]: return False
    return True


def compareAlgosSurTableauxRepetes(algos, taille=20000, pas=1000, ech=15, maxVal=3):
    for tri in algos :
      if testTriNonPermutation(tri):
          print(tri.__name__ + ": OK")
      else:
          print(tri.__name__ + ": échoue")


    print("Comparaison à l'aide de randomTab")
    tableaux = [[i, [randomTab(i,1, 3) for j in range(ech)]] for i in range(2, taille, pas)]
    courbes(algos, tableaux, styleLigne='-')
    affiche("Comparaison à l'aide de randomTab")


##############################################################
#
# Main
#

if __name__ == '__main__':
  trisRapides = [ triRapide, triRapideEnPlace, triRapideAleatoire, triRapideEnPlaceAleatoire ]
  trisHybrides = [ triRapideAmeliore, triSedgewick, triShell ]
  trisDrapeaux = [ triDrapeau, triDrapeauEnPlace ]
  trisRapideDrapeaux = [ triRapideDrapeau, triRapideDrapeauEnPlace ]


  # exercice 1
  #print("Exercice 1")
  #algos = trisRapides
  #compareAlgos(algos)

  # exercice 2

  #print("Exercice 2")
  #algos = [triRapideAmeliore, triSedgewick]
  #compareAlgos(algos)
  #algos = trisRapides + trisHybrides
  #compareAlgos(algos)

  # exercice 3

  print("Exercice 3")
  # comparaison des tris drapeaux
  print("Comparaisons sur tableaux très répétés")
  algos = trisDrapeaux
  compareAlgosSurTableauxRepetes (algos, maxVal=3)

  # comparaison des tris rapide drapeaux
  # print("Comparaisons sur tableaux très répétés")
  # algos = [triRapide, triRapideEnPlace] + trisRapidesDrapeaux
  # compareAlgosSurTableauxRepetes (algos, taille=1000, pas=100, ech=5, maxVal=5)
