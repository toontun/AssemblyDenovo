 #!/usr/bin/env python3

""" Module to manage Graph, 
	Edge and Node."""

import numpy

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
		self.nodeTwo==object(Node)"""
		self.nodeOne=nodeOne
		self.nodeTwo=nodeTwo
		self.num=num
		self.value=nodeOne.value[:-1]+nodeTwo.value[1:]

	def __str__(self):
		return("Edge {} connect Node {} TO Node {}".format(self.num, str(self.nodeOne.num), str(self.nodeTwo.num)))

class Graph: 
	def __init__(self, Edges):
		"""To initialize graph, 
		Edges=list(object(Edge))"""
		self.edges=Edges
		self.matrixAdja=numpy.zeros((Node._howMany, Node._howMany))
		self.listAdja={}
		if(len(Edges)!=0):
			self.__initMatrix()
			self.__initListeAdja()

	def __initMatrix(self):
		"""Create an adjacency matrix"""
		for edge in self.edges:
			self.matrixAdja[edge.nodeOne.num][edge.nodeTwo.num]=1
	
	def __initListeAdja(self):
		"""Create an adjacency list"""
		for edge in self.edges:
			if edge.nodeOne.num not in self.listAdja:
				self.listAdja[edge.nodeOne.num]=[edge.nodeTwo.num]
			else:
				self.listAdja[edge.nodeOne.num].append(edge.nodeTwo.num)			

	def __str__(self):
		display="\n"
		for edge in self.edges:
			display=display+str(edge)+"\n"
		display+="\n"+str(self.listAdja)
		display+="\n\n"+str(self.matrixAdja)
		return(display)
