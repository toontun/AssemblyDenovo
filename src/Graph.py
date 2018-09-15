 #!/usr/bin/env python3

""" Module to manage Graph, 
	Edge and Node."""			


class Graph:

	def __init__(self, listAdja={}, GoInNode={}):
		"""listAdja is a dictionary represent the adjacency list of the graph, 
		which contains all nodes and their edges going out. 
		GoInNode is the same but with the edge go in the node"""
		self.listAdja=listAdja
		self.GoInNode=GoInNode

	def addNode(self, Node):
		"""Add a node to the graph"""
		if(Node not in self.listAdja):
			self.listAdja[Node]=[]
		
		if(Node not in self.GoInNode):
			self.GoInNode[Node]=[]

	def addEdge(self, NodeOne, NodeTwo):
		"""Create a edge from NodeOne to NodeTwo"""
		self.listAdja[NodeOne].append(NodeTwo)
		self.GoInNode[NodeTwo].append(NodeOne)

	def isEulerian(self):
		"""Function to check if the graph is Eulerian"""
		for key in self.listAdja:
			if(len(self.listAdja[key])!=len(self.GoInNode[key])):
				return False
		return True
