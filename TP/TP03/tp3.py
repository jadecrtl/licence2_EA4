#!/usr/bin/env python3

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


############################################################
# Exercice 1.1
#
# Tri selection
#

def triSelection(T):
    # À COMPLETER
    return T

############################################################
# Exercice 1.2
#
# randomPerm prend en paramètre un entier n et renvoie une
# permutation aléatoire de longueur n dont l'algorithme s'appuie
# sur le tri sélection
#

def randomPerm(n):
    T = [i+1 for i in range(n)]
    # À COMPLETER
    return T

############################################################
# Exercice 1.3
#
# testeQueLaFonctionTrie prend en paramètre une fonction de
# tri f et l’applique sur des permutations aléatoires de
# taille i variant de 2 à 100 et vérifie que le résultat est
# un tableau trié
#

def testeQueLaFonctionTrie(f):
    # À COMPLETER
    return False

############################################################
# Exercice 1.4
#
# randomTab prend des entiers n, a et b et renvoie un tableau
# aléatoire de taille n contenant des entiers compris entre
# les bornes a et b.
#

def randomTab(n,a,b):
    T = [0]*n
    # À COMPLETER
    return T

############################################################
# Exercice 1.5
#
# derangeUnPeu prend des enntiers n, k et un booleen rev et
# effectue k échanges entre des positions aléatoires sur la
# liste des entiers de 1 à n si rev vaut False ou sur la
# liste des entiers n à 1 si rev vaut True.
#

def derangeUnPeu(n,k,rev):
    T = [ n - i for i in range(n) ] if rev else [ i + 1 for i in range(n) ]
    # À COMPLETER
    return T


############################################################
# Exercice 2.1
#
# Trois variantes du tri par insertion L échanges successifs,
# insertion directe à la bonne position, et avec recherche
# dichotomique de la positio
#

def triInsertionEchange(T):
    # À COMPLETER
    return T

def triInsertionRotation(T):
    # À COMPLETER
    return T

def triInsertionRapide(T):
    # À COMPLETER
    return T

############################################################
# Exercice 2.2
#
# Tri fusion
#

def fusion(T1,T2):
    # À COMPLETER
    return T1 + T2

def triFusion(T, deb=0, fin=None) :
    # À COMPLETER
    return T

############################################################
# Exercice 2.3
#
# Tri à bulles
#

def triBulles(T) :
    # À COMPLETER
    return T

############################################################
# Exercice 3.1
#
# Trie par insertion le sous-tableau T[debut::gap] de T
#

def triInsertionPartiel(T, gap, debut) :
    # À COMPLETER
    return None

############################################################
# Exercice 3.2
#
# Tri Shell
#

def triShell(T) :
    # À COMPLETER
    return T

##############################################################
#
# Mesure du temps
#

def mesure(algo, T) :
    debut = clock()
    algo(T)
    return clock() - debut

def mesureMoyenne(algo, tableaux) :
  return sum([ mesure(algo, t[:]) for t in tableaux ]) / len(tableaux)

couleurs = ['b', 'g', 'r', 'm', 'c', 'k', 'y', '#ff7f00', '.5', '#00ff7f', '#7f00ff', '#ff007f', '#7fff00', '#007fff' ]
marqueurs = ['o', '^', 's', '*', '+', 'd', 'x', '<', 'h', '>', '1', 'p', '2', 'H', '3', 'D', '4', 'v' ]

def courbes(algos, tableaux, styleLigne='-') :
  x = [ t[0] for t in tableaux ]
  for i, algo in enumerate(algos) :
    print('Mesures en cours pour %s...' % algo.__name__)
    y = [ mesureMoyenne(algo, t[1]) for t in tableaux ]
    plt.plot(x, y, color=couleurs[i%len(couleurs)], marker=marqueurs[i%len(marqueurs)], linestyle=styleLigne, label=algo.__name__)

def affiche(titre) :
  plt.xlabel('taille du tableau')
  plt.ylabel('temps d\'execution')
  plt.legend(loc='upper left')
  plt.title(titre)
  plt.show()

def compareAlgos (algos, taille=1000, pas=100, ech=5) :
  # taille = 1000 : taille maximale des tableaux à trier
  # pas = 100 : pas entre les tailles des tableaux à trier
  # ech = 5 : taille de l'échantillon pris pour faire la moyenne
  for tri in algos :
      if testeQueLaFonctionTrie(tri):
          print(tri.__name__ + ": OK")
      else:
          print(tri.__name__ + ": échoue")
  print()
  print("Comparaison à l'aide de randomPerm")
  tableaux = [[i, [randomPerm(i) for j in range(ech)]] for i in range(2, taille, pas)]
  courbes(algos, tableaux, styleLigne='-')
  affiche("Comparaison à l'aide de randomPerm")
  print()
  
  print("Comparaison à l'aide de randomTab")
  tableaux = [[i, [randomTab(i,0,1000000) for j in range(ech)]] for i in range(2, taille, pas)]
  courbes(algos, tableaux, styleLigne='-')
  affiche("Comparaison à l'aide de randomTab")
  print()

  print("Comparaison à l'aide de derangeUnPeu (rev = True)")
  tableaux = [[i, [derangeUnPeu(i,10,True) for j in range(ech)]] for i in range(2, taille, pas)]
  courbes(algos, tableaux, styleLigne='-')
  affiche("Comparaison à l'aide de derangeUnPeu (rev = True)")
  print()

  print("Comparaison à l'aide de derangeUnPeu (rev = False)")
  tableaux = [[i, [derangeUnPeu(i,10,False) for j in range(ech)]] for i in range(2, taille, pas)]
  courbes(algos, tableaux, styleLigne='-')
  affiche("Comparaison à l'aide de derangeUnPeu (rev = False)")
  print()

def compareAlgosSurTableauxTries (algos, taille=20000, pas=1000, ech=10) :
  print("Comparaison à l'aide de derangeUnPeu (rev = False)")
  tableaux = [[i, [derangeUnPeu(i,10,False) for j in range(ech)]] for i in range(2, taille, pas)]
  courbes(algos, tableaux, styleLigne='-')
  affiche("Comparaison à l'aide de derangeUnPeu (rev = False)")
  
##############################################################
#
# Main
#

if __name__ == '__main__':
  trisInsertion = [ triInsertionEchange, triInsertionRotation, triInsertionRapide ]
  trisLents = [ triSelection, triBulles ]

  sys.setrecursionlimit(4000)

  #exercice1
  
  # print("Exercice 1")
  # algos = [triSelection]
  # compareAlgos(algos)
  
  #exercice2
  
  # print("Exercice 2")
  # algos += trisInsertion + [triFusion, triBulles]
  # compareAlgos(algos)

  ###################################################################
  ##### Commentez ici les résultats obtenus pour les différents #####
  ##### algorithmes sur les différents types de tableaux ############
  ###################################################################
  # commentaires...
  ###################################################################
  
  #exercice3
  
  # print("Exercice 3")
  # algos = [triShell]
  # compareAlgos(algos)


  #compare tous les algos

  # print("Comparaisons de tous les algos")
  # algos = trisInsertion + trisLents + [ triFusion, triShell ]
  # compareAlgos(algos, taille=2000, pas=200)

  ###################################################################
  ##### Commentez ici les résultats obtenus pour les différents #####
  ##### algorithmes sur les différents types de tableaux ############
  ###################################################################
  # commentaires...
  ###################################################################
  
  #compare les tris fusions et Shell

  # print("Comparaisons des tris fusion et Shell")
  # algos = [ triFusion, triShell ]
  # compareAlgos(algos, taille=10000, pas=500)

  ###################################################################
  ##### Commentez ici les résultats obtenus pour les différents #####
  ##### algorithmes sur les différents types de tableaux ############
  ###################################################################
  # commentaires...
  ###################################################################
  
  # comparaison sur tableaux presque triés
  
  # print("\nComparaisons sur tableaux presque triés")
  # algos = trisInsertion + [ triFusion, triShell ]
  # compareAlgosSurTableauxTries (algos)

  ###################################################################
  ##### Commentez ici les résultats obtenus pour les différents #####
  ##### algorithmes sur les différents types de tableaux ############
  ###################################################################
  # commentaires...
  ###################################################################
