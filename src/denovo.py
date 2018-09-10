import numpy
import random

class Read:
	def __init__(self, seq="error"):
		"""Initialisation du read, seq = string"""
		self.seq=seq

	def __str__(self):
		return self.seq 

	def __len__(self):
		return(len(self.seq))

class Node:
	_howMany = 0
	def __init__(self, num, readValue):
		"""Initialisation d'un noeud, num = int,
		readValue = oject(read)"""
		Node._howMany+=1
		self.num=num
		self.readValue=readValue
		self.used=False

	def __str__(self):
		return("Node: {} value: {} used: {}".format(self.num, str(self.readValue), self.used))

class Edge:
	def __init__(self, nodeOne, nodeTwo, num):
		"""Initialisation d'une arrête, self.nodeOne=object(Node)
		self.nodeTwo==object(Node)"""
		self.nodeOne=nodeOne
		self.nodeTwo=nodeTwo
		self.num=num

	def __str__(self):
		return("Edge {} connect Node {} AND Node {}".format(self.num, str(self.nodeOne.num), str(self.nodeTwo.num)))

class Graph: 
	def __init__(self, Edges):
		"""Initialisation d'un graph, Edges=list(object(Edge))"""
		self.edges=Edges
		self.matrixAdja=numpy.zeros((Node._howMany, Node._howMany))
		self.listAdja={}
		self.initMatrix()
		self.initListeAdja()

	def initMatrix(self):
		for edge in self.edges:
			self.matrixAdja[edge.nodeOne.num][edge.nodeTwo.num]=1
			self.matrixAdja[edge.nodeTwo.num][edge.nodeOne.num]=1
		for i in range(Node._howMany):
			self.matrixAdja[i][i]=1
	
	def initListeAdja(self):
		for edge in self.edges:
			if edge.nodeOne.num not in self.listAdja:
				self.listAdja[edge.nodeOne.num]=[]
			if edge.nodeOne.num in self.listAdja:
				self.listAdja[edge.nodeOne.num].append(edge.nodeTwo.num)
			if edge.nodeTwo.num not in self.listAdja:
				self.listAdja[edge.nodeTwo.num]=[]
			if edge.nodeTwo.num in self.listAdja:
				self.listAdja[edge.nodeTwo.num].append(edge.nodeOne.num)				

	def __str__(self):
		display="\n"
		for edge in self.edges:
			display=display+str(edge)+"\n"
		display+="\n"+str(self.listAdja)
		display+="\n\n"+str(self.matrixAdja)
		return(display)

class Genome:
	def __init__(self, size, alphabet):
		self.genome_size=size
		self.genome_alphabet=alphabet
		self.sequence=""
		for i in range(self.genome_size):
			self.sequence+=random.choice(self.genome_alphabet)

readOne= Read("CCCCCCCC")
readTwo= Read("ATCGCTGA")
readThree= Read("TTTCTATC")
readFour= Read("TCATCTAAA")
NodeOne=Node(0, readOne)
NodeTwo=Node(1, readTwo)
NodeThree= Node(2, readThree)
NodeFour= Node(3, readFour)
EdgeOne=Edge(NodeOne, NodeTwo, 0)
EdgeTwo= Edge(NodeThree, NodeFour, 1)
EdgeThree= Edge(NodeOne, NodeFour, 2)
EdgeFour= Edge(NodeTwo, NodeThree, 3)
Edges=[EdgeOne, EdgeTwo, EdgeThree, EdgeFour]
graph1 = Graph(Edges)
print(graph1)

gen1=Genome(10000, "ATCG")
print(gen1.sequence)



#ajouter l'alphabet
#ajouter l'overlap longueur
#ajouter le génome peut être
#ajouter les k-mers des reads et leur longeurs
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