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
		with open(filename, "w") as fasta:
			fasta.write(">"+comment)
			for i in range(len(sequence)):
				if(i%80!=0):
					fasta.write(sequence[i])
				else:
					fasta.write("\n"+sequence[i])

	start=time.time()
	g=grp.Graph()


	gen1=gen.Genome(int(sys.argv[1]), sys.argv[2])
	gen1.createRandomRead(int(sys.argv[3]), int(sys.argv[4]))
	gen1.createKmers(int(sys.argv[5]))

	for kmer in gen1.kmers:
		g.addNode(kmer[1:])
		g.addNode(kmer[:-1])
		g.addEdge(kmer[:-1], kmer[1:])

	if(g.isEulerian()):
		cycle=g.getEulerianCycle()
		newseq=""
		for node in cycle:
			newseq+=node[0]
		if(gen1.isEqual(newseq)):
			writeFastaFile("../results/initial_sequence.fasta", gen1.sequence, "Initial Genome")
			writeFastaFile("../results/sequence_from_cycle.fasta", newseq, "Sequence found with De Bruijn graph.")
			print("Sequence found, go to see in results")
		else:
			sys.exit("We didn't find a good sequence, please restart the program.")


	else:
		sys.exit("We didn't have an eulerian graph, please restart the program.")

	end=time.time()
	print(end-start)

