import time
start=time.time()
import Graph as grp
import Genome as gen
import sys 

#genome_size, genome_alphabet, Read_Number, Read_size, Kmer_size
if(len(sys.argv)!=6):
	sys.exit("command line: genome_size, 'availabled_nucleotides', number_of_read, read_size, kmer_size")

gen1=gen.Genome(int(sys.argv[1]), sys.argv[2])
gen1.createRandomRead(int(sys.argv[3]), int(sys.argv[4]))
gen1.createKmers(int(sys.argv[5]))

g=grp.Graph()

for kmer in gen1.kmers:
    g.addNode(kmer[1:])
    g.addNode(kmer[:-1])
    g.addEdge(kmer[:-1], kmer[1:])
# print(gen1)
# print(gen1.kmers)
# print(g.listAdja)
end=time.time()
t=end-start
print(t)
# i=0
# nodes=[]
# for value in gen1.kmers_sufpref:
#     nodes.append(grp.Node(i, value))
#     i+=1

# edges=[]
# k=0

# for i in range(len(nodes)):
#     for j in range(len(nodes)):
#         if(nodes[i].value[1:]==nodes[j].value[:-1]):
#             if(nodes[i].value[:-1]+nodes[j].value[1:] in gen1.kmers):
#                 edges.append(grp.Edge(nodes[i], nodes[j], k))
#                 k+=1

# g1=grp.Graph(edges)

# print(g1.listAdja)
# print(g1.Node.howMany)
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
