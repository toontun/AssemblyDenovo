 #!/usr/bin/env python3

"""Program to find the original sequence from reads of a circulary Genome randomly created or 
	given circulary genome from fasta file.Launch the program into the repository "src" with 
	the following command line:	
	python3 main.py genome_size 'availabled_nucleotides' number_of_read read_size kmer_size """

import time
import Graph as grp
import Genome as gen
import sys 

if __name__ == "__main__":

	good_len_of_argv=[5,6]
	if(len(sys.argv) not in good_len_of_argv):
		sys.exit("COMMAND LINES:\n\npython3 main.py genome_size 'availabled_nucleotides' number_of_read read_size kmer_size"+"\n\n"+
			"OR:\n\npython3 main.py fasta_file number_of_read read_size kmer_size\n")

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

	if(len(sys.argv)==good_len_of_argv[1]):
		genome=gen.Genome(int(sys.argv[1]), sys.argv[2])
		genome.createRandomRead(int(sys.argv[3]), int(sys.argv[4]))
		genome.createKmers(int(sys.argv[5]))

	if(len(sys.argv)==good_len_of_argv[0]):
		seq_of_fasta=""
		with open(sys.argv[1], "r") as f:
			for line in f:
				if(line[0]!=">"):
					seq_of_fasta+=line[:-1]

		genome=gen.Genome(len(seq_of_fasta), "ATCG", seq_of_fasta)
		genome.createRandomRead(int(sys.argv[2]), int(sys.argv[3]))
		genome.createKmers(int(sys.argv[4]))


	for kmer in genome.kmers:
		graph.addNode(kmer[1:])
		graph.addNode(kmer[:-1])
		graph.addEdge(kmer[:-1], kmer[1:])

	if(graph.isEulerian()): 
	#if the graph is not eulerian, graph is not strongly connected and not have a eulerian cycle. 
		cycle=graph.getEulerianCycle()
		new_seq=""
		for node in cycle:
			new_seq+=node[0]
		if(genome.isEqual(new_seq)):
			writeFastaFile("../results/initial_sequence.fasta", genome.sequence, "Initial Genome")
			writeFastaFile(
				"../results/sequence_from_cycle.fasta", new_seq, "Sequence found with De Bruijn graph. Parameters: genome_size: {}, number_of_read: {}, read_size: {}, number_of_kmer: {}, kmer_size: {}"
				.format(len(new_seq),len(genome.reads), len(genome.reads[0]), len(genome.kmers), len(list(genome.kmers.keys())[0])))
			print("Sequence found, go to see in results")
		else:
			sys.exit("We didn't find a good sequence, please restart the program.")


	else:
		sys.exit("We didn't have an eulerian graph, please restart the program.")

	end=time.time()
	print(end-start)

