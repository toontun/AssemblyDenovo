 #!/usr/bin/env python3

""" Module to manage Graph, 
	Edge and Node."""

class Node:
	_howMany = 0
	def __init__(self, num, value):
		"""To initialize node, num = int,
		readValue = oject(read)"""
		Node._howMany+=1
		self.num=num
		self.value=value
		self.used=False

	def __str__(self):
		return("Node: {} value: {} used: {}".format(self.num, str(self.value), self.used))

class Edge:
	def __init__(self, nodeOne, nodeTwo, num):
		"""To initialize edge, self.nodeOne=object(Node)
		self.nodeTwo==object(Node). An edge from nodeOne to nodeTwo."""
		self.nodeOne=nodeOne
		self.nodeTwo=nodeTwo
		self.num=num
		self.value=nodeOne.value[:-1]+nodeTwo.value[1:]

	def __str__(self):
		return("Edge {} connect Node {} TO Node {}".format(self.num, str(self.nodeOne.num), str(self.nodeTwo.num)))			


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
		verify=len(self.listAdja)
		k=0
		for key in self.listAdja:
			if(len(self.listAdja[key])==len(self.GoInNode[key])):
				k+=1
		
		if(k==verify):
			return True
		return False
