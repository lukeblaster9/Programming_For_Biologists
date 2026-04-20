#!/usr/bin/python3

import gff_functions

def main():
    Fasta_name = input("Enter name of Fasta file: ")
    gff_name = input("Enter name of gff file: ")
    Output_name = input("Enter name of output file: ")
    genome_sequence = gff_functions.read_fasta(Fasta_name)
    begin, end, num_ID = gff_functions.read_gff(gff_name)
    gff_functions.write_output(Output_name, genome_sequence, begin, end, num_ID)
#set the environment for this script
#is it main(), or is this a module being called by something else?
if __name__ == "__main__":
    main()