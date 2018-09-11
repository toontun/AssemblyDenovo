#!/usr/bin/env python
import random


""" Module to manage Genome, Read and K-mers."""


class Genome:
	def __init__(self, size, alphabet):
		self.reads=[]
		self.genome_size=size
		self.genome_alphabet=alphabet
		self.sequence=""
		for i in range(self.genome_size):
			self.sequence+=random.choice(self.genome_alphabet)
	
	def createRandomRead(self, number_of_read, read_size):
		pos_already_taken=[-1]
		for i in range(number_of_read):
			pos_random=-1
			while pos_random in pos_already_taken:
				pos_random = random.randint(0,self.genome_size)
			pos_already_taken.append(pos_random)
			if self.genome_size - pos_random > read_size:
				self.reads.append(self.sequence[pos_random:pos_random+read_size])
			else:
				self.reads.append(self.sequence[pos_random:]+self.sequence[:read_size-(self.genome_size-pos_random)])

	def __str__(self):
		return(self.sequence)