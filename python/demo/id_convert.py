import math 
import sys
from typing import List


## Je définis une fonction qui aura la responsabilité de vérifier la notation en 8bits du quad décimal
def checkByte8bitsNotation(notationToCheck: List[str]):

    ## si vous voulez compter des caractères il faut que l'entité soit comptable donc par exemple
    ## qu'elle soit un itérable par exemple une Liste
    if not isinstance(notationToCheck, List): raise TypeError("⛔️ notationToCheck must be a list")
    
    if not len(notationToCheck) == 8:
        while not len(notationToCheck) == 8:
            notationToCheck.insert(0, "0")


## Je définis une fonction de conversion d'une adresse IP en quad décimal en binaire
def convertIpDecimalAddressToBinary(ip: str): 
    # je récupère un ip en décimales ex: 192.168.1.1
    # son type c'est une chaîne de caractères

    #je vérifie que le type soit bien une chaîne de caractères
    if not isinstance(ip, str): raise TypeError("I want a string")
    #------------------------------------------------------------


   

    #je transformer la chaîne en liste et le séparateur est le "."

    bits_group = ip.split(".")

    #je veux qu'il y ait 4 quad décimals 
    if not len(bits_group) == 4: raise ValueError("⛔️ IP must be made up of 4 bytes");

    """ 
    il s'agit d'un commentaire sur plusieurs lignes
    
    j'initialise une variable binary_quads en liste (vide [])
    qui récupérera au fur et à mes bytes (8bits) 
    sous forme de chaîne de caractères composée de 0 et de 1 
    
    """
    binary_quads = []


    # une boule ex "for in" permet d'itérer ( de répéter une opération ) 
    # sur un itérable (par exemple une liste)

    for quad in bits_group:

        # Je dois convertir quad qui est une chaîne de caractères 
        # en nombre à virgule flottante (un nombre décimal)
        float_quad = float(quad)

        ## j'initialise une variable qui est une liste de chaînes de caractères ( string)  
        quad_to_bin: List[str] = []
   
        # Une boucle démarre en mode True autrement dit elle sera infinie sauf
        # si on atteint l'instruction break qui permettra de sortir de la boucle
        while True:   
            
            # si la division du flottant (qui représente le byte à la première itération) par 2 
            # ne donne pas 0 alors tu divises la valeur du flottant par 2
            # tu arrondis à l'unité inférieure si le résultat est décimal et tu stockes la valeur 
            # dans la variable qui représente le flottant
            # tu ajoutes le reste de la division à la liste des bits qui représe le byte 
            if not str(float_quad / 2).startswith("0"):
                left = math.floor(float_quad % 2) 
                quad_to_bin.append(str(left)) 
                float_quad = math.floor(float_quad / 2)
            else:
                # si c'est égale à 0 alors tu stockes le reste de la division converti en str dans la liste
                # représentant les bits du byte
                # et tu mets fin à la boucle avec l'instruction break
                left = math.floor(float_quad % 2) 
                quad_to_bin.append(str(left))
                break;
        # une fois que le break est arrivé
        # tu inverses l'ordre des éléments de la liste des bits représentant le byte de 8bits (IPv4)
        quad_to_bin.reverse()

        # tu vérifies si le byte est représenté par 8 (0 / 1) 
        # si ce n'est pas le cas tu ajoutes des 0 à gauche du ou des 0 ou 1 déjà présents
        # jusqu'à ce que cela fasse 8
        checkByte8bitsNotation(quad_to_bin)
        
        ## Je transforme la liste de bits représentant le byte en une chaîne de caractères en effaçant
        ## la virgule qui les sépare dans la liste
        quad_to_bin = "".join(quad_to_bin)

        ## j'ajoute cette chaîne de bits représentant le byte à tableau qui EST déclaré à l'extérieur
        ## de toute boucle et qui représentant la conversion de toutes les bytes décimaux en bytes binaires
        binary_quads.append(quad_to_bin)
    ## je transforme en chaîne de caractères 
    ## la liste représentant les différents bytes constituant l'adresse IP en binaire
    ## séparant les éléments par un ".""
    binary_quads = ".".join(binary_quads)   
    print("--------------------------")
    print("✅ L'adresse IP en décimal (en IPv4) : {0} devient en binaire {1} ".format(sys.argv[1], binary_quads))  
    print("--------------------------")


## je passe à la fonction le deuxième arguments qui suit l'interpréteur dans le terminal 
## le premier argument étant le nom du fichier à interpréter
convertIpDecimalAddressToBinary(ip=sys.argv[1])