#!/usr/bin/env python3

""" Module to manage Genome, 
	Read and K-mers."""

import random

class Genome:
	def __init__(self, size, alphabet):
		self.reads=[]
		self.kmers=[]
		self.kmer_suffixe=[]
		self.kmer_prefixe=[]
		self.genome_size=size
		self.genome_alphabet=alphabet
		self.sequence=""
		for i in range(self.genome_size):
			self.sequence+=random.choice(self.genome_alphabet)
	
	def createRandomRead(self, number_of_read, read_size):
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
		"""Function to get the prefixe and the suffixe from each kmer."""
		self.kmer_suffixe=[]
		self.kmer_prefixe=[]
		for kmer in self.kmers:
			self.kmer_prefixe.append(kmer[:-1])
			self.kmer_suffixe.append(kmer[1:])

	def __str__(self):
		return(self.sequence)