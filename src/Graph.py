 #!/usr/bin/env python3

""" Module to manage Graph, 
	Edge and Node."""

import numpy

class Node:
	_howMany = 0
	def __init__(self, num, readValue):
		"""To initialize node, num = int,
		readValue = oject(read)"""
		Node._howMany+=1
		self.num=num
		self.readValue=readValue
		self.used=False

	def __str__(self):
		return("Node: {} value: {} used: {}".format(self.num, str(self.readValue), self.used))

class Edge:
	def __init__(self, nodeOne, nodeTwo, num):
		"""To initialize edge, self.nodeOne=object(Node)
		self.nodeTwo==object(Node)"""
		self.nodeOne=nodeOne
		self.nodeTwo=nodeTwo
		self.num=num

	def __str__(self):
		return("Edge {} connect Node {} AND Node {}".format(self.num, str(self.nodeOne.num), str(self.nodeTwo.num)))

class Graph: 
	def __init__(self, Edges):
		"""To initialize graph, 
		Edges=list(object(Edge))"""
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
