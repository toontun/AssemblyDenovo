 #!/usr/bin/env python3

"""Program to find the original sequence from reads of a circulary Genome randomly created.
	Launch the program into the repository "src" with the following command line:
	python3 main.py genome_size 'availabled_nucleotides' number_of_read read_size kmer_size """

import time
import Graph as grp
import Genome as gen
import sys 

if __name__ == "__main__":

	if(len(sys.argv)!=6):
		sys.exit("command line: genome_size, 'availabled_nucleotides', number_of_read, read_size, kmer_size")

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


	random_genome=gen.Genome(int(sys.argv[1]), sys.argv[2])
	random_genome.createRandomRead(int(sys.argv[3]), int(sys.argv[4]))
	random_genome.createKmers(int(sys.argv[5]))

	for kmer in random_genome.kmers:
		graph.addNode(kmer[1:])
		graph.addNode(kmer[:-1])
		graph.addEdge(kmer[:-1], kmer[1:])

	if(graph.isEulerian()): 
	#if the graph is not eulerian, graph is not strongly connected and not have a eulerian cycle. 
		cycle=graph.getEulerianCycle()
		new_seq=""
		for node in cycle:
			new_seq+=node[0]
		if(random_genome.isEqual(new_seq)):
			writeFastaFile("../results/initial_sequence.fasta", random_genome.sequence, "Initial Genome")
			writeFastaFile("../results/sequence_from_cycle.fasta", new_seq, "Sequence found with De Bruijn graph.")
			print("Sequence found, go to see in results")
		else:
			sys.exit("We didn't find a good sequence, please restart the program.")


	else:
		sys.exit("We didn't have an eulerian graph, please restart the program.")

	end=time.time()
	print(end-start)

