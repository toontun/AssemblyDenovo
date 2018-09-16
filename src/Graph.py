#!/usr/bin/env python3

""" Module to manage Graph, 
	Edge and Node. This class is oriented for a De Bruijn graph."""			

import random
import copy

class Graph:

	def __init__(self, list_adja={}, go_in_node={}):

		"""Init a graph: list_adja is a dictionary represent the adjacency list of the graph, 
		which contains all nodes and for each node, the connected node by a outgoing edge. 
		go_in_node is the same but with incoming edge, each node contains a list of node connected by incoming edge."""

		self.list_adja=list_adja
		self.go_in_node=go_in_node
		self._number_edge=0

	def addNode(self, Node):

		"""Add a node to the graph if the node doesn't exist."""

		if(Node not in self.list_adja):
			self.list_adja[Node]=[]
		
		if(Node not in self.go_in_node):
			self.go_in_node[Node]=[]

	def addEdge(self, node_one, node_two):

		"""Create a edge from node_one to node_two"""

		self.list_adja[node_one].append(node_two)
		self._number_edge+=1
		self.go_in_node[node_two].append(node_one)

	def isEulerian(self):

		"""Function to check if the graph is Eulerian. Return true if graph is eulerian, if not return false."""

		if(not self.list_adja and not self.go_in_node): #means graph is empty
			return False
		for key in self.list_adja:
			if(len(self.list_adja[key])!=len(self.go_in_node[key])):
				return False
		return True

	def getEulerianCycle(self):

		"""Function to have an eulerian cycle of the graph. Return a list of vertices. Follow the vertices one by one to retrieve the cycle."""

		copy_list_adja=copy.deepcopy(self.list_adja) #we need copy it because each time an edge is used we will delete it in the copy of the adjacency list. 
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
				copy_list_adja[current_node].remove(next_node)#because we can take an edge just once. 
				cycle[pos_in_cycle]=next_node
				pos_in_cycle+=1
				current_node=next_node
			
			else:#here we come back at the starting node but somes edges are not used. So we restart the course at a node with outgoing edge.				
				cycle_bis=[""]*self._number_edge 
				for node in cycle:
					if(copy_list_adja[node]):#check node with outgoing edge. 
						starting_node=node
						current_node=starting_node
						cycle_bis[0]=starting_node
						pos_in_cycle_bis=1
						break

				copy_list_adja=copy.deepcopy(self.list_adja)#so we copy adjacency list one more time because we need to restart our old-course.
				while(cycle):#if cycle is empty, we run on the entire cycle. 
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