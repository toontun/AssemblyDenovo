 #!/usr/bin/env python3

""" Module to manage Graph, 
	Edge and Node."""			
import random
import copy

class Graph:

	def __init__(self, listAdja={}, GoInNode={}):
		"""listAdja is a dictionary represent the adjacency list of the graph, 
		which contains all nodes and their edges going out. 
		GoInNode is the same but with the edge go in the node"""
		self.listAdja=listAdja
		self.GoInNode=GoInNode
		self._number_edge=0

	def addNode(self, Node):
		"""Add a node to the graph"""
		if(Node not in self.listAdja):
			self.listAdja[Node]=[]
		
		if(Node not in self.GoInNode):
			self.GoInNode[Node]=[]

	def addEdge(self, NodeOne, NodeTwo):
		"""Create a edge from NodeOne to NodeTwo"""
		self.listAdja[NodeOne].append(NodeTwo)
		self._number_edge+=1
		self.GoInNode[NodeTwo].append(NodeOne)

	def isEulerian(self):
		"""Function to check if the graph is Eulerian"""
		if(not self.listAdja and not self.GoInNode): #means graph is empty
			return False
		for key in self.listAdja:
			if(len(self.listAdja[key])!=len(self.GoInNode[key])):
				return False
		return True

	def getEulerianCycle(self):
		copy_list_adja=copy.deepcopy(self.listAdja) #we need copy it because each time an edge is used we will delete it in the copy of the adjacency list. 
		#we use deepcopy because our dictionary contains list. 
		cycle=[""]*self._number_edge
		starting_node=random.choice(tuple(copy_list_adja.keys()))
		current_node="tmp"
		cycle[0]=starting_node
		pos_in_cycle=1 #indicate where we are in "cycle". We start at 1 because 0 is the starting node. 
		

		while(pos_in_cycle!=self._number_edge):
			
			if(current_node!=starting_node):#because we can only get stuck at the starting_node. cf: https://www.youtube.com/watch?v=_x4IVlsw_q4&list=PLQ-85lQlPqFNGdaeGpV8dPEeSm3AChb6L&index=9
				if(pos_in_cycle==1):
					current_node=starting_node
				next_node=random.choice(tuple(copy_list_adja[current_node]))
				copy_list_adja[current_node].remove(next_node)
				cycle[pos_in_cycle]=next_node
				pos_in_cycle+=1
				current_node=next_node
			
			else:
				copy_list_adja=copy.deepcopy(self.listAdja)
				cycle_bis=[""]*self._number_edge 
				for node in cycle:
					if(copy_list_adja[node]):
						starting_node=node
						current_node=starting_node
						cycle_bis[0]=starting_node
						pos_in_cycle_bis=1
						break

				while(cycle):#if cycle is empty, we done the same path. 
					for node in cycle:
						if(node in copy_list_adja[current_node]):
							next_node = node
							cycle_bis[pos_in_cycle_bis]=next_node
							pos_in_cycle_bis+=1
							copy_list_adja[current_node].remove(next_node)
							cycle.remove(next_node)
							current_node=next_node
				
				pos_in_cycle=pos_in_cycle_bis
				cycle=list.copy(cycle_bis)

		return cycle