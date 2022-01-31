#!/usr/bin/env python3


#
# A REMPLIR
#
def crible_eratosthene(n):
# calcule la table de booléens où la i-ème position est True
# si et seulement si i est un nombre premier.
    return [True]*(n+1)

def test_crible(n):
    c=crible_eratosthene(n)
    for i in range(len(c)):
        if c[i]:
           print(i, end= ' ')
    print()


#
# A REMPLIR
#
def somme_impairs(x) :
# calcule la somme des entiers impairs de 1 à x
	return 0

def test_somme(n) :
# teste que la somme des entiers impairs de 1 à x =
#    (x/2)*(x/2) si x est pair
#    (x+1)/2*(x+1)/2 sinon
# pour tout 1 <= x <= n
	return True


# AJOUTER D'AUTRES TESTS
#  [valeur_x, resultat_attendu]
def testDataSomme() :
    """retourne un jeu de tests"""
    return [[0, 0], [3, 4], [24, 144], [-3, 0]]


#
# NE PAS MODIFIER
#
def testOp(op, data) :
	print('\n\n* Test function %s:' % op.__name__)
	score = 0
	ldata = len(data)
	for i, dt in enumerate(data) :
		print('** test %d/%d : ' % (i + 1, ldata), end='')
		x = dt[0]
		refr = dt[1]
		r = op(x)
		if r == refr :
			score+=1
			print('ok')
		else :
			print('ECHEC')
			print('    entree  : %s' % x)
			print('    calcule : %s' % r)
			print('    attendu : %s' % refr)
	print('** Score %d/%d' % (score, ldata))


if __name__ == '__main__':
        test_crible(50)
        testOp(somme_impairs, testDataSomme())
