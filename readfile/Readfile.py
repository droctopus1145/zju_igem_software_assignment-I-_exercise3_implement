from Bio import SeqIO

def read_fasta_file(fasta_file_path):
    info=[]
    all_sequences=list(SeqIO.parse(fasta_file_path, "fasta"))
    first_sequence=all_sequences[0]
    info.append(first_sequence.id)
    info.append(str(first_sequence.seq))
    #print(info)
    return info
