#!/usr/bin/python3

file_path="../Data/covid_genome/"

#define the read_fasta function
def read_fasta(filename):
    #Make an empty string to store the genome sequence
    genome_sequence=""
    with open(file_path + filename, "r") as Fasta:
        #Skip the header
        header=next(Fasta)
        #Read line by line through the Fasta file
        for line in Fasta:
            # strip the line breaks
            line = line.strip()
            #Add each line to genome_sequence to make one 
            #Large string of the genome
            genome_sequence +=line
    return genome_sequence

#define the read_gff function
def read_gff(filename):
    #Make an empty list to store the beginning coordinates  
    begin=[]
    #Make an empty list to store the end coordinates
    end=[]
    #Make an empty list to store the unique IDs
    num_ID=[]     
    with open(file_path + filename, "r") as GFF:
        for line in GFF:
            columns = line.strip().split('\t')
            if len(columns) >= 9:
                begin_start = int(columns[3])
                begin.append(begin_start)
                end_start = int(columns[4])
                end.append(end_start)
                num_ID_start = columns[8]
                num_ID.append(num_ID_start.split("ID=")[1].split(";")[0].split(":")[0])
    return begin, end, num_ID

def write_output(filename, genome_sequence, begin, end, num_ID):
    with open(file_path + filename, "w") as covid_genome:
        for i in range(len(begin)):
            print(num_ID[i], file=covid_genome)
            print(genome_sequence[begin[i]:end[i]], file=covid_genome)
