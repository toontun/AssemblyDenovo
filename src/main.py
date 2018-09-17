 #!/usr/bin/env python3

"""Program to find the original sequence from reads of a circulary Genome randomly created or 
	given circulary genome from fasta file.Launch the program into the repository "src" with 
	the following command line:	
	python3 main.py genome_size 'availabled_nucleotides' number_of_read read_size kmer_size 
	OR
	python3 main.py fasta_file number_of_read read_size kmer_size

	where:

	genome_size is the wanted size for a random genome.

	availabled_nucletides is the nucleotides will be use to construct the genome.

	number_of_read is the number of reads.

	read_size is the wanted size for each read.

	kmer_size is the wanted size for each kmer.

	fasta_file is the path to a fasta file contains a complete circulary genome.
	
	CLASSES:

	This main use two classes, this classes need to be in the same directory that main.py:

		Genome.py
		Graph.py

	OUTPUTS:

		If this program find an eulerian cycle, it writes two fasta files in the repository 'results'.
		One is the initial genome. The other is the sequence founded with this program. 
		In the comment of the fasta file you have the used parameters. 

	For more informations read this article: 
	Compeau, P. E., Pevzner, P. A., & Tesler, G. (2011). How to apply de Bruijn graphs to genome assembly.
	Nature biotechnology,29(11), 987.
	"""

import Graph as grp
import Genome as gen
import time
import sys

if __name__ == "__main__":

	good_len_of_argv=[2,5,6]
	if(len(sys.argv) not in good_len_of_argv):
		sys.exit("COMMAND LINES:\n\npython3 main.py genome_size 'availabled_nucleotides' number_of_read read_size kmer_size"+"\n\n"+
			"OR:\n\npython3 main.py fasta_file number_of_read read_size kmer_size\n\nOR\n\npython3 main.py -help\n\n")

	if(len(sys.argv)==2):
		if(sys.argv[1]=="-help"):
			import main
			print(help(main))
			sys.exit()

	def writeFastaFile(filename, sequence, comment):
		"""little fonction to write a fasta file"""
		with open(filename, "w") as fasta:
			fasta.write(">"+comment)
			for i in range(len(sequence)):
				if(i%80!=0):
					fasta.write(sequence[i])
				else:
					fasta.write("\n"+sequence[i])

	start=time.time()
	graph=grp.Graph()

	#the two statements "if" check if the user give a fasta file to construct the genome or if we need to construct it ramdomly.
	
	if(len(sys.argv)==good_len_of_argv[2]):#without fasta file
		genome=gen.Genome(int(sys.argv[1]), sys.argv[2])
		genome.createRandomRead(int(sys.argv[3]), int(sys.argv[4]))
		genome.createKmers(int(sys.argv[5]))

	if(len(sys.argv)==good_len_of_argv[1]):#with fasta file
		seq_of_fasta=""
		with open(sys.argv[1], "r") as f:
			for line in f:
				if(line[0]!=">"):
					seq_of_fasta+=line[:-1]

		genome=gen.Genome(len(seq_of_fasta), "ATCG", seq_of_fasta)
		genome.createRandomRead(int(sys.argv[2]), int(sys.argv[3]))
		genome.createKmers(int(sys.argv[4]))


	for kmer in genome.kmers: #Function addNode manage the duplicates. Function addEdge doesn't manage duplicates because in Genome.createKmers we can't have similars kmers.
		graph.addNode(kmer[1:])
		graph.addNode(kmer[:-1])
		graph.addEdge(kmer[:-1], kmer[1:])

	if(graph.isEulerian()): 
	#if the graph is not eulerian, graph is not strongly connected and not have a eulerian cycle. 
		cycle=graph.getEulerianCycle()
		new_seq=""
		for node in cycle: #here we follow the cycle and take the edge value. Because it's an eulerian cycle in a De Bruijn Graph. 
			new_seq+=node[0]
		if(genome.isEqual(new_seq)):
			writeFastaFile("../results/initial_sequence.fasta", genome.sequence, "Initial Genome")
			writeFastaFile(
				"../results/sequence_from_cycle.fasta", new_seq, "Sequence found with De Bruijn graph. Parameters: genome_size: {}, number_of_read: {}, read_size: {}, number_of_kmer: {}, kmer_size: {}"
				.format(len(new_seq),len(genome.reads), len(genome.reads[0]), len(genome.kmers), len(list(genome.kmers.keys())[0])))
			print("\nSequence found, go to see in the repository 'results'.")
		else:
			sys.exit("We didn't find a good sequence, please restart the program.")


	else:
		sys.exit("We didn't have an eulerian graph, please restart the program.")

	end=time.time()
	print("\nTime to run the program: " + str(end-start) + " seconde(s).\n")

