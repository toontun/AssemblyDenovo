#!/usr/bin/env python3

""" Module to manage Genome, 
	Read and K-mers."""

import random

class Genome:
	def __init__(self, size, alphabet):
		"""To init a Genome with a random sequence, size = int, alphabet are the nucleotides needed like "ATCG" or
		just "AC" so alphabet=string.""" 
		self.reads=[]
		self.kmers=[]
		self.kmers_sufpref=[]
		self.genome_size=size
		self.genome_alphabet=alphabet
		self.sequence=""
		for i in range(self.genome_size):
			self.sequence+=random.choice(self.genome_alphabet)
	
	def createRandomRead(self, number_of_read, read_size):
		"""To create Random Read from the Genome. Just give number of read wanted and their size. Both is int"""
		if(read_size>self.genome_size):
			print("read biger than genome")
			return False
		self.reads=[]
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
				#the genome is circular. 
	
	def createKmers(self, kmer_size):
		"""Function to create kmers with a specific size from each read"""
		if(kmer_size>len(self.reads[0])):
			print("size of kmers > size of reads")
			return False
		self.kmers=[]
		for read in self.reads:
			for i in range(len(read)-kmer_size+1):
				self.kmers.append(read[i:i+kmer_size])
	
	def createSuffixePrefixe(self):
		"""Function to get the prefixe and the suffixe from each kmer stocked into Genome.kmers_sufpref."""
		self.kmers_sufpref=[]
		for kmer in self.kmers:
			suffixe=kmer[1:]
			prefixe=kmer[:-1]
			if(suffixe not in self.kmers_sufpref):
				self.kmers_sufpref.append(suffixe)
			if(prefixe not in self.kmers_sufpref):
				self.kmers_sufpref.append(prefixe)

	def __str__(self):
		return(self.sequence)