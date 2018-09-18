# Author

Adam Bellaïche

adam.bellaiche@gmail.com

https://github.com/toontun/AssemblyDenovo

University of Paris 7
M2BI
2018-2019

# Short Description

This is a program made for a project at the university of Paris 7 in master 2 of bio-informatics.
This program permit to assemble de novo a genome from reads.

# Needed Files 

* Genome.py
* Graph.py
* Optional: fasta file


# How to use it

* make sure you have python3
* make sure you are in the repository "src" with:
	* Genome.py
	* Graph.py
	* main.py

* commands to run main.py:
	* python3 main.py -help
	* python3 main.py    genome_size   available_nucleotides   read_number   read_size   kmer_size
	* python3 main.py    path_to_fasta_file   read_number  read_size    kmer_size

* command to have help on class Genome or Graph:
	* python3 Genome.py
	* python3 Graph.py

# Some examples

* python3 main.py 10 "ATCG" 9 9 8
	* genome_size = 10
	* available nucleotide = "ATCG"
	* read_number = 9
	* read_size = 9
	* kmer_size = 8

* python3 main.py ..\data\mycoplasma.fna 200000 400 300
	* fasta_file = ..\data\mycoplasma.fna
	* read_number = 200000
	* read_size = 400
	* kmer_size = 300

* python3 main.py 100000 "ATCG" 50000 100 55
	* genome_size = 100000
	* available nucleotides = "ATCG"
	* read_number = 50000
	* read_size = 100
	* kmer_size = 55

# Documentation

* with command line: see in "How to use it" with help function. 
* go to AssemblyDenovo/doc/pythonDoc/Doxygen_doc/index.html
* you have the rules for the project and the article in AssemblyDenovo/doc/projectInfo
* you have the report for the project in AssemblyDenovo/doc/RapportPC.pdf
* you have a UML diagram in AssemblyDenovo/doc/UML.pdf
