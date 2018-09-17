#!/usr/bin/env python3

""" Module to manage Genome, 
	Read and K-mers.

	Use it in main.py.
	"""

import random

class Genome:
	def __init__(self, size, alphabet, sequence=""):

		"""To init a Genome with a random sequence or given sequence, 
			size = int, 
			alphabet are the availabled nucleotides so alphabet=string,
			sequence is a string.
			"""
		
		self.reads=[]
		self.kmers={}
		self.genome_size=size
		self.genome_alphabet=alphabet
		self.sequence=sequence
		if(not sequence):
			for i in range(self.genome_size):
				self.sequence+=random.choice(self.genome_alphabet)
	
	def createRandomRead(self, number_of_read, read_size):

		"""To create Random Read from the Genome. Just give number of read wanted and their size. Both is int."""

		if(read_size>self.genome_size):
			print("read biger than genome")
			return False
			
		self.reads=[""]*number_of_read
		pos_not_taken=list(range(self.genome_size))
		for i in range(number_of_read):
			pos_random=random.choice(pos_not_taken)
			pos_not_taken.remove(pos_random)
			if self.genome_size - pos_random > read_size:
				self.reads[i]=self.sequence[pos_random:pos_random+read_size]
			else:
				self.reads[i]=self.sequence[pos_random:]+self.sequence[:read_size-(self.genome_size-pos_random)]
				#the genome is circular.
		
	def createKmers(self, kmer_size):

		"""Function to create kmers with a specific size from each read. Accept a kmer only once. We can not have similar kmer.
		kmer_size is int."""

		if(kmer_size>len(self.reads[0])):
			print("size of kmers > size of reads")
			return False
		self.kmers={}
		for read in self.reads:
			for i in range(len(read)-kmer_size+1):
				if(read[i:i+kmer_size] not in self.kmers):
					self.kmers[read[i:i+kmer_size]]=1
				else:
					self.kmers[read[i:i+kmer_size]]+=1
	
	def isEqual(self, other_sequence):

		"""Function to test if the circulary genome is equal to another sequence, even if there are rotations.
		Return true if genome are equal, if not return false.
		other_sequence is a string.""" #function taken here: https://www.geeksforgeeks.org/a-program-to-check-if-strings-are-rotations-of-each-other/

		temp=''
		other_sequence_size=len(other_sequence)

		if(self.genome_size!=other_sequence_size):
			return False

		temp = other_sequence + other_sequence

		if(temp.count(self.sequence)>0):
			return True
		else:
			return False

	def __str__(self):
		return(self.sequence)

if __name__=="__main__":
	import Genome
	print(help(Genome))