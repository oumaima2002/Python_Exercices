
#Exercice1:Tester si e appartient à une saisi

def chaine():
    a = input("Donnez une phrase");
    if('e' in a):
        print("oui");

def chaine2():
    a = input("Donnez une phrase");
    long=len(a);
    i=0;
    while(i<long):
        if a[i]=='e':
            print("trouvable à l'iteration ",i+1);
        i=i+1;


#Exercice2:Inserer un caractère d'espacement dans une chaîne de caractères

def inserer():
    b=input("saisir une chaine a recopier:");
    T=b[0];
    for i in range(1,len(b)):
       T=T+"*"+b[i];
       i=i+1;
    print(T);

#Exercice3:Inversion d'une chaîne de caractères
def inverser():
    f=input("Donnez un chaine a inverser:");
    k="";
    i=len(f)-1;
    while(i>=0):
            k+=f[i];
            i = i - 1;

    print(k);

#Exercice4:La pyramide de lettres
def pyramide():
    e=input("Donnez une chaine");
    i=1;
    while(i<=len(e)):
        print(e[:i]);
        e=e[i:];
        i=i+1;
#Chiffre de César
def cesar():
    t="abcdefghijklmnopqrstuvwxyz" ;
    p=input("Donnez une chaine a crypté par cesar");
    f = input("Donnez le pas du decodage");
    code="";
    for i in p.lower():
        pos=t.find(i);
        if(pos!=-1):
            code+=t[(pos+int(f))%len(t)];

        else:
            code+=i;
    print(code);


# Le codage Chuck Norris
# !/usr/bin/env python3
# coding: utf-8

# Codage Chuck Norris (binaire vers unaire)
def binaire2unaire(binaire, table):
    # On prépare le résultat unaire
    unaire = ""

    # Mémorisation du caractère précédent pour détecter le changement
    prev = ""

    # Il faut un compteur de répétitions
    rep = 0  # Facultatif car la première occurrence le crée. Mais pour la forme...

    # Traitement de tous les caractères du binaire
    # Comme il faudra faire un traitement après le dernier caractère
    # On lui rajoute "artificiellement" une valeur pour gérer le dernier caractère utile
    for b in binaire + ".":
        # Si le caractère a changé
        if b != prev:
            # Si on n'est pas sur le premier cas (déjà un caractère mémorisé)
            if prev:
                # On complète le unaire
                unaire += " %s %s" % (table[prev], "0" * rep)

            # Le compteur de répétitions est remis à 0 (création à la première itération si pas créé avant la boucle)
            rep = 0

            # On mémorise ce nouveau caractère
            prev = b
        # if

        # Cas général, quel que soit le caractère on incrémente la répétition
        rep += 1
    # for

    # Travail terminé (mais la chaine commence par un espace inutile)
    return unaire[1:]


# binaire2unaire()

# Décodage Chuck Norris (unaire vers binaire)
def unaire2binaire(unaire, table):
    # On crée la table de décodage en inversant clefs et valeurs de la table de codage
    decode = dict()
    for (k, v) in table.items(): decode[v] = k

    # On prépare le résultat binaire
    binaire = ""

    # On commence par découper le unaire sur l'espace
    mesg = unaire.split(" ")

    # On récupère le message découpé de 2 en 2
    for i in range(0, len(mesg), 2):
        # Le premier élément est le code, le second le nombre de répétitions
        binaire += decode[mesg[i]] * len(mesg[i + 1])

    # Travail terminé
    return binaire


# unaire2binaire()
























#Test Des Fonctions
c=input("Faire un choix svp de l'exercice voulu:");
choix=int(c);
def menu(choix):
   if (choix== 1):
       print("ex1:Tester si e appartient à une saisi");
       print("methode 1:");
       chaine();
       print("methode 2:");
       chaine2();
   else:
       if (choix==2):
           print("Exercice2:Inserer un caractère d'espacement dans une chaîne de caractères");
           inserer();

       if (choix==3):
           print("Exercice3:Inversion d'une chaîne de caractères");
           inverser();
       if (choix==4):
           print("Pyramide de lettres");
           pyramide();
       if (choix == 5):
           print("Cryptage de cesare");
           cesar();

       if (choix == 6):
           print("Cryptage binaire de Chuck Norris");
           # Test
           # La table de traduction binaire/unaire
       table = {
           "1": "0",
           "0": "00",
       }

       # Le message de base
       mesg = "10000111"

       # Le codage
       unaire = binaire2unaire(mesg, table)

       # Le décodage
       binaire = unaire2binaire(unaire, table)

       # Résultat
       print("message originel: [{}]".format(mesg))
       print("codage: [{}]".format(unaire))
       print("décodage: [{}]".format(binaire))

menu(choix);