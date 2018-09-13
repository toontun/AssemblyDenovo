import Graph as grp
import Genome as gen


gen1=gen.Genome(100, "ATCG")
gen1.createRandomRead(5, 10)
gen1.createKmers(4)
gen1.createSuffixePrefixe()


i=0
nodes=[]
for value in gen1.kmers_sufpref:
    nodes.append(grp.Node(i, value))
    i+=1

edges=[]
k=0
for i in range(len(nodes)):
    for j in range(len(nodes)):
        if(nodes[i].value[1:]==nodes[j].value[:-1]):
            if(nodes[i].value[:-1]+nodes[j].value[1:] in gen1.kmers):
                edges.append(grp.Edge(nodes[i], nodes[j], k))
                k+=1

#ajouter l'overlap longueur
#link entre noeud et arrête pour savoir si la fourmi peut l'emprunter.
#rajouter un +1 à un compteur, si le compteur est égale au nombre d'arrête alors on a un cycle d'euler.
#si on fait un parcours qui ne fait pas toutes les arrêtes, on en fait un deuxième qui passe
	#par les arrêtes non utilisées et on essaie de concaténer les deux. 
#créer le génome aléatoirement et faire les read aléatoirement (on prend
	#une position aléatoire + size_of_read == read)
#du coup les read sont divisés en kmer de 20 pour l'instant
#ensuite on prend tous les suffixes et préfixes et on regarde lesquels se complètent
# on en fait une arrête si un suffixe et un préfixe se complètent bien. 
#après on vérifie que ce graph est connexe. A la limite on peut vérifier
#les in and out degree. 
#si le graph est connexe on lance les algo de recherche du cycle de Euler
#sinon je sais pas ce qu'il faut faire.
#une fois qu'on a trouvé le cycle, l'afficher (voir module en python)
#testé si le genome trouvé est ok en sachant qu'il est circulaire. 
# on verra pour les extensions.  
