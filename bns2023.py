# Sujet 1

def verifie(tab):
    for i in range(1,len(tab)):
        if tab[i] < tab[i-1]:
            return False
    return True

urne = ['A', 'A', 'A','B', 'C', 'B', 'C','B', 'C', 'B']

def depouille(urne):
    resultat = {}
    for bulletin in urne:
        if bulletin in resultat:
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin] = 1
    return resultat

def vainqueur(election):
    vainqueur = ''
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax :
            nmax = election[candidat]
            vainqueur = candidat
    liste_finale = [nom for nom in election if election[nom] == nmax]
    return liste_finale

# Sujet 2

def indices_maxi(tab):
    m = tab[0]
    l = []
    for i in range(len(tab)):
        if tab[i] > m:
            m = tab[i]
    for i in range(len(tab)):
        if tab[i] == m:
            l.append(i)
    return (m,l)

def positif(pile):
    pile_1 = list((pile))
    pile_2 = []
    while pile_1 != []:
        x = pile_1.pop()
        if x >= 0:
            pile_2.append(x)
    while pile_2 != []:
        x = pile_2.pop()
        pile_1.append(x)
    return pile_1

# Sujet 3

def moyenne(tab):
    somme = 0
    coeff = 0
    for i in range(len(tab)):
        somme += tab[i][0]*tab[i][1]
        coeff += tab[i][1]
    if coeff == 0:
        return None
    return somme/coeff

coeur = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0], 
        [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0], 
        [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0], 
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0], 
        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def affiche(dessin):
    ''' affichage d'une grille : les 1 sont représentés par 
        des " *" , les 0 par deux espaces "  " '''
    for ligne in dessin:
        for col in ligne:
            if col == 1:
                print(" *", end="")
            else:
                print("  ", end="")
        print()


def zoomListe(liste_depart,k):
    '''renvoie une liste contenant k fois chaque 
    élément de liste_depart'''
    liste_zoom = []
    for elt in liste_depart :
        for i in range(k):
            liste_zoom.append(elt)
    return liste_zoom

def zoomDessin(grille,k):
    '''renvoie une grille où les lignes sont zoomées k fois 
    ET répétées k fois'''
    grille_zoom=[]
    for elt in grille:
        liste_zoom = zoomListe(elt,k)
        for i in range(k):
            grille_zoom.append(liste_zoom)
    return grille_zoom

# Sujet 4

def a_doublon(tab):
    for i in range(1,len(tab)):
        if tab[i-1] == tab[i]:
            return True
    return False





