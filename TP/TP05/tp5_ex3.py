#!/usr/bin/env python3

#importe indirectement tp5, ea4lib et tp5_ex* pour * < 2
from tp5_ex2 import *

#
# À COMPLÉTER !
#
def supprimerPlusPetit(arbre) :
    ''' Supprimer le plus petit élément de arbre. Renvoie la paire (elt,new_arbre)
    où elt est le plus petit élement de arbre et new_arbre est le nouvel arbre.
    Renvoie None et Vide quand arbre est vide.'''
    return None, Vide

#
# À COMPLÉTER !
#
def supprimerPlusGrand(arbre) :
    ''' Supprimer le plus grand élément de arbre. Renvoie la paire (elt,new_arbre)
    où elt est le plus grand élement de arbre et new_arbre est le nouvel arbre.
    Renvoie None et Vide quand arbre est vide.'''
    return None, Vide

#
# À COMPLÉTER !
#
def suppressionABR(arbre, elt, alea=False) :
    ''' supprime le noeud d'étiquette elt dans l'arbre; en version
    déterministe, remplacement par le prédécesseur; sinon, à pile ou face
    renvoie None si elt n'est pas dans arbre, sinon renvoie le nouvel arbre'''
    return None

#####################################################################
##  TESTS
#####################################################################

def testSuppression():
  arbres = [arbre3ABR1, arbre3ABR1, arbre10ABR2, arbre10ABR2, arbre100ABR1, arbre100ABR1, arbre100ABR1, arbre100ABR1]
  elements = [1, 4, 3, 7, 55, 1, 49, 43]
  score = 0
  print('Test Suppression')
  for i in range(len(arbres)):
    print (' - test %d/%d: ' % (i + 1, len(arbres)), end='')
    elt = elements[i]
    a = suppressionABR(arbres[i],elt)
    if a == None : a = arbres[i]
    res = arbreBinaireDeFichier('tests/testSuppression_%d.txt' % i)
    if a == res :
      printcol(" {ok}", "green")
      score += 1
      #dessineArbreBinaire(a,'obtenu_'+str(i))
    else:
        printcol(" {echec}", "red", end='')
        #print(": obtenu ", a, end='')
        #print(" <> attendu ", res[i])
        dessineArbreBinaire(a,'obtenu_'+str(i))
        dessineArbreBinaire(res, 'attendu_'+str(i))

  printcol ('  score {%d/%d} ' % (score, len(arbres)), "cyan")

if __name__ == '__main__':
    testSuppression()
