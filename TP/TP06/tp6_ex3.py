#!/usr/bin/env python3

import tp6_ex1_ex2

def mot_to_int(mot) :
    #A COMPLETER
    return

def creer_dico(lg=0) :
    #A COMPLETER
    return

def ajouter_mot(dico, mot) :
    #A COMPLETER
    return dico

def retirer_mot(dico, mot) :
    #A COMPLETER
    return dico

def dans_dico(dico, mot):
    #A COMPLETER
    return dico

##############################################################
#
# crée un générateur des mots contenus dans le roman de Marcel Proust
#
def proust() :
    with open("proust.txt", encoding="utf-8") as f :
        for ligne in f :
            for mot in ligne.split() :
                tmp = mot.strip('-,.?!;:"«»()^').lower()
                if tmp != '' : yield tmp


##############################################################
#
# Main
#

if __name__ == '__main__':
    
    #complétez avec vos tests...
    S = creer_dico(8)
