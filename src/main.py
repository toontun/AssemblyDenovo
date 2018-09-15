 #!/usr/bin/env python3
import time
start=time.time()
import Graph as grp
import Genome as gen
import sys 

#genome_size, genome_alphabet, Read_Number, Read_size, Kmer_size
if(len(sys.argv)!=6):
	sys.exit("command line: genome_size, 'availabled_nucleotides', number_of_read, read_size, kmer_size")

gen1=gen.Genome(int(sys.argv[1]), sys.argv[2])
gen1.createRandomRead(int(sys.argv[3]), int(sys.argv[4]))
gen1.createKmers(int(sys.argv[5]))

g=grp.Graph()

for kmer in gen1.kmers:
    g.addNode(kmer[1:])
    g.addNode(kmer[:-1])
    g.addEdge(kmer[:-1], kmer[1:])

if(g.isEulerian()):
	cycle=g.getEulerianCycle()

end=time.time()
t=end-start
print(t)