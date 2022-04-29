#!/usr/local/bin/python3

from os import system

# *******************************
# ** Quelques fonctions utiles **
# *******************************

class ArbreBinaire:
    def __init__(self, v=None, ls=None, rs=None):
        if (v != None or ls != None or rs != None) and (v == None or ls == None or rs == None):
            raise ValueError('A tree without value must be empty.')
        self.value = v
        self.left_son = ls
        self.right_son = rs

    def __str__(self) :
        return '-' if self.value == None \
             else  '(%d,%s,%s)' % (self.value, self.left_son, self.right_son)

    def __eq__(self, other) :
        if type(other) != ArbreBinaire : return False
        return self.value == other.value and \
               self.left_son == other.left_son and \
               self.right_son == other.right_son

    def __ne__(self, other) :
        return not(self == other)


# *******************************
# ** Opérateurs de construction
# *******************************

Vide = ArbreBinaire()

def Noeud(valeur,abr_gauche,abr_droit):
    if valeur == None or abr_gauche == None or abr_droit == None :
        raise ValueError('No argument given to Noeud should be None.')
    if type(valeur) != type(0):
        raise ValueError('The first argument of function Noeud should be an integer.')
    if type(abr_gauche) != type(Vide) :
        raise ValueError('The second argument of function Noeud should be a binary tree.')
    if type(abr_droit) != type(Vide) :
        raise ValueError('The third argument of function Noeud should be a binary tree.')

    return ArbreBinaire(valeur, abr_gauche, abr_droit)

def Feuille(valeur) :
    if valeur == None :
        raise ValueError('The argument given to the function Feuille should not be None.')
    return Noeud(valeur, Vide, Vide)

# *******************************
# ** Accesseurs
# *******************************

def estVide(arbre):
    if arbre == None :
        raise ValueError('The argument given to the function estVide should not be None.')
    return arbre == Vide

def etiquetteRacine(arbre):
    if arbre == None :
        raise ValueError('The argument given to the function etiquetteRacine should not be None.')
    if estVide(arbre) :
        raise ValueError('The argument given to the function etiquetteRacine should not be the empty tree.')
    return arbre.value

def filsGauche(arbre):
    if arbre == None :
        raise ValueError('The argument given to the function filsGauche should not be None.')
    if estVide(arbre) :
        raise ValueError('The argument given to the function filsGauche should not be the empty tree.')
    return arbre.left_son

def filsDroit(arbre):
    if arbre == None :
        raise ValueError('The argument given to the function filsDroit should not be None.')
    if estVide(arbre) :
        raise ValueError('The argument given to the function filsDroit should not be the empty tree.')
    return arbre.right_son

##########################################################################

##########################################################################

def createArbreFromTable(T,root) :
    if root == None : return Vide

    etiquette, fg, fd, pere = T[root]
    arb_g = createArbreFromTable(T,fg)
    arb_d = createArbreFromTable(T,fd)

    if etiquette == None :
        if arb_g != Vide or arb_d != Vide :
            raise ValueError('An empty label should correspond to an empty tree.')

        return Vide
    else:
        return Noeud(etiquette,arb_g,arb_d)

def arbreBinaireDeFichier(fichier) :
    ''' lit un fichier contenant la description d'un arbre avec une ligne
    par noeud, au format : num,etiquette,fg,fd
    et construit un tableau contenant en case d'indice num la liste
    [etiquette, fg, fd, pere]
    On suppose que les num sont en ordre croissant incremente de 1 a chaque ligne'''
    try:
        res = []
        with open(fichier) as f:
            for ligne in f :
                noeud = [None, None, None, None]
                num, etiquette, fg, fd = ligne.strip().split(',')
                if etiquette != '' : noeud[0] = int(etiquette)
                if fg : noeud[1] = int(fg)
                if fd : noeud[2] = int(fd)
                res.append(noeud)
    except IOError:
        print("Erreur d'ouverture du fichier <%s>" % fichier)
        return
    except ValueError:
        print("L'etiquette ou les indices doivent etre des entiers.")

    # ajout des peres
    for i, noeud in enumerate(res) :
        etiquette, fg, fd, pere = noeud
        for fils in (fg, fd) :
            if fils != None :
                if res[fils][-1] == None :
                    res[fils][-1] = i
                else :
                    print("Erreur dans le fichier <%s> : Un noeud a plusieurs pere." % fichier)
                    return

    # calcul de(s) élément(s) sans pere (normalement un seul : la racine)
    racines = []
    for i, noeud in enumerate(res) :
        if (noeud[-1] == None):
            racines.append(i)

    # erreur si trop ou pas assez de racines
    if len(racines) != 1:
        print('Mauvais nombre de racines (%d) : ' % len(racines) + str(racines))
        return

    return createArbreFromTable(res,racines[0])


##########################################################################

##########################################################################

def arbreBinaireVersFichierAux(arbre,f,i) :
    if estVide(arbre) :
        f.write(str(i) + ',,,\n')
        return i + 1
    else :
        ig = arbreBinaireVersFichierAux(filsGauche(arbre),f,i)
        id = arbreBinaireVersFichierAux(filsDroit(arbre),f, ig)
        f.write(str(id) + ',' + str(etiquetteRacine(arbre)) + ',' + str(ig-1) + ',' + str(id-1) + '\n')
        return id+1

def arbreBinaireVersFichier(arbre, fichier) :
    ''' réciproque de la précédente '''
    try :
        with open(fichier, 'w') as f:
            arbreBinaireVersFichierAux(arbre,f,0)
    except IOError:
        print("Erreur d'ouverture du fichier <%s>" % fichier)


##########################################################################

##########################################################################

def dessineArbreBinaireAux(arbre,fic,i) :
    if estVide(arbre) :
        fic.write("\t" + str(i) + '[shape="plaintext", label=""];\n')
        return i + 1
    else :
        ig = dessineArbreBinaireAux(filsGauche(arbre),fic,i)
        id = dessineArbreBinaireAux(filsDroit(arbre),fic, ig)
        fic.write("\t" + str(id) +"[label=" + str(etiquetteRacine(arbre)) + "];\n")
        fic.write("\t" + str(id) + " -- " + str(ig-1) + ";\n")
        fic.write("\t" + str(id) + " -- " + str(id-1) + ";\n")
        return id+1

def dessineArbreBinaire(arbre,fname = 'arbre') :
    ''' crée un fichier fname.dot et un fichier fname.pdf
    représentant l'arbre '''

    # creation du fichier .dot
    fic = open(fname+".dot", 'w')
    fic.write("graph arbre {\n")

    dessineArbreBinaireAux(arbre,fic,0)

    fic.write("}\n")
    fic.close()

    # transformation en .pdf
    system("dot -Tpdf -o " + fname + ".pdf " + fname + ".dot")

##########################################################################

##########################################################################

arbre3ABR1 = Noeud(2,Feuille(1),Feuille(3))
arbre3ABR2 = Noeud(1,Vide,Noeud(2,Vide,Feuille(3)))
arbre3ABR3 = Noeud(3,Noeud(2,Feuille(1),Vide),Vide)

arbre10ABR1 = arbreBinaireDeFichier("tests/abr10_1.txt")
arbre10ABR2 = arbreBinaireDeFichier("tests/abr10_2.txt")

arbre100ABR1 = arbreBinaireDeFichier("tests/abr100_1.txt")
arbre100ABR2 = arbreBinaireDeFichier("tests/abr100_2.txt")

arbre100notABR = arbreBinaireDeFichier("tests/notAbr100.txt")

##########################################################################

##########################################################################
if __name__ == '__main__':
  pass
