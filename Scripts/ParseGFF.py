#!/usr/bin/env python3

import argparse

##----------------------accept and parse command line arguments
# create an argument parser object
parser = argparse.ArgumentParser(description="This script reads in Fasta and GFF files")

#add a positional argument, in this case, the the computer you want to run your slurm script on
parser.add_argument("Fasta_name", help="Choose fasta file")
parser.add_argument("GFF_name", help="Choose GFF file")

args = parser.parse_args()

# put the filename – and path if necessary – in a variable

# open the file
file_path=file_path="../Data/covid_genome/"
#Fasta = open(file_path+str(args.Fasta_name), "r")
#GFF= open(file_path+str(args.GFF_name), "r")
# we created a variable ('genome') when we opened the file: what is it?

#dna_sequence = Fasta.read()

with open(file_path+str(args.Fasta_name), "r") as Fasta:
    #read the file line by line
    header=next(Fasta)
    for line in Fasta:
        #print just to make sure we're reading the file okay
        # print(line, end="")

        # strip the line breaks
        line = line.strip()
        genome_sequence=line
        
with open(file_path+str(args.GFF_name), "r") as GFF:
    #read the file line by line
    #header=next(GFF)
    for line in GFF:
        #print just to make sure we're reading the file okay
        # print(line, end="")

        # strip the line breaks
        line = line.strip()
        print(line)
      

        